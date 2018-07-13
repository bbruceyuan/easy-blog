#!/usr/bin/env python
# Created by BBruceyuan on 18-7-5.


from .. import db
from flask import url_for
import datetime


class Post(db.Model):
    """
    post
    """
    __tablename__ = 'posts'

    id = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 加上author,这样就可以根据文章找作者，也可以直接更具作者找文章
    author = db.relationship('User', backref='posts', lazy='dynamic')
    view_count = db.Column(db.Integer, default=0)
    # todo, 这个暂时不加
    # comments = db.relationship('Comment', backref='post', lazy='dynamic')

    @staticmethod
    def from_json(post_json):
        """
        ｔｏｄｏ
        :param post_json: 结构应该包含 {'title': str, 'body': str} 
        :return: 
        """
        pass

    def to_json(self):
        post_json = {
            'url': url_for('api.get_post', id=self.id),
            'title': self.title,
            'body': self.body,
            'body_html': self.body_html,
            'author_url': url_for('api.get_user', id=self.author_id),
            'timestamp': self.timestamp,
            'view_count': self.view_count
        }
        return post_json
