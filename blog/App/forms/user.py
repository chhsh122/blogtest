# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/24 21:11
FILE_NAME: user.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
from flask_wtf import FlaskForm
# 注册表单类
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class Register(FlaskForm):
    username = StringField('用户名',validators=[DataRequired("用户名不能为空"),Length(min=6,max=12,message='用户名在6-12位之间')],render_kw={'placeholder':'请输入用户名'})
    userpass =  PasswordField('密码',validators=[DataRequired("密码不能为空"),Length(min=6,max=12,message='用户名在6-12位之间')],render_kw={'placeholder':'请输入密码'})
    comfirm = PasswordField('确认密码',validators=[DataRequired("确认密码不能为空"),EqualTo("userpass",message="密码和确认密码不一致")],render_kw={'placeholder':'请输入确认密码'})
    email = StringField('激活邮箱',validators=[DataRequired("邮箱地址不能为空"),Email(message="请输入正确邮箱地址")],render_kw={'placeholder':'请输入确认密码'})
