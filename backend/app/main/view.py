#!/usr/bin/env python
# Created by BBruceyuan on 18-7-15.


from . import main
from flask import jsonify, render_template, redirect, request, abort, session, url_for, current_app
from ..api.authentication import auth
from ..model import User, Post
from .. import db


# 把路由交给前端管理
@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@main.route('/login', methods=['POST'])
@auth.login_required
def login():
    # 是先验证完装饰器之后才能执行函数
    data = request.get_json()
    if data.get('remember'):
        # todo, 需要考虑在logout的时候怎么处理 session. 貌似这个session和token一样，可以有时间限制
        session['username'] = data.get('username')
    return redirect(url_for('api.get_token'))


@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # print(data)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if username is None or password is None:
        print('missing arguments')
        abort(400)
    if User.query.filter_by(username=username).first():
        print(User.query.filter_by(username=username).first())
        print('username exists')
        abort(400)
    if User.query.filter_by(email=email).first():
        print('email had been used')
        abort(400)
    user = User()
    user.username = username
    user.password = password
    user.email = email
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username})


@main.route('/posts')
def get_posts():
    page = request.args.get('page', 1, type=int)
    # 先根据时间拍一下顺序
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page,
        per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('main.get_posts', page=page - 1)
    next_ = None
    if pagination.has_next:
        next_ = url_for('main.get_posts', page=page + 1)
    return jsonify(
        {
            # posts 里面的 post json中就有一项是url
            # 具体的格式如下
            """
                post_json = { # 注释见Post
                    'url': url_for('main.get_post', id=self.id),
                    'title': self.title,
                    'body': self.body,
                    'body_html': self.body_html,
                    'author_url': url_for('api.get_user', id=self.author_id),
                    'timestamp': self.timestamp,
                    'view_count': self.view_count
                    }
            """
            'posts': [post.to_json() for post in posts],
            'prev': prev,
            'next': next_,
            'count': pagination.total
        })


@main.route('/post/<int:pid>')
def get_post(pid):
    post = Post.query.get_or_404(pid)
    return jsonify(post.to_json())


@main.errorhandler(404)
def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 404
    return response
