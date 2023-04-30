from flask import Flask
import mysql.connector

app = Flask(__name__)


# "localhost:5000/hello" page
@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/data')
def data():
    return 'cur.execute("SELECT * FROM users")'
    return 'Hello, World!'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Penguin12'
app.config['MYSQL_DB'] = 'weather'

conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)


# Run the Flask app by adding the following code at the end of your Python file:
if __name__ == '__main__':
    app.run()
