#!/usr/bin/env python
# Created by BBruceyuan on 18-7-9.


from flask_script import Manager
from flask_script import Shell
from flask_migrate import Migrate, MigrateCommand
from flask import current_app
from app import create_app
from app import db


blog = create_app('develop')

manager = Manager(blog)
# with blog.app_context():
#     print(current_app.config['SECRET_KEY'])
# manager.run()

migrate = Migrate(blog, db)


def make_shell_context():
    return dict(app=blog, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
