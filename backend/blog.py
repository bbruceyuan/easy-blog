#!/usr/bin/env python
# Created by BBruceyuan on 18-7-9.


from flask_script import Manager
from app import create_app

blog = create_app('develop')

manager = Manager(blog)

# manager.run()

if __name__ == '__main__':
    manager.run()
