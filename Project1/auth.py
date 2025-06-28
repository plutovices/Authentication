
from flask import Flask, render_template, url_for,request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from werkzeug.security import generate_password_hash  
import os
import bcrypt


auth = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
auth.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
# auth.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
auth.config['SECRET_KEY'] = 'thesecretkey'

db = SQLAlchemy(auth)

class User(db.Model, UserMixin):
    
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(35), nullable=False, unique=True)
       email = db.Column(db.String(70), nullable=False, unique=True)
       password = db.Column(db.String(80), nullable=False)
       department = db.Column(db.String(50), nullable=False, unique=False)
       faculty = db.Column(db.String(10), nullable=False, unique=False)


@auth.route("/login")
def login():
    return render_template('loginpage.html')

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
         username = request.form['username']
         email = request.form['email']
         faculty = request.form['faculty']
         department = request.form['department']
         password = request.form['password']

         salt = bcrypt.gensalt(rounds=12)
         hashed_pass = bcrypt.hashpw(password=password.encode("utf-8"), salt=salt)


         def validate_form():
           existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
           if existing_user:
               flash("Try logging in this user already exists", "danger")

         new_user = User(
              username=username, 
              email=email, 
              password= hashed_pass, 
              faculty=faculty,
              department=department,
            )
         
         

         db.session.add(new_user)
         db.session.commit()
         
         flash("You've been registered successfully!", "success")
         return  redirect(url_for('login'))

    return render_template('register.html')

if __name__ == "__main__":
    with auth.app_context():
        db.create_all()
        print("Database is created!!!")
    auth.run(debug=True)

    #AJAX js real-time username validation
    #Database migration (Flask migrate)