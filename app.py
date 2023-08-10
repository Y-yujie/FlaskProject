from flask import Flask, request, jsonify, session, g
import config
from exts import db, mail
from models import UserModel
# from blueprints.QA import bp as QA_bp
from blueprints.auth import bp as auth_bp

# 使用flask-migrate来管理数据库迁移，并将Flask应用程序连接到数据库
# 将模型映射到数据库中
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定config文件
app.config.from_object(config)

# 与db绑定, 与mail绑定
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

# blueprint: 用来做模块化
# 与蓝图绑定
# app.register_blueprint(QA_bp)
app.register_blueprint(auth_bp)


# before_request/ before_first_request/ after_request 执行视图函数前，先执行这些（拦截器）
# hook 钩子函数
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        # 把user绑定到全局对象g上
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


# 钩子函数
# 把用户名和退出登录放在上下文处理器中,后续在所有模板中都可以使用user
@app.context_processor
def my_context_precessor():
    return {"user": g.user}


if __name__ == '__main__':
    app.run(debug=True)
