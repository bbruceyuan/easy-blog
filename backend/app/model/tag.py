#!/usr/bin/env python
# Created by BBruceyuan on 18-7-28.


from .. import db


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(64), unique=True)


class TagUtil:

    def __init__(self):
        self.tags = []

    def add_tags(self, tags):
        for tag in tags:
            self.tags.append(self.__add_tag(tag))
        return self.tags

    def __add_tag(self, tag):
        return  Tag.query.filter_by(tag_name=tag).first() or Tag(tag_name=tag)
