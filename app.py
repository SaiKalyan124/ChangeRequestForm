from sqlite3 import Date
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password%40124#@localhost/crud1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    projectId = db.Column(db.String(255), primary_key=True)
    requestorName = db.Column(db.String(255))
    typeOfRequest = db.Column(db.String(255))
    targetDate = db.Column(db.String(255))
    description = db.Column(db.String(255))
    reason = db.Column(db.String(255))

    def __init__(self, projectId, requestorName, typeOfRequest, targetDate, description, reason) -> None:
        self.projectId = projectId
        self.requestorName = requestorName
        self.typeOfRequest = typeOfRequest
        self.targetDate = targetDate
        self.description = description
        self.reason = reason


@app.route('/')
def Index():
    all_data=Data.query.all()
    return render_template("Index.html",requestForms=all_data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        projectId = request.form['projectId']
        requestorName = request.form['requestorName']
        typeOfRequest = request.form['typeOfRequest']
        targetDate = request.form['targetDate']
        description = request.form['description']
        reason = request.form['reason']

        my_data = Data(projectId, requestorName, typeOfRequest, targetDate, description, reason)
        db.session.add(my_data)
        db.session.commit()

        flash("New request has been submitted")

        return redirect(url_for('Index'))

@app.route('/update', methods=['GET','POST'])

def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('projectId'))
        my_data.requestorName = request.form['requestorName']
        my_data.typeOfRequest = request.form['typeOfRequest']
        my_data.targetDate = request.form['targetDate']
        my_data.description = request.form['description']
        my_data.reason = request.form['reason']

        db.session.commit()
        flash("Form Updated")

        return redirect(url_for('Index'))

@app.route('/delete/<projectId>/', methods=['GET','POST'])
def delete(projectId):
    my_data = Data.query.get(projectId)
    db.session.delete(my_data)
    db.session.commit()
    flash("Record Deleted")


    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)