#!/usr/bin/env python
# Created by BBruceyuan on 18-7-11.


from flask import Blueprint

api = Blueprint('api', __name__)

from . import user, errors, authentication
