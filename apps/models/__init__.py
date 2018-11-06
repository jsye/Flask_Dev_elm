from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 下面是导入 models下面的子文件 模块
from apps.models import user_models

