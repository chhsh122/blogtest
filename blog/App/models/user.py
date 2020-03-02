# User model
from datetime import datetime

from App.extensions import db
from .db_base import DB_Base


class User(db.Model,DB_Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(12),index=True,unique=True )
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.Boolean,default = True)
    age = db.Column(db.Integer,default = 18)  # 年龄
    email = db.Column(db.String(50),unique= True)  #邮箱
    icon = db.Column(db.String(75),default="default")
    lastlogin = db.Column(db.DateTime,default=datetime.utcnow)
    confirm = db.Column(db.Boolean,default=False)
