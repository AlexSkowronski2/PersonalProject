from flask import Flask, current_app, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)

def database_connection(database_name, user_name, host_name):
    conn = psycopg2.connect(f"dbname={database_name} user={user_name} host={host_name}")
    return conn

#really should change name of database to personal_project
conn = database_connection('wlodarczyk', 'wlodarczyk', 'localhost')

def execute_sql_query(query):
    if conn != None:
        with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as curs:
            curs.execute(query)
            returned_data = curs.fetchall()
            return returned_data

@app.route("/", methods=["GET"])
def index():
    return current_app.send_static_file("index.html")

# prints the results of main table in its raw form, want to add stuff like muscle names not ids
@app.route("/exercises", methods=["GET"])
def exercises():
    query = "SELECT * FROM exercises;"
    response = execute_sql_query(query)
    return jsonify(exercises = response)

@app.route("/movements", methods=["GET"])
def movements():
    query = "SELECT * FROM movementpattern;"
    response = execute_sql_query(query)
    return jsonify(exercises = response)

@app.route("/equipment", methods=["GET"])
def equipment():
    query = "SELECT * FROM equipment;"
    response = execute_sql_query(query)
    return jsonify(exercises = response)

@app.route("/muscles", methods=["GET"])
def muscles():
    query = "SELECT * FROM muscles;"
    response = execute_sql_query(query)
    return jsonify(exercises = response)