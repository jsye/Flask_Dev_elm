from flask_script import Manager
from apps import create_app
from apps.models import db
from flask_migrate import Migrate, MigrateCommand

# 管理 app
app = create_app()
manager = Manager(app=app)

# 管理数据库迁移
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    print(app.url_map)
    manager.run()
