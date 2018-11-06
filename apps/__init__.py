from flask import Flask


# 管理数据库模块
def regster_db(app):
    from apps.models import db
    db.init_app(app)


#管理蓝图模块
def register_bp(app):
    from apps.apis import apis_bp
    from apps.cms import cms_bp

    # 注册蓝图模块
    app.register_blueprint(apis_bp, url_prefix='/apis') # url_prefix 为蓝图的路径
    app.register_blueprint(cms_bp, url_prefix='/cms')


# 使用函数统一管理
def create_app():
    app = Flask(__name__)

    # 在使用session时，要配置SECRET_KEY ，
    app.config['SECRET_KEY'] = '232242'
    # 配置数据库
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@127.0.0.1:3306/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 注册蓝图模块
    register_bp(app)

    # 注册数据库
    regster_db(app)

    return app