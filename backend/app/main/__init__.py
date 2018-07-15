#!/usr/bin/env python
# Created by BBruceyuan on 18-7-15.


from flask import Blueprint

# 注册蓝图
main = Blueprint('main', __name__)


from . import view
