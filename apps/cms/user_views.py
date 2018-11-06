from flask import Response
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import session
# from sqlalchemy import and_, or_

# 导入用户模块
from apps.cms import cms_bp     # 导入蓝图
from apps.forms.user_forms import RegisterForm    # 导入注册验证表单模块
from apps.forms.user_forms import LoginForm        # 导入登录验证表单模块
from apps.models.user_models import UserModel     # 数据库模块
from apps.models import db

# 用户注册
@cms_bp.route('/reg', endpoint='reg',methods=['GET', 'POST'])
def user_reg_view():
    """
    if request.method == 'GET':
        return render_template('reg.html')
    elif request.method == 'POST':
        forms = RegisterForm(request.form)
        if forms.validate():
            # 表单验证通过后的数据
            user = forms.name.data
            pwd = forms.pwd.data
            # 写入数据库
            user = UserModel(name=user, pwd=pwd)
            db.session.add(user)
            db.session.commit()
            # 注册成功后跳转到登录页
            return redirect(url_for('cms.login'))
        else:
            # 注册失败将错误数据返回前端提示
            error = forms.errors     # 接收表单验证错误的数据
            return render_template('reg.html', **error)
    else:
        return render_template('error.html')
    """
    # 优化后的代码
    # 先生成一个forms实例并进行验证
    froms = RegisterForm(request.form)
    if request.method == 'POST' and froms.validate():
        # 实例化model
        data = UserModel()
        # 接收验证后的数据
        data.name = froms.name.data
        data.pwd = froms.pwd.data
        # 写入数据库
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('cms.login'))
    else:
        return render_template('regs.html', froms=froms)


# 用户登录
@cms_bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def user_login_view():
    """
    # 当请求方式为get时
    if request.method == 'GET':
        # 验证cookie
        if request.cookies.get('name'):
            # 存在跳转到个人中心
            return redirect(url_for('cms.info'))
        else:
            # 不存在跳转到登录页
            return render_template('login.html')
        # 当请求方式 为post时
    elif request.method == 'POST':
        # 接收表单提交的参数
        user = request.form.get('name')
        pwd = request.form.get('pwd')
        # 验证帐号密码
        if user =='admin' and pwd == 'admin':          #  密码验证
            # 验证成功，设置cookie并跳转
            response:Response = make_response(render_template('info.html'))
            response.set_cookie('name', 'admin')                # 设置cookie
            return response
        else:
            return render_template('login.html')
    else:
        # 当请求方式为其它时
        return render_template('error.html')
    """

    # 实例化一个登录验证表单
    forms = LoginForm(request.form)
    # 当请求方式为GET时
    if request.method == 'GET':
        # 验证cookie,存在则跳转到个人中心
        cookie = request.cookies.get('name')
        if cookie:
            return redirect(url_for('cms.info'))
        else:
            return render_template('logins.html', forms=forms)
    elif request.method == 'POST' and forms.validate():
        """
        # 验证成功设置cookie
        response:Response = make_response(redirect(url_for('cms.info')))
        response.set_cookie('name', forms.name.data, max_age=3600)   
        return response
        """
        #使用session
        session['name'] = 'name'
        return redirect(url_for('cms.info'))

    else:
        return render_template('logins.html', forms=forms)

# 个人中心
@cms_bp.route('/info', endpoint='info')
def user_info_view():
    cookie = request.cookies.get('name')
    if cookie:
        return render_template('info.html')
    else:
        return redirect(url_for('cms.index'))



# 安全退出 （清除cookie）
@cms_bp.route('/logout',endpoint='logout')
def user_logout_view():
    # 删除cookie并跳转到主页
    response:Response = make_response(redirect(url_for('cms.index')))
    response.delete_cookie('name')
    return response