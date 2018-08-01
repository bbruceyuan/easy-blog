#!/usr/bin/env python
# Created by BBruceyuan on 18-8-1.


from flask import jsonify, g
from . import api
from ..model import User


@api.route('/tags')
def get_tags():
    """
    在这里希望根据用户来获取，和用户有关的tag
    所以我们需要做的是，获取用户所有的post,然后找到所有的tag
    :return: 
    """
    result_tags = []

    # 找到某个用户的所有的文章，把所有文章的Tag都放在一块
    def append_tag(user_posts):
        tmp = []
        for post in user_posts:
            for tag in post.tags.all():
                tmp.append(tag.tag_name)
        return tmp
    # 如果当前用户存在，就是用当前用户
    if g.get('current_user', None):
        user_posts_ = g.current_user.posts.all()
        result_tags.extend(append_tag(user_posts_))
    # 如果不存在，就是用默认用户
    else:
        user = User.query.get(1)
        result_tags.extend(append_tag(user.posts.all()))
    result_tags = list(set(result_tags))
    return jsonify(result_tags)

