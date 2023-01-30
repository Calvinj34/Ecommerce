from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from secrets import token_hex
from werkzeug.security import generate_password_hash
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    caption = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __init__(self, product_id, product_name, img_url, caption, user_id):
        self.product_id = product_id
        self.product_name =product_name
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
        'product_id': self.product_id,
        'product_name': self.product_name,
        'img_url': self.img_url,
        'caption': self.caption,
        'user_id': self.user_id,
        'author': self.author.username,
         }



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), db.ForeignKey('user.username'))
    product_id = db.Column(db.String, db.ForeignKey('product.product_id'))


    def __init__(self, username, product_id):
        self.username = username
        self.product_id = product_id
        

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
        
    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()