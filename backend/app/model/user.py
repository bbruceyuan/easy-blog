#!/usr/bin/env python
# Created by BBruceyuan on 18-7-5.


from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
# from ...config import Config　　　# 这样会导致循环引用，虽然我不知道是什么鬼，但是这个问题好难
# 以后要用config的地方，一定要使用current_app了, 而且要用字典的方式获取
from flask import current_app


class User(db.Model):
    """
    User类
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64))
    # 虽然已经在post类中加了反向引用，但是因为lazy设置为dynamic不能是多对一/一对一。所以这里需要在User上加上关系
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        检查密码的hash值是否相同
        :param password: string
        :return: bool
        """
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=600):
        """
        获取token,
        :param expiration: 有效时间, int, 默认十分钟 
        :return: token, 这是一个byte值, 所以后面需要decode
        """
        # config类似于字典的获取方式
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        # 这里一定要转为Str，不然不能dumps
        return s.dumps({'id': str(self.id)})

    @staticmethod
    def verify_auth_token(token):
        """
        解析token，确认登录的用户身份
        :param token: token
        :return: user 
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            print('the token is expired')
            return None  # valid token, but not expired
        except BadSignature:
            print('token is not valid')
            return None
        user = User.query.get(id=data.get('id'))
        if user is None:
            return False
        return User

    def to_json(self):
        # todo, add more info
        user_json = {'username': self.username, 'post_count': self.posts.count()}
        return user_json

    def __repr__(self):
        return '<User of {}>'.format(self.username)

    def __str__(self):
        return '<User Model>'
