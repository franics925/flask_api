import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .commands import reset_items

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
  # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
  
  db.init_app(app)

  from .views import api
  app.register_blueprint(api)

  app.cli.add_command(reset_items)

  return app