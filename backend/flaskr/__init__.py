import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions
    # get a question by id from questions
def get_question(question_id,questions):
    for question in questions:
        if question.id == question_id:
             return question

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app,resources={r"*":{"origins":"*"}})
  

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS,PATCH"
        )
        return response
  
    @app.route("/categories")
    def get_categories():
        # to get the all the categories
        all_categories = Category.query.all()
    
        if len(all_categories) == 0:
            abort(404)
 
        categories_list = {}
        for a_category in all_categories:
            categories_list[a_category.id] = a_category.type

        return jsonify({
            "success": True,
            "categories": categories_list
        })

    @app.route("/questions")
    def get_questions():
        # to get the questions
        query_questions = Question.query.all()
        paginated_questions = paginate_questions(request, query_questions)

        # TO get all categories
        query_categories = Category.query.all()

        # the list of all categories
        categories_list = {}
        for category in query_categories:
            categories_list[category.id] = category.type

        # return 404 for empty question
        if len(paginated_questions) == 0 :
            abort(404)

        return jsonify({
            "success": True,
            "questions": paginated_questions,
            "total_questions": len(query_questions),
            "categories": categories_list,
            "current_category": None
        })
     
        # to Delete a question
    @app.route("/questions/<int:q_id>", methods=['DELETE']) 
    def delate_a_question(q_id):
        try:
            query_question = Question.query.get(q_id)
            if query_question is None:
                abort(404)
            query_question.delete()
        except:
            abort(422)
        return jsonify({
            "success": True,
            "deleted": q_id
        })
    
    @app.route('/questions', methods=['POST'])
    def a_new_question():
        body = request.get_json()
        try:
            new_question = Question(
                body['question'],
                body['answer'],
                body['category'],
                body['difficulty']
            )
            new_question.insert()
           
            return jsonify({
                "success": True,
                "question": new_question.question
            })
        except BaseException:
            abort(422)
   
    @app.route('/questions/search', methods=['POST'])
    def search_term():
        try:
            term = request.get_json()['searchTerm']
            search_term = '%{}%'.format(term)

            questions = Question.query.filter(
                Question.question.ilike(search_term)).all()
            questions_list = [question.format() for question in questions]

            return jsonify({
                 "success": True,
                "questions": questions_list,
                "total_questions": len(questions_list),
                "current_category": None
            })
        except:
            abort(405)
  
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_qestions_by_category(category_id):
        try:
            # get all the questions filtered by cat_id
            query_questions = Question.query.filter_by(
                category=str(category_id)).order_by(
                Question.id).all()
            questions_list = [question.format() for question in query_questions]

            # get category
            category = Category.query.get(category_id)

            # else return json object
            return jsonify({
                "success": True,
                "questions": questions_list,
                "total_questions": len(query_questions),
                "current_category": category.type
            })
        except BaseException:
            abort(404)
   
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():

        try:
            # get the category id
            c_id = int(request.get_json()['quiz_category']['id'])
            answered_q = request.get_json().get(
                'previous_questions')  # previous questions

            if answered_q is None:
                answered_q = []
            
            query_categories = Category.query.all()  # query categories

            # store categories ids for check
            category_list = []
            for category_id in query_categories:
                category_list.append(category_id.id)

            # if category is not specified -> ALL
            if c_id == 0:
                # get all the questions
                all_questions = Question.query.order_by(Question.id).all()

                question_list = []  # store the questions ids for comparison agains previous_questions
                for question_id in all_questions:
                    question_list.append(question_id.id)

            elif (c_id in category_list):  # a specific category
                # get all the questions filtered by category id
                all_questions = Question.query.filter_by(
                    category=str(c_id)).order_by(
                    Question.id).all()

                question_list = []
                for question_id in all_questions:
                    question_list.append(question_id.id)
            else:
                abort(400)

            # get random question id from questions_id
            random_q = random.choice(question_list)

            # let assume the question is not answered
            is_answered = False
            # while the question is not answered, send the question and mark it
            # answered
            while not is_answered:
                if random_q in answered_q:
                    random_q = random.choice(question_list)
                else:
                    is_answered = True
                # base case
                if len(all_questions) == len(answered_q):
                    return jsonify({"success": True})

            question = get_question(random_q,all_questions)

            return jsonify({
                "success": True,
                "question": question.format()
            })
        except BaseException:
            abort(400)
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return({
            "success": False,
            "message": "resource not found",
            "error": 404
        }), 404

    @app.errorhandler(422)
    def unprocessible(error):
        return({
            "success": False,
            "message": "unprocessable",
            "error": 422
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return({
            "success": False,
            "message": "bad request",
            "error": 400
        }), 400

    @app.errorhandler(405)
    def not_found(error):
        return (jsonify({"success": False, "error": 405,
                         "message": "method not allowed"}), 405)

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    return app

