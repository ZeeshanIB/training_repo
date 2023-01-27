from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)


@app.route('/create_table', methods=['POST'])
def create_table():
    age = request.form.get('age')
    conn = connect(dbname='your_db_name', user='your_db_user',
                   password='your_db_password', host='172.26.0.3')
    cur = conn.cursor()
    cur.execute("CREATE TABLE ages (age INTEGER)")
    cur.execute(f"INSERT INTO ages (age) VALUES ({age})")
    conn.commit()
    cur.execute("SELECT * FROM ages")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return str(rows)


if __name__ == '__main__':
    app.run(debug=True)
