from flask import flask, render_template
from flask_sqlachemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =flask_sqlachemy

db = SQLAlchemy(app)

class Todo(db.Model):
	id = 