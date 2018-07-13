#!/usr/bin/env python
# Created by BBruceyuan on 18-7-11.


from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..model import User
from . import api
from .errors import unauthorized


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    """
    这获取的是头部中auth中的值
    :param username_or_token: 
    :param password: 
    :return: 
    """
    if username_or_token == '':
        return False
    if password == '':
        # 使用token进行验证
        # 这时候说明是一个token,　而不是username
        # 看User的实现可以知道，我们返回的是一个user
        g.current_user = User.verify_auth_token(username_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.get(username=username_or_token)
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return g.current_user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


# todo, 好好研究一下这个怎么放比较好
# 这个before_request仅仅对api下的路由生效
# @api.before_request
# @auth.login_required
# def before_request():
#     """
#     这么做的作用就是让api下所有的路由都需要auth.login_required
#     :return:
#     """
#     pass


@api.route('/token')
def get_token():
    # 因为g.current_user.generate_auth.token是一个byte值，所以需要decode
    data = {
        'token': g.current_user.generate_auth_token(expiration=3600).decode('utf-8'),
        'expiration': 3600
    }
    return jsonify(data)
