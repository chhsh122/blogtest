# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/23 21:55
FILE_NAME: main.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
from flask import Blueprint, render_template

# 蓝本
main = Blueprint('main',__name__)

# 首页视图
@main.route('/')
@main.route('/index/')
def index():
    return render_template('main/index.html')
