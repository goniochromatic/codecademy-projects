from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.app_context().push()

login = LoginManager(app)

login.login_view = 'login'

@login.user_loader
def load_user(id):
  return User.query.get(int(id))
  
import routes#, models
from models import User, Post