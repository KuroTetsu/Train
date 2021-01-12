from flask import Flask
from main.route import routes as route
from configuration import MysqlConfiq
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(route)

#sqlalchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = MysqlConfiq.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = MysqlConfiq.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)