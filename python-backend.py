from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)

class postModel(db.Model):
	postId = db.Column(db.Integer, primary_key = True, nullable=False)
	userName = db.Column(db.String(30), nullable=False)
	className = db.Column(db.String(15), nullable = False)
	instructor = db.Column(db.String(15))
	postTitle = db.Column(db.String(), nullable = False)
	postBody = db.Column(db.String(), nullable = False)
	resolved = db.Column(db.Boolean, nullable = False)
	numViews = db.Column(db.Integer, nullable = False


class answerModel(db.Model):
	answerId = db.Column(db.Integer, primary_key=True, nullable=False)


# db.create_all()
# getArgs = reqparse.RequestParser()

# getArgs.add_argument("userName" , type=str, help="please enter username", required=True)
