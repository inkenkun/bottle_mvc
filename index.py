# -*- coding: utf-8 -*-

import sys
sys.path.append('libs')

from bottle import route, static_file, default_app
from app.controllers import *


# ==========================================
#   静的なパスを追加
# ==========================================
@route('/stat/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./stat/')

## bottle単品で動かしたい場合
#from bottle import run
#run(host='localhost', port=3000)

## gunicornを使う場合
app = default_app()