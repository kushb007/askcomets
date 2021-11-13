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
	numViews = db.Column(db.Integer, nullable = False)


class answerModel(db.Model):
	answerId = db.Column(db.Integer, primary_key=True, nullable=False)
	postId = db.Column(db.Integer, nullable=False)
	answerBody = db.Column(db.String(), nullable = False)



#db.create_all()
getQuestionArgs = reqparse.RequestParser()

getQuestionArgs.add_argument("userName" , type=str)
getQuestionArgs.add_argument("titleQuery" , type=str, help="enter some title worlds", required=True)
getQuestionArgs.add_argument("className", type=str)

question_put_args = reqparse.RequestParser()
question_put_args.add_argument("name", type=str, help="Add Name: ")
question_put_args.add_argument("Title", type=str, help="Add Title: ")
question_put_args.add_argument("Content", type=str, help="Add Content: ")
question_put_args.add_argument("Class", type=str, help="Add Class: ")

getAnswerArgs = reqparse.RequestParser()
getAnswerArgs.add_argument("postid" , type=int)

answer_put_args = reqparse.RequestParser()
answer_put_args.add_argument("answerid", type=int)
answer_put_args.add_argument("answerbody", type=str)
answer_put_args.add_argument("postid", type=str)
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

resource_fields2 = {
    'answerId' : fields.Integer,
    'postId' : fields.Integer,
    'answerBody' : fields.String
}

class Questions (Resource):
	QUESTIONID = 0

	@marshal_with(resource_fields)
	def get(self):
		args = getQuestionArgs.parse_args()
		result = postModel.query.filter_by(postTitle=args['titleQuery']).first()
		return result

	@marshal_with(resource_fields)
	def put (self):
		args = question_put_args.parse_args()

		print(str(Questions.QUESTIONID))
		

		result = postModel.query.filter_by(postId=Questions.QUESTIONID).first()
		if (result):
			abort(409, message="post already exists")

		question = postModel(postId = Questions.QUESTIONID, userName=args['name'], postTitle=args['Title'], postBody=args['Content'], className=args['Class'], resolved=False, numViews=0  )
		Questions.QUESTIONID = Questions.QUESTIONID + 1

		db.session.add(question)
		db.session.commit()
		return question, 201

api.add_resource(Questions, "/Questions")

class Answers (Resource):
    ANSWERID = 8
    @marshal_with(resource_fields2)
    def get(self):
        args = getAnswerArgs.parse_args()
        result = answerModel.query.filter_by(postId=args['postId']).first()
        return result

    @marshal_with(resource_fields2)
    def put(self):
        args = answer_put_args.parse_args()
        answer = answerModel(answerId = Answers.ANSWERID, answerBody=args['answerbody'], postId=args['postid'])
        Answers.ANSWERID = Answers.ANSWERID + 1
        db.session.add(answer)
        db.session.commit()
        return answer, 201
api.add_resource(Answers, "/Answers")



if __name__ == "__main__" :
	app.run(debug=True)
