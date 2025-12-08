from flask import Flask, render_template, request, jsonify
from entities.user import User
from entities.likes import Like
from entities.threads import Thread
from entities.coments import Coment
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Users
@app.route('/users')
def users():
    users = User.get_all_user()   # Llamamos al método
    return render_template('users.html', users=users)

@app.route('/users', methods=['POST'])
def save_user():
    data = request.get_json()

    u = User(
        nombre=data['nombre'],
        correo=data['correo'],
        edad=data.get('edad'),
        foto_perfil=data.get('foto_perfil')
    )

    id = u.save_user()
    success = id is not None

    return jsonify(success=success), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()

    u = User(id=id)
    success = u.update_user(
        nombre=data.get('nombre'),
        correo=data.get('correo'),
        edad=data.get('edad'),
        foto_perfil=data.get('foto_perfil')
    )

    return jsonify(success=success), (200 if success else 404)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    u = User(id=id)
    success = u.delete_user()
    return jsonify(success=success), (200 if success else 404)


#Threads
@app.route('/threads', methods=['GET'])
def get_all_thread():
    threads = Thread.get_all_thread()
    return render_template("threads.html", threads=threads)


@app.route('/threads', methods=['POST'])
def save_thread():
    data = request.get_json()

    h = Thread(
        categoria=data.get('categoria'),
        imagen=data.get('imagen'),
        contenido=data.get('contenido'),
        titulo=data['titulo'],
        usuario_id=data['usuario_id']
    )

    id = h.save_thread()
    return jsonify(success=id is not None, id=id), 201


@app.route('/threads/<int:id>', methods=['PUT'])
def update_thread(id):
    data = request.get_json()

    h = Thread(id=id)
    success = h.update_thread(
        categoria=data.get('categoria'),
        imagen=data.get('imagen'),
        contenido=data.get('contenido'),
        titulo=data.get('titulo'),
    )

    return jsonify(success=success), (200 if success else 404)


@app.route('/threads/<int:id>', methods=['DELETE'])
def delete_thread(id):
    h = Thread(id=id)
    success = h.delete_thread()
    return jsonify(success=success), (200 if success else 404)



#Cities



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5150)