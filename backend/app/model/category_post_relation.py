#!/usr/bin/env python
# Created by BBruceyuan on 18-7-31.


from .. import db


category_post_relation = db.Table('category_post_relation',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)
