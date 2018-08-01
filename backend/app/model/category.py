#!/usr/bin/env python
# Created by BBruceyuan on 18-7-31.


from .. import db


class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(64), unique=True)


class CategoryUtil:

    def __init__(self):
        self.categories = []

    def add_categories(self, categories):
        for category in categories:
            self.categories.append(self.__add_category(category))
        return self.categories

    def __add_category(self, category):
        return  Category.query.filter_by(
            category_name=category).first() or Category(category_name=category)
