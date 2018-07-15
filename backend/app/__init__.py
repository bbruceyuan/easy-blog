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
    app = Flask(
        __name__,
        # template_folder='/home/yuan/Desktop/yuanchaofa/dist',
        # static_folder='/home/yuan/Desktop/yuanchaofa/dist'
        # 在 dist 后面一定不能加上斜杠　/，不然会出问题（感觉这做的有点差啊
        static_folder='../../frontend/dist',
        template_folder='../../frontend/dist'
    )
    # 如果是开发环境，要求跨域
    if config_name == 'develop':
        CORS(app)  # or cors = CORS(app)
    app.config.from_object(config[config_name])

    # init backend config by a static method
    config[config_name].init_app(app)
    db.init_app(app)

    # 蓝图的注册
    from .api import api
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api, url_prefix='/api')
    return app
