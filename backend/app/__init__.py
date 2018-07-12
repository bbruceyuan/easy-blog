#!/usr/bin/env python
# Created by BBruceyuan on 18-7-5.


from flask import Flask
from config import config

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()


def create_app(config_name):
    """
    based on config_name 创建不同的app
    :param config_name: 
    :return: 
    """
    app = Flask(__name__)
    # 如果是开发环境，要求跨域
    if config_name == 'develop':
        CORS(app)  # or cors = CORS(app)
    app.config.from_object(config[config_name])

    # init backend config by a static method
    config[config_name].init_app(app)
    db.init_app(app)
    return app
