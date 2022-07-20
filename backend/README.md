# Full Stack Trivia API Backend

## Getting Started
### Installing Dependencies

#### Python 3.7
Follow these steps [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) to install the latest version of Python for your platform.

#### Virtual Enviornment
When using Python for projects, we recommend working in a virtual environment. This keeps your project dependencies distinct and organized. Setup instructions for your platform's virtual environment may be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies
Install dependencies after your virtual environment is up and running by going to the '/backend' directory and executing:

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


## Endpoints

### GET '/categories'

- Fetches a dictionary of categories, where the keys are the ids and the value is the category's associated string.
- Request Arguments: None
- Returns: An object of categories (keys;value pairs), with keys: ids of categories, values: name of categories and success.

```json5
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

### GET '/questions'

- Fetches all questions
- Request Arguments: none
- Returns: 

```json5
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": "5", 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": "5", 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "4", 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 23
}

```

### POST '/questions'

- Adds a new question
- Request Arguments: Question body

```json5
{
  "question": "What is my name?",
  "answer": "Abdull Yahuza",
  "difficulty": 1,
  "category": 1
}
```

- Returns:

```json5
{
    "answer": "Abdull Yahuza",
    "category": 1,
    "difficulty": 1,
    "question": "What is my name?",
    "success": true
}
```

### GET '/categories/<int:category_id>/questions'
- Get questions by category
- Request Arguments: `category_id`
- Returns:

```json5
{
    "current_category": "Geography",
    "questions": [
        {
            "answer": "Lake Victoria",
            "category": "3",
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "3",
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Abdull Yahuza",
            "category": "3",
            "difficulty": 1,
            "id": 21,
            "question": "What is my name"
        },
        {
            "answer": "Abuja",
            "category": "3",
            "difficulty": 1,
            "id": 22,
            "question": "What is the capital of Nigeria?"
        }
    ],
    "success": true,
    "total_questions": 5
}
```

### POST '/questions/results'

- Search questions
- Request Arguments: searchTerm

```json5
{
  "searchTerm": "test"
}
```
- Returns:

```json5
{
    "current_category": null,
    "questions": [
        {
            "answer": "Abuja",
            "category": "3",
            "difficulty": 1,
            "id": 22,
            "question": "What is the capital of Nigeria?"
        }
    ],
    "success": true,
    "total_questions": 1
}
```

### POST '/quizzes'

- Play quiz
- Request Arguments: `quiz_category`

```json5
{
  "quiz_category": {
    "id": 3
  }
}
```

- Returns:

```
{
    "question": {
        "answer": "Abdull Yahuza",
        "category": "3",
        "difficulty": 1,
        "id": 24,
        "question": "What is my name"
    },
    "success": true
}
```

## Errors

### Bad Request (400)

- Returns:
```json5
{
  'success': false,
  'error': 400,
  'message': 'bad request'
}
```

### Not Found (404)

```json5
{
  'success': false,
  'error': 404,
  'message': 'not found'
}
```

### Unprocessable request (422)

```json5
{
  'success': false,
  'error': 422,
  'message': 'unprocessible'
}
```

### Internal server error (500)

```json5
{
  'success': false,
  'error': 500,
  'message': 'internal server error'
}
```

### Method not allowed (405)

```json5
{
  'success': false,
  'error': 500,
  'message': 'method not allowed'
}
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```