from flask import Blueprint, request, render_template, redirect, url_for, flash
from appdummy import app
from flask_mysqldb import MySQL
# from dotenv import load_dotenv
import os

 # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password@124#'
app.config['MYSQL_HOST'] = '127.0.0.1' # localhost
app.config['MYSQL_DB'] = 'crud1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# MySQL Connection
mysql = MySQL(app)
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/insert', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"


    if request.method == 'POST':
        projectName = request.form['projectId']
        requestorName = request.form['requestorName']
        typeOfRequest = request.form['typeOfRequest']
        targetDate = request.form['targetDate']
        description = request.form['description']
        reason = request.form['reason']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO table5 VALUES(%s,%s,%s,%s,%s,%s)''',
                       (projectName, requestorName, typeOfRequest, targetDate, description, reason))
        mysql.connector.commit()
        cursor.close()
        return f"Done!!"


app.run(host='localhost', port=5000)


if __name__ == "__main__":
    app.run(debug=True)
