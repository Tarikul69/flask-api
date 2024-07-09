from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

 
#DB Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

 
@app.route('/')
def home():
 cur = mysql.connection.cursor()
 cur.execute("SELECT * FROM users")
 fetchdata = cur.fetchall()
 cur.close()
 data = str(fetchdata)
 return data


if  __name__ == "__main__":
    app.run(debug=True)

 