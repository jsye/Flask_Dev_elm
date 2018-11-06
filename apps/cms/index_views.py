from flask import render_template


# 导入蓝图接管路由
from apps.cms import cms_bp


# 主页
@cms_bp.route('/', endpoint='index')
@cms_bp.route('/index', endpoint='index')
def index_view():
    return render_template('index.html')




# 添加页
@cms_bp.route('/add', endpoint='add', methods=['GET', 'POST'])
def add_view():
    return render_template('add.html')



# /detail
@cms_bp.route('/detail', endpoint='detail')
def detail_view():
    return render_template('detail.html')


