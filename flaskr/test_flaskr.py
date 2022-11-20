import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://postgres:root@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)


        self.new_question = {
            'question': 'Which one is the largest continent in the world',
            'answer': 'Africa',
            'difficulty': 2,
            'category': 3
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
  @DONE
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_404_request_beyond_valid_page(self):
        res = self.client().get("/questions?page=100000")
        data = json.loads(res.data)
    
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_question_not_allowed(self):
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')


    def test_delete_question(self):
        res = self.client().delete('/questions/5')
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'],2)

    def test_422_for_question_does_not_exist(self):
        response = self.client().delete('/questions/98575')


        self.assertEqual(response.status_code, 404)



    def test_get_questions_search_with_results(self):
        res = self.client().post("/searchquestions", json={"searchTerm": "medicine"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
       

    def test_get_questions_search_without_results(self):
        res = self.client().post("/searchquestions", json={"searchTerm": "zxaxasdcaxf"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["total_questions"], 0)


    def test_get_question_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['current_category'], 'science')
        self.assertEqual(data['success'], True)
      

    def test_get_question_by_category_not_found(self):
        res = self.client().get('/categories/0/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)

    def test_play_quiz(self):
        quiz_round = {'previous_questions': [], 'quiz_category': {'type': 'Geography', 'id': 14}}
        response = self.client().post('/playquiz', json=quiz_round)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_play_quiz_unproccessible(self):
        response = self.client().post('/playquiz', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()











   