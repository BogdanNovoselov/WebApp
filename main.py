from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/usersinformation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(28), nullable=False, unique=True)
    password = db.Column(db.String(28), nullable=False)


@app.route('/')
def registration():
    return render_template("registration.html")

@app.route('/home')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)