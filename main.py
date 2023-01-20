# -*- coding: utf8 -*-
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import json #подключили библиотеку для работы с json
from pprint import pprint
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/usersinformation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



hasentered = False


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(28), nullable=False, unique=True)
    password = db.Column(db.String(28), nullable=False)


@app.route('/', methods=['POST', 'GET'])
def registration():
    global hasentered
    hasentered = False
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        for curUser in User.query.all():
            if curUser.login == login and curUser.password == password:

                hasentered = True
                return redirect("/home")
        return "Неверное имя пользователя или пароль!"
    else:
        return render_template("registration.html")


@app.route('/home')
def home():
    if hasentered:
        return render_template("homepage.html")
    else:
        return redirect('/')



@app.route('/parser')
def parser():
    if hasentered:
        with open('5_result.json') as f:  # открыли файл с данными
            text = json.load(f)  # загнали все, что получилось в переменную

        return render_template("index.html", text=text)
    else:
        return redirect('/')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        password2 = request.form['password2']
        for curUser in User.query.all():
            if curUser.login == login:
                return "Такой пользователь уже существует!"
        if(password == password2):
            newUser = User(login=login, password=password)
        else:
            return "Пароли не совпадают!"
        try:
            db.session.add(newUser)
            db.session.commit()
            return redirect('/')
        except:
            return "ERROR 404"

    else:
        return render_template("SignUp.html")


if __name__ == "__main__":
    app.run(debug=True)