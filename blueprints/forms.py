"""
@author: Yyujie
@email: yyj17320071233@163.com
@Date: 2023/7/20 11:32
@Description
"""

import wtforms
from wtforms.validators import Email, Length, EqualTo
from models import UserModel, EmailCaptchaModel


class RegisterForm(wtforms.Form):
    email = wtforms.EmailField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码格式错误！")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # 自定义验证
    # 邮箱是否已注册
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册！")

    # 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
        if not captcha_model:
            raise wtforms.ValidationError(message="邮箱或验证码错误！")

        # todo: 可以删掉captcha_model, 不能重复登录


class LoginForm(wtforms.Form):
    email = wtforms.EmailField(validators=[Email(message="邮箱格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])
