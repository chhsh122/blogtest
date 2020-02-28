# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/23 21:29
FILE_NAME: __init__.py.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
from .main import main
from .user import user

blueprint_config = [
    (main,''),
    (user,'')
]

def register_blueprint(app):
    for blueprint,prefix in blueprint_config:
        app.register_blueprint(blueprint,url_prefix=prefix)
