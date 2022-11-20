# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


## API Reference

### Getting Started 
Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
Authentication: This version does not require authentication or API keys.

### Error Handling

The API will return this errors;
- 400 - bad request
- 404 - resource not found
- 422 - unprocessable
- 500 - Server Error
- 405 - Method Not allowed

### Endpoints

#### GET '/categories'
- Gets all the available categories of questions in the database 
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs
- Sample: `curl http://127.0.0.1:5000/categories`
```
{
  "categories":
  {"1":"Science","2":"Art","3":"Geography","4":"History","5":"Entertainment","6":"Sports"},"current_category":null,
  "success":true
  }
```

#### GET '/categories/<int:id>/questions'
- Gets all questions in a specified category by id using url parameters
- Sample: `curl http://127.0.0.1:5000/categories/3/questions`
```
{
  "current_category":null,
  "questions":
  [
    {"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},
    {"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"}],
    "success":true,
    "total_questions":2
}
```

#### GET '/questions'
- Returns a list of questions Including a list of categories, a list of paginated 10 questions with details of question such as category, difficulty, answer and id
- Sample: `curl http://127.0.0.1:5000/questions`
```
{
  "categories":
  {"1":"Science",
  "2":"Art",
  "3":"Geography",
  "4":"History",
  "5":"Entertainment",
  "6":"Sports"},
  "current_category":null,
  "questions":[
    {"answer":"Apollo 13","category":5,"difficulty":4,"id":2,"question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},
    {"answer":"Tom Cruise","category":5,"difficulty":4,"id":4,"question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},
    {"answer":"Brazil","category":6,"difficulty":3,"id":10,"question":"Which is the only team to play in every soccer World Cup tournament?"},
    {"answer":"Uruguay","category":6,"difficulty":4,"id":11,"question":"Which country won the first ever soccer World Cup in 1930?"},
    {"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},
    {"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"},
    {"answer":"Escher","category":2,"difficulty":1,"id":16,"question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"},
    {"answer":"Mona Lisa","category":2,"difficulty":3,"id":17,"question":"La Giaconda is better known as what?"},{"answer":"One","category":2,"difficulty":4,"id":18,"question":"How many paintings did Van Gogh sell in his lifetime?"},
    {"answer":"Jackson Pollock","category":2,"difficulty":2,"id":19,"question":"Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"}],
    "success":true,
    "total_questions":17
    }
```

### DELETE '/questions/<int:id>'
- Deletes a question by id using url parameters
- Returns deleted question id if successfully deleted
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/3`
```
{
  "deleted question":3,
  "success":true,
  "total":16
}

```

#### POST '/searchquestions'
- Search for a question basing on the search Term entered, 
- Returns a question with that searchTerm

- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "medicine"}'`
```
{
  "questions":[
  {"answer":"Blood",
  "category":1,"difficulty":4,
  "id":22,
  "question":"Hematology is a branch of medicine involving the study of what?"}],
  "success":true,
  "total_questions":19
}
```
#### POST '/questions'
- Creates a new question in the database
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "Who is the head couch of manchester city FC", "answer": "Pep Guardiola", "difficulty": 3, "category": "6" }'`
- Created_question:
```
{
"created":28,
"question_created":"Who is the head couch of manchester city FC"
}
```
- JSON response:
```

"questions":[
  {
    "answer":"Apollo 13",
    "category":5,
    "difficulty":4
    "id":2,"question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },

  {
    "answer":"Tom Cruise",
    "category":5,"difficulty":4,
    "id":4,
    "question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
  },

  {
    "answer":"Brazil",
    "category":6,
    "difficulty":3,
    "id":10,
    "question":"Which is the only team to play in every soccer World Cup tournament?"
    },

  {
    "answer":"Uruguay",
    "category":6,
    "difficulty":4,
    "id":11,
    "question":"Which country won the first ever soccer World Cup in 1930?"
    },

  {
    "answer":"Lake Victoria",
    "category":3,
    "difficulty":2,
    "id":13,
    "question":"What is the largest lake in Africa?"
    },

  {
    "answer":"The Palace of Versailles",
    "category":3,"difficulty":3,
    "id":14,
    "question":"In which royal palace would you find the Hall of Mirrors?"
  },
  {
    "answer":"Escher",
    "category":2,"difficulty":1,
    "id":16,
    "question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
  },

  {
  "answer":"Mona Lisa",
  "category":2,"difficulty":3,
  "id":17,
  "question":"La Giaconda is better known as what?"
  },

  {
  "answer":"One",
  "category":2,
  "difficulty":4,
  "id":18,
  "question":"How many paintings did Van Gogh sell in his lifetime?"},
  {
    "answer":"Jackson Pollock","category":2,"difficulty":2,"id":19,
    "question":"Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }],"success":true,"total_questions":17}
```


#### POST '/playquiz'
- Allows user to play the trivia Quiz game




