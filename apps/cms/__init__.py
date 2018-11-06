from flask import Blueprint

#注册成为蓝图
cms_bp = Blueprint('cms', __name__)

# 导入cms下的视图
from apps.cms import index_views
from apps.cms import user_views


