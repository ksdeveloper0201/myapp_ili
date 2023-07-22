from flask import Flask
from flaskr.database.database import db
from flaskr.routes.world import bp

# ipが異なる場合は、下記にipごとの設定を分け,
# create_appへ渡し、from_objectの引数として使用する。
# config_environment = {
#     "develop": "config.Develop",
#     "local": "config.Local",
# }


def create_app():

    app = Flask(__name__)

    # config.pyを読み込む
    app.config.from_object('config.Config')
    db.init_app(app)
    app.register_blueprint(bp)
    # Blueprintなどappに加えたい設定

    return app
