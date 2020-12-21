from flask import Flask
from main.route import routes
from configuration import MysqlConfiq
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(routes)

#sqlalchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = MysqlConfiq.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = MysqlConfiq.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)