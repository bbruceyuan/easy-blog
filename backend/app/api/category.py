#!/usr/bin/env python
# Created by BBruceyuan on 18-8-1.


from flask import jsonify, g
from . import api
from ..model import User


@api.route('/categories')
def get_categories():
    """
    和get_tag的思路是一样的
    :return: 
    """
    result_categories = []

    # 找到某个用户的所有的文章，把所有文章的Tag都放在一块
    def append_category(user_posts):
        tmp = []
        for post in user_posts:
            for category in post.categories.all():
                tmp.append(category.category_name)
        return tmp
    # 如果当前用户存在，就是用当前用户
    if g.get('current_user', None):
        user_posts_ = g.current_user.posts.all()
        result_categories.extend(append_category(user_posts_))
    # 如果不存在，就是用默认用户
    else:
        user = User.query.get(1)
        result_categories.extend(append_category(user.posts.all()))
    # 直接用最蠢的方法来去重，因为不同的文章可能有相同的类别
    result_categories = list(set(result_categories))
    return jsonify(result_categories)
