from flask import Flask, request, jsonify

from psycopg2 import connect

def get_connection():
    connection = connect(
        host="postgres",
        database="postgres",
        user="webuser",
        password="mysecretpassword"
    )
    return connection

app = Flask(__name__)


@app.route('/')
def index():
    # Connect to the Postgres container
    conn = connect(
     port= 5432,
     host= "postgres" ,
     #user="postgres",
     password="mysecretpassword",
    # dbname="postgres"
    )

    # Create the table to store IP addresses
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS ip_addresses (id SERIAL PRIMARY KEY, address VARCHAR(15));")

    # Store the incoming IP address
    with conn.cursor() as cur:
        cur.execute("INSERT INTO ip_addresses (address) VALUES (%s);", (request.remote_addr,))

    
   # cur.execute("SELECT * FROM ip_addresses")
    #rows = cur.fetchall()
    #for row in rows:
     #   print(row)
    conn.commit()
    conn.close()
    return "IP address stored!"
@app.route('/display_table')
def display_table():
    conn = connect(
     port= 5432,
     host= "postgres" ,
     #user="postgres",
     password="mysecretpassword",
    # dbname="postgres"
    )

    # Create the table to store IP addresses
    with conn.cursor() as cur:

        cur.execute("SELECT * FROM ip_addresses")

        rows = cur.fetchall()
        print(rows)

    cur.close()
    conn.close()

    return jsonify(rows)


if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0',port=8080)
