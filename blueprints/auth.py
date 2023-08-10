"""
@author: Yyujie
@email: yyj17320071233@163.com
@Date: 2023/7/19 11:03
@Description: 用户相关
"""
import csv
import random

from flask import Blueprint, render_template, jsonify, redirect, url_for, session, Response
from exts import mail, db
from flask_mail import Message
from flask import request
import string
from models import EmailCaptchaModel, ResultModel
from .forms import RegisterForm, LoginForm
from models import UserModel

# flask中密码加密的方法
from werkzeug.security import generate_password_hash, check_password_hash

# Blueprint对象
bp = Blueprint("auth", __name__, url_prefix="/auth")


# 视图函数
@bp.route("/index")
def index():
    return render_template("index.html")


# # 将预测结果数据插入数据库
# @bp.route('/adddata')
# def adddatar():
#     with open('predict.csv', 'r', encoding='utf=-8') as f:
#         reader = csv.reader(f)
#         if reader != None:
#             for i in reader:
#                 result = ResultModel(name=i[0], numbers=i[1])
#                 db.session.add(result)
#             db.session.commit()
#         return ''

# # 测试Ajax的用法,从客户端（javascript）向服务器端（flask）发送异步请求来创建动web应用程序。能够在不重新加载整个页面的情况下更新网页的内容
# # 创建一个路由来处理AJAX请求
# @bp.route('/process_data', methods=['POST'])
# def process_data():
#     data_from_ajax = request.get_json()
#     # Process the data (you can add your logic here)
#     result = {'message': 'Data received successfully!'}
#     return jsonify(result)  # Return a JSON response

# 测试连接数据库，从前端发送请求信息，后端响应对应数据
@bp.route('/get_data', methods=['GET'])
def get_data():
    data = ResultModel.query.all()
    return jsonify([{
        'name': row.name,
        'numbers': row.numbers
    } for row in data])


# 返回某字段值与前端某一变量相等的一条数据
@bp.route('/search_data', methods=['POST'])
def search_data():
    data_from_fronted = request.json.get('customVariable')
    if data_from_fronted:
        # 查询数据库以找到与搜索值匹配的记录
        result = ResultModel.query.filter_by(name=data_from_fronted).first()
        if result:
            return jsonify([{
                'name': result.name,
                'numbers': result.numbers
            }])
        else:
            return jsonify({'message': 'Data not found'}), 404

    else:
        return jsonify({'message': 'Invalid request.'}), 404


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("用户不存在！")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # cookie
                # cookie中不适合存放太多数据
                # cookie一般用来存储授权的东西
                # flask中的session，是经过加密后存储在cookie中的
                session['user_id'] = user.id
                return redirect(url_for("auth.index"))
            else:
                print("密码错误！")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


# GET：从服务器上获取数据。POST：将客户端的数据提交给服务器
@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # 表单验证：flask-wtf
        # 验证用户提交的邮箱和验证码是否对应且正确，
        # 获取前端提交的数据
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data

            user = UserModel(email=email, username=username, password=generate_password_hash(password))  # 密码加密
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))  # 将视图函数转换为url
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


# 退出登录，清除cookie中的session信息
@bp.route("/logout")
def logout():
    session.clear()
    # 跳转到首页
    return redirect("auth.login")


@bp.route("/captcha/email")
def get_email_cpatcha():
    # 传参有两种方式
    # 1、 /captcha/email/<email> :路径传参
    # 2、 /captcha/email?email=xxx@qq.com  :查询字符串的方式传参
    email = request.args.get("email")
    # 随机产生4/6位数字， string中
    # string.digits*4 --》0123456789012345678901234567890123456789
    source = string.digits * 4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)  # 验证码格式转化
    print(captcha)
    message = Message(subject="验证码", recipients=[email], body=f"您的验证码是：{captcha}")
    mail.send(message)
    # 在服务器上存储验证码，以验证验证码是否正确且对应，
    # 缓存 memcached/redis
    # 用数据库表的方式存储
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API
    return jsonify({"code": 200, "message": "", "data": None})  # JS动态页面， jsonfy是一种数据格式
