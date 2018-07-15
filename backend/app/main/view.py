#!/usr/bin/env python
# Created by BBruceyuan on 18-7-15.


from . import main
from flask import jsonify, render_template, redirect, request, abort, session
from ..api.authentication import auth
from ..model import User
from .. import db


# 把路由交给前端管理
@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@main.route('/login', method=['POST'])
@auth.login_required
def login():
    data = request.get_json()
    if data.get('remember'):
        # todo, 需要考虑在logout的时候怎么处理 session. 貌似这个session和token一样，可以有时间限制
        session['username'] = data.get('username')
    return redirect('api.get_token')


@main.route('/register', method=['POST'])
def register():
    data = request.get_json()
    # print(data)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        print('missing arguments')
        abort(400)
    if User.query.filter_by(username=username).first():
        print(User.query.filter_by(username=username).first())
        print('username exists')
        abort(400)
    user = User()
    user.username = data.get('username')
    user.password = data.get('password')
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username})


@main.errorhandler(404)
def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 404
    return response
