# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/23 21:30
FILE_NAME: extensions.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy() # ORM扩展库
migrate = Migrate() # 模型迁移
mail = Mail() # 邮件发送


def init_app(app):
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app,db=db)
    mail.init_app(app)