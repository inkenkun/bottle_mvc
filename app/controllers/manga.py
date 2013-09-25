# -*- coding:utf-8 -*-

import sys
sys.path.append('libs')

from bottle import route, post, request, redirect, jinja2_template as template

import app.models.manga
model = app.models.manga.Manga()


#一覧ページ
@route('/')
@route('/<page:int>')
def index(page=1):
    result = model.load(page)
    return template('index', result = result)


#新規登録ページ
@route('/new')
def new():
    return template('new')


#編集ページ
@route('/edit/<id:int>')
def edit(id):
    return template('edit', i = model.edit(id))


#post送信先
@post('/done')
def done():
    post_data = {}
    post_data["name"] = request.forms.get('name')
    post_data["kana"] = request.forms.get('kana')
    post_data["num"] = request.forms.get('num')
    post_data["id"] = request.forms.get('id')
    post_data["del"] = request.forms.get('del')

    model.done(post_data)

    redirect("/")
