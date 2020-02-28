# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/23 21:56
FILE_NAME: user.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
from flask import Blueprint, render_template

from App.forms import Register

user = Blueprint("user",__name__)
# 注册步骤
"""
1. 创建模型类
2. 加载flask-migrate扩展库(迁移)
3. 在试图中导入模型类(便于存储)
4. 验证(用户名、密码)是否存在
5. 获取并存储模板前台传递过来的数据
6. 明文转换成密文(加密存储)
7. 配置发送邮件扩展库和功能
8. 发送邮件
9. 消息闪现(注册成功, 前去激活)
"""
@user.route('/register/',methods=['GET','POST'])
def register():

    form = Register()
    return render_template('user/register.html',form=form)

