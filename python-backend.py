from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)

QUESTIONID = 0;

class postModel(db.Model):
	postId = db.Column(db.Integer, primary_key = True, nullable=False)
	userName = db.Column(db.String(30), nullable=False)
	className = db.Column(db.String(15), nullable = False)
	instructor = db.Column(db.String(15))
	postTitle = db.Column(db.String(), nullable = False)
	postBody = db.Column(db.String(), nullable = False)
	resolved = db.Column(db.Boolean, nullable = False)
	numViews = db.Column(db.Integer, nullable = False)


class answerModel(db.Model):
	answerId = db.Column(db.Integer, primary_key=True, nullable=False)
	postId = db.Column(db.Integer, nullable=False)
	answerBody = db.Column(db.String(), nullable = False)



# db.create_all()
getQuestionArgs = reqparse.RequestParser()

getQuestionArgs.add_argument("userName" , type=str)
getQuestionArgs.add_argument("titleQuery" , type=str, help="enter some title worlds", required=True)
getQuestionArgs.add_argument("className", type=str)

question_put_args = reqparse.RequestParser()
question_put_args.add_argument("name", type=str, help="Add Name: ")
question_put_args.add_argument("Title", type=str, help="Add Title: ")
question_put_args.add_argument("Content", type=str, help="Add Content: ")
question_put_args.add_argument("Class", type=str, help="Add Class: ")

resource_fields = {
    'postId' : fields.Integer,
    'userName' : fields.String,
    'className' : fields.String,
    'instructor' : fields.String,
    'postTitle' : fields.String,
    'postBody' : fields.String,
    'resolved' : fields.Boolean,
    'numViews' : fields.Integer,
}

class Questions (Resource):
 	
	def get(self):
		args = getQuestionArgs.parse_args()
		result = postModel.query.filter_by(postTitle=args['titleQuery']).first()
		return result

	def put (self):
		args = question_put_args.parse_args()
		question = postModel(postId = QUESTIONID, userName=args['useame'], postTitle=args['Title'], postBody=args['Content'], className=args['Class'], resolved=False, numViews=0  )
		QUESTIONID = QUESTIONID + 1
		db.session.add(question)
		db.session.commit()
		return question, 201

api.add_resource(Questions, "/Questions")

if __name__ == " __main__ " :
	app.run(debug=True)
