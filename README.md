# easy_blog
============

一个简单的博客。我想这应该挺适合新手练手的。

使用的Python的flask框架以及Vue，组件库用的是iview3.0。前端是单页面应用(SPA)，主要是想学习一下前后端分离的思想。

## 特点

- 简洁
- 学习向

## 技术栈

- flask
- vue
- vue-router
- vuex
- iview3.0
- python
- spa(因为我以前觉得这个东西挺难的，所以写一哈)
- 后端token认证

## 用法

```
cd backend
pip install -r requirements.txt
python blog.py runserver
```
**值得注意**

我们在`python blog.py runserver`之前,应该先使用`python blog.py shell`

然后在shell里面运行`db.create_all()`.或者使用flask-migrate的命令也行。

```
cd frontend
npm intall
npm run serve
```

## todo
### 后端
- []增加评论功能
- []禁止主用户之外的user发文章
- []权限系统最好跟新一下
- []写测试
### 前端
- []timeline组件抽象一下
- []加上评论树部分
