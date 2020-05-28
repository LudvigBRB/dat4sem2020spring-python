from flask import Flask, jsonify, abort, request
import datetime
import mysql.connector

app = Flask(__name__)

animals = [
    {
        'id': 1,
        'species': u'Monitor lizard',
        'description': u'Fast, active, arboreal, swim', 
        'diet' : u'meat, fruit',
        'extinct': False
    },
    {
        'id': 2,
        'species': u'Dunkleosteus',
        'description': u'Armored, jawed fish', 
        'diet' : u'meat',
        'extinct': True
    },
    {
        'id':3,
        'species': u'mesonyx',
        'description' : u'hooved, carnivore, mammal',
        'diet' : u'meat',
        'extinct':True
    }
]

@app.route('/')
def index():
    return "List af links: "

@app.route('/underdeling1')
def beneath1():
    return "dette er et link under"

@app.route('/underdeling2')
def beneath2():
    return "et andet under"

@app.route('/animals/all', methods=['GET'])
def allSpecies():
    return jsonify({'animals' : animals})

@app.route('/animals/<int:animal_id>', methods=['GET'])
def specificSpecies(animal_id):
    animal = [animal for animal in animals if animal['id'] == animal_id]
    if len(animal) == 0:
        abort(404)
    return jsonify({'animal': animal[0]})

@app.route('/sql')
def sql():
    cnx = mysql.connector.connect(user='dev', password='ax2',
                              host='127.0.0.1',
                              port='3307',
                              database='Relationship', #kan fkernes hvis database specifeceres i query
                              use_pure=True)
    cursor = cnx.cursor()
    query = ('SELECT * FROM ADDRESS WHERE ID BETWEEN %s AND %s')
    cursor.execute(query, (3, 6))

    data = ""

    for e in cursor:
        data = data + str(e[0]) + ' ' + e[1] + ' ' + e[2] + ' ' + str(e[3]) + '\n'
    
    cursor.close()
    cnx.close()

    return data

@app.route('/sql/<int:number>')
def idsql(number):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                              host='127.0.0.1',
                              port='3307',
                              database='Relationship', #kan fkernes hvis database specifeceres i query
                              use_pure=True)
    cursor = cnx.cursor()
    query = ('SELECT * FROM ADDRESS WHERE ID = %s')
    cursor.execute(query, (number,))

    data = ""

    for e in cursor:
        data = data + str(e[0]) + ' ' + e[1] + ' ' + e[2] + ' ' + str(e[3]) + '\n'

    cursor.close()
    cnx.close()

    return data

@app.route('/sql/<string:city>')
def citysql(city):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                              host='127.0.0.1',
                              port='3307',
                              database='Relationship', #kan fkernes hvis database specifeceres i query
                              use_pure=True)
    cursor = cnx.cursor()
    query = ('SELECT * FROM ADDRESS WHERE CITY = %s')
    cursor.execute(query, (city,))

    data = ""

    for e in cursor:
        data = data + str(e[0]) + ' ' + e[2] + ' ' + str(e[3]) + '              ' #'\n\n\n'

    cursor.close()
    cnx.close()

    return data


if __name__ == '__main__':
    app.run(debug=True)