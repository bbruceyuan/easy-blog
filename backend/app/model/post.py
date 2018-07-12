#!/usr/bin/env python
# Created by BBruceyuan on 18-7-5.


from .. import db
import datetime


class Post(db.Model):
    """
    post
    """
    __tablename__ = 'posts'

    id = db.Column(db.String(64), primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 加上author,这样就可以根据文章找作者，也可以直接更具作者找文章
    author = db.relationship('User', backref='posts', lazy='dynamic')
    # todo, 这个暂时不加
    # comments = db.relationship('Comment', backref='post', lazy='dynamic')
