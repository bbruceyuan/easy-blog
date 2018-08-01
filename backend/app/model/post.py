#!/usr/bin/env python
# Created by BBruceyuan on 18-7-5.


from .. import db
from flask import url_for
import datetime
from ..exceptions import ValidationError
from markdown import markdown
import bleach


class Post(db.Model):
    """
    post
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 加上author,这样就可以根据文章找作者，也可以直接更具作者找文章, 因为不能一对多，所以改成在User上加关系
    # author = db.relationship('User', backref='posts'，lazy='dynamic')
    view_count = db.Column(db.Integer, default=0)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    tags = db.relationship('Tag', backref='posts',
                           secondary='tag_post_relation', lazy='dynamic')
    categories = db.relationship(
        'Category',
        backref='posts',
        secondary='category_post_relation',
        lazy='dynamic'
    )

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b',
                        'blockquote', 'code', 'em', 'i',
                        'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(
            bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    @staticmethod
    def from_json(post_json):
        """
        ｔｏｄｏ
        :param post_json: 结构应该包含 {'title': str, 'body': str} 
        :return: 
        """
        title = post_json.get('title')
        body = post_json.get('body') or post_json.get('content')
        if body is None or body == '' or title is None or title == '':
            raise ValidationError('post does not have a body')
        return Post(title=title, body=body)

    def to_json(self):
        post_json = {
            # 这里之所以不用 api.get_post是因为 api需要登入才能看，而我们希望每个人都能看。
            # 反正是个人博客
            'url': url_for('api.get_post', pid=self.id),
            # 'url': url_for('main.get_post', pid=self.id),
            'title': self.title,
            'body': self.body,
            'body_html': self.body_html,
            'author_url': url_for('api.get_user', uid=self.author_id),
            'timestamp': str(self.timestamp),
            'comments_url': url_for('api.get_post_comments', id=self.id),
            'view_count': self.view_count,
            'comment_count': self.comments.count(),
            'tags': [tag.tag_name for tag in self.tags],
            'categories': [category.category_name for category in self.categories]
        }
        return post_json

db.event.listen(Post.body, 'set', Post.on_changed_body)
