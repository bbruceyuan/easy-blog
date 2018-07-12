#!/usr/bin/env python
# Created by BBruceyuan on 18-7-12.

from .. import db
from . import api
from ..model import Post
from flask import current_app, request, url_for, jsonify


@api.route('/posts/')
def get_posts():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page - 1)
    next_ = None
    if pagination.has_next:
        next_ = url_for('api.get_posts', page=page + 1)
    return jsonify(
        {
            'posts': [post.to_json() for post in posts],
            'prev': prev,
            'next': next_,
            'count': pagination.total
        })
