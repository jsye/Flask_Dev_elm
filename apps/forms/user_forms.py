from sqlalchemy import and_
from wtforms import *
from wtforms.validators import *

# 用户模块
from apps.models import db
from apps.models.user_models import UserModel



# 登录表单验证
class LoginForm(Form):
    name = StringField(label='帐号', validators=[validators.DataRequired(message='不能为空'),
                                   validators.Length(min=3, message='帐号至少3个字符'),
                                   validators.Length(max=10, message='帐号不能大于10个字符')]
                                   ,render_kw={'class': 'form-control', 'placeholder': '请输入帐号'})

    pwd = PasswordField(label='密码', validators=[validators.DataRequired(message='不能为空'),
                                  validators.Length(min=6, message='不能少6位'),
                                  validators.Length(max=128, message='不能大于128位')]
                                , render_kw={'class': 'form-control', 'placeholder': '请输入密码'})
    """

    # 自定义表单验证 用户名 （登录）
    def validate_name(self, obj):      # 注 名字要与上面要验证字段相同
        name = obj.data
        pwd = self.pwd.data
        res = db.session.query(UserModel).filter(and_(UserModel.name == name, UserModel.pwd == pwd)).first()   # 到数据库中查询数据
        print(res)
        if res is None:
            raise validators.ValidationError('帐号或密码错误！')

"""
"""
    # 自定义表单验证 密码
    def validate_pwd(self, obj):
        pwd = obj.data
        res = res = db.session.query(UserModel).filter(UserModel.name == pwd).first()  # 到数据库中查询数据
        if res:
            return pwd
        else:
            raise validators.ValidationError('帐号或密码错误！')

"""




# 注册表单验证
class RegisterForm(LoginForm):
    """
    name = StringField(label='用户名', validators=[validators.DataRequired(message='用户名 不能为空'),
                                   validators.Length(min=3, message='用户名不能少于3个字符'),
                                   validators.Length(max=10, message='用户名不能大于10个字符')
                                ],render_kw={'class': 'form-control', 'placeholder': '请输入用户名'})

    pwd = PasswordField(label='登录密码', validators=[validators.DataRequired(message='密码 不能为空'),
                                 validators.Length(min=6, message='密码不能少于3位数'),
                                  validators.Length(max=128, message='密码不能大于128位数')
                                ], render_kw={'class': 'form-control', 'placeholder': '请输入密码'})

    """


    repwd = PasswordField(label='重复密码', validators=[EqualTo('pwd', message='两次密码不一致'),
                                                  validators.DataRequired(message='重复密码不能为空')],
                        render_kw={'class': 'form-control', 'placeholder': '请输入重复密码'})     # 核对两次密码


    # 自定义字段验证(注册)
    def validate_name(self, obj):
        name = obj.data        # 接收过虑过的字段
        res = db.session.query(UserModel).filter(UserModel.name == name).first()   # 到数据库中查询数据
        if res:
            raise validators.ValidationError('用户已存在')   # 字段存在则弹出错误
        else:
            return None   # 不存在则返回字段


