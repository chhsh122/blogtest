# -*- coding: utf-8 -*-
"""
PROJECT: blog_pro
AUTHOR: 摩登老师
TIME: 2020/2/23 21:19
FILE_NAME: manage.py
QQ暖心答疑群: 816572891
bilibili公众号: 猫在大神旁的小C【https://space.bilibili.com/286378257】
"""
from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app

app = create_app()
manager = Manager(app)
manager.add_command("db",MigrateCommand)
if __name__ == "__main__":
    manager.run()