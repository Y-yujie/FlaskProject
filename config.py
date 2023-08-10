"""
@author: Yyujie
@email: yyj17320071233@163.com
@Date: 2023/7/19 10:45
@Description: Configuration file
"""

# 加密盐
SECRET_KEY = "daubfeiwopdfbcweidw"

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'itcast'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2498899860@qq.com"
MAIL_PASSWORD = "csykoqdvyrgrecca"
MAIL_DEFAULT_SENDER = "2498899860@qq.com"
