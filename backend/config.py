#!/usr/bin/env python
# Created by BBruceyuan on 18-7-9.


import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # flask config
    SECRET_KEY = os.getenv('SECRET_KEY', 'please set a secret string')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        """
        初始化函数
        :param app: 
        :return: 
        """
        pass


class ProductConfig(Config):
    pass


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    pass


config = {
    'product': ProductConfig,
    'develop': DevelopConfig,

    'default': DevelopConfig
}