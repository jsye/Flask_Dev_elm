from apps.models import db


# 用户表
class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    pwd = db.Column(db.String(32))

    def __str__(self):
        return self.name


