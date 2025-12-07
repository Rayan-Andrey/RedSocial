from flask import Flask, render_template, request, jsonify
from entities.city import City, get_all
from entities.costumer import Costumer, get_all
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cities')
def cities():
    for c in get_all():
        print(c.name)
    return render_template('cities.html')
    #return get_all()

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

#Costumers
@app.route('/costumers')
def costumer():
    for c in get_all():
        print(c.costumer_name)
    return render_template('costumers.html')
    #return get_all()

@app.route('/costumers', methods = ['POST'])
def save_costumer():
    data = request.get_json()
    c = Costumer(name = data['costumer_name'],email = data['costumer_email'],zip =data['costumer_zip_code'],phone = data['costumer_phone'])    
    id = c.save()
    success = id is not None
    return jsonify(success), 201

@app.route('/costumers/<int:id>', methods = ['PUT'])
def update_costumer(id):
    data = request.get_json()
    name = data.get('name')
    c = Costumer(id = id)
    success = c.update(name)

    return jsonify(success = success),(200 if success else 404)

@app.route('/costumers/<int:id>', methods = ['DELETE'])
def delete_costumer(id):
    c = Costumer(id = id)
    success = c.delete()
    return jsonify(success = success), (200 if success else 404)



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5150)