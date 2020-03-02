# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/23 21:29
FILE_NAME: config.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 配置基础的类
class Config:
    SECRET_KEY = "modeng"
    # 去除控制台自动追踪,然后
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件发送配置
    MAIL_SERVER = "smtp.1000phone.com"
    # 用户名
    MAIL_USERNAME = "zhaojun@1000phone.com"
    # 密码
    MAIL_PASSWORD = "@@@@@@@@@@@@@@"
# 开发环境
class  DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woshishen8@127.0.0.1:3306/modeng_blog'
    DEBUG = True
    TESTING = False

# 测试环境
class  TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woshishen8@127.0.0.1:3306/test_blog'
    DEBUG = True
    TESTING = True

# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:woshishen8@127.0.0.1:3306/pro_blog'
    DEBUG = False
    TESTING = False

# 配置类的字典
configDict = {
    "default":DevelopmentConfig,
    "dev":DevelopmentConfig,
    "test":TestingConfig,
    "production":ProductionConfig,
}
