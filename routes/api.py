from flask import Blueprint, request, jsonify
from models import Question, Answer
from schemas import question_schema, questions_schema, answer_schema, answers_schema
from extensions import db

api_bp = Blueprint("api", __name__)

@api_bp.route("/questions", methods=["GET", "POST"])
def api_questions():
    if request.method == "POST":
        content = request.json.get("content")
        new_question = Question(content=content)
        db.session.add(new_question)
        db.session.commit()
        return question_schema.jsonify(new_question), 201
    questions = Question.query.all()
    return questions_schema.jsonify(questions)

@api_bp.route("/questions/<int:question_id>/answers", methods=["GET", "POST"])
def api_answers(question_id):
    if request.method == "POST":
        content = request.json.get("content")
        new_answer = Answer(content=content, question_id=question_id)
        db.session.add(new_answer)
        db.session.commit()
        return answer_schema.jsonify(new_answer), 201
    answers = Answer.query.filter_by(question_id=question_id).all()
    return answers_schema.jsonify(answers)
