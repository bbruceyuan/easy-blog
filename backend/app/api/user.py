#!/usr/bin/env python
# Created by BBruceyuan on 18-7-12.

from flask import jsonify, request, url_for, current_app
from ..model import User, Post
from . import api
from .. import db


@api.route('/users/<uid>', methods=['GET', 'DELETE'])
def get_user(uid):
    uu = UserUtils(uid)
    if request.method == 'GET':
        return uu.get_user()
    elif request.method == 'DELETE':
        return uu.del_user()


@api.route('/users/<uid>/posts/')
def get_user_posts(uid):
    user = User.query.get_or_404(uid)
    page = request.args.get('page', 1, type=int)
    # 时间递减
    pagination = user.posts.order_by(
        Post.timestamp.desc()
    ).paginate(
        page,
        per_page=current_app.config['FLASK_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    # 前面是否有请求过pagination, (previous)
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_posts', id=uid, page=page - 1)
    # 因为next是关键字，所以这里使用next_代替
    next_ = None
    if pagination.has_next:
        next_ = url_for('api.get_user_posts', id=uid, page=page + 1)
    return jsonify(
        {
            'posts': [post.to_json() for post in posts],
            'prev': prev,
            'next': next_,
            'count': pagination.total
        }
    )


# @api.route('/user/<int:id>/timeline/')


class UserUtils:
    """
    CRUD HTTP 对应http操作
    Create POST 　（这个是register
    Read GET 
    Update PUT 
    Delete DELETE 
    """
    def __init__(self, user_id):
        self.uid = user_id
        self.user = User.query.get_or_404(self.uid)

    def get_user(self):
        return jsonify(self.user.to_json())

    def del_user(self):
        username = self.user.username
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.commit()
        response = {"username": username, 'type': 'delete', 'error_code': 0}
        return jsonify(response)
