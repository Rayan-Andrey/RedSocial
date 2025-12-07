from flask import Flask, render_template, request, jsonify
from entities.city import City 
from entities.user import User
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

#Cities
"""
@app.route('/cities')
def cities():
    cities = get_all()
    return render_template('cities.html', cities=cities)
    #return get_all()
"""

@app.route('/cities', methods = ['POST'])
def save_city():
    data = request.get_json()
    c = City(name = data['name'])    
    id = c.save()
    success = id is not None
    return jsonify(success), 201

@app.route('/cities/<int:id>', methods = ['PUT'])
def update_city(id):
    data = request.get_json()
    name = data.get('name')
    c = City(id = id)
    success = c.update(name)

    return jsonify(success = success),(200 if success else 404)

@app.route('/cities/<int:id>', methods = ['DELETE'])
def delete_city(id):
    c = City(id = id)
    success = c.delete()
    return jsonify(success = success), (200 if success else 404)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5150)