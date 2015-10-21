# Python Bottle MVC Sample

pythonのマイクロフレームワークbottleのMVCサンプルです

マンガ何巻まで持ってたっけかな管理ツール

## Pythonバージョン

macに最初から入ってる 2.7

## 必要モジュール

```
# MySQLコネクタ
sudo pip install MySQL-python

# テンプレートエンジン
sudo pip install jinja2

# HTTP サーバ
sudo pip install gunicorn

# プロセス管理ツール
sudo pip install supervisor
```

gunicornで複数workerを立ち上げて、それをsupervisorでプロセス管理する感じ


# ディレクトリ構成

* `/`
    * `app/`
        * `controllers/` ... コントローラー
        * `models/` ... モデル
    * `config/` ... 設定ファイル
    * `libs/` ... ライブラリ
    * `sql/` ... SQLファイル
    * `stat/` ... 静的ファイル
        * `css/` ... CSS
    * `views/` ... HTMLテンプレート
        * `inc/` ... 共通テンプレート
    * `index.py` ... dispatcher


author inkenkun.
