#!/usr/bin/env python
# Created by BBruceyuan on 18-7-28.


from .. import db


tag_post_relation = db.Table('tag_post_relation',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)
