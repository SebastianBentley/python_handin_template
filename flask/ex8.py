#!flask/bin/python
from flask import Flask, jsonify, abort, request
import mysql.connector as mysql
app = Flask(__name__)

## connecting to the database using 'connect()' method
db = mysql.connect(
    # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
    host = "db",
    user = "root",
    passwd = "root",
    db = "db"
    #,charset='latin1'
    #,collation='latin1_danish_ci'
)


@app.route('/api/laptops/all')
def gen_people():  
    cur = db.cursor()
    query = 'select * from laptops'
    cur.execute(query)
    all_laptops = cur.fetchall()
    cur.close()
    results = []
    for idx,val in enumerate(all_laptops):
        results.append({"id": val[0], "name": val[1], "price":val[2]})
    return jsonify(results)

@app.route('/api/laptops', methods=['POST'])
def create_laptop():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        abort(400)
    name = request.json['name']
    price = request.json['price']
    laptop = {
        'name': request.json['name'],
        'price': request.json['price'],
    }
    cur = db.cursor()
    insert_query = """INSERT INTO laptops (name, price) VALUES (%s, %s)"""
    val = (name, price,)
    cur.execute(insert_query, val) 
    db.commit()
    cur.close()
    return jsonify(laptop), 201
