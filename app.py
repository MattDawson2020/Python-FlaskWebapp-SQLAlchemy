from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy # remember to point source towards virtualenv otherwise this wont be imported
from send_email import send_email
from sqlalchemy.sql import func

from dotenv import load_dotenv
load_dotenv()
import os
password = os.environ.get("db_pass")

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:%s@localhost/height_collector' % password
db=SQLAlchemy(app)
class Data(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height=db.Column(db.Integer)

    def __init__(self, email, height):
        self.email=email
        self.height=height

@app.route('/')
#implicitly declares get
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form['height_name']
        if db.session.query(Data).filter(Data.email==email).count() == 0:
            data=Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height)).scalar()
            average_height=round(average_height)
            count=db.session.query(Data.height).count()
            send_email(email, height, average_height, count)
            return render_template('success.html')
    return render_template('index.html', text='That email address has already submitted data to us')


if __name__ == '__main__': #checks that the app is running and not being IMPORTED
    app.debug=True
    app.run()


