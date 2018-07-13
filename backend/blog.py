#!/usr/bin/env python
# Created by BBruceyuan on 18-7-9.


from flask_script import Manager
from flask import current_app
from app import create_app

blog = create_app('develop')

manager = Manager(blog)
# with blog.app_context():
#     print(current_app.config['SECRET_KEY'])
# manager.run()

if __name__ == '__main__':
    manager.run()
