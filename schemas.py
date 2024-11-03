from extensions import ma
from models import Question, Answer

class QuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        include_relationships = True
        load_instance = True

class AnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Answer
        include_fk = True
        load_instance = True

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
answer_schema = AnswerSchema()
answers_schema = AnswerSchema(many=True)
