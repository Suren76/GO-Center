from flask_sqlalchemy import SQLAlchemy, Model
# from app import db


db: SQLAlchemy = SQLAlchemy()

model: Model = db.Model


class User(model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    full_name = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50))
    birthday = db.Column(db.DateTime)
    address = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    phone_number = db.Column(db.String(50), unique=True)
    status = db.Column(db.String(50))

    def __repr__(self):
        return f"<User {self.id}>"


class Profile(model):
    # id = db.Column(db.Integer, primary_key=True)

    userId = db.Column(db.Integer, db.ForeignKey("User.id"), primary_key=True)
    avatar = db.Column(db.LargeBinary)
    description = db.Column(db.String)
    englishLevel = db.Column(db.String)
    groups = db.Column(db.String)

    def __repr__(self):
        return f"<Profile {self.userId}>"

