# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/23 21:22
FILE_NAME: __init__.py.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
from flask import Flask

from App.config import configDict
from App.extensions import init_app
from App.views import register_blueprint


def create_app(configName = "default"):
    app = Flask(__name__)
    # 加载配置文件内容
    app.config.from_object(configDict[configName])
    # 注册蓝本
    register_blueprint(app)
    # 初始化扩展库
    init_app(app)
    return app