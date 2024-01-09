# app.py
from flask import Flask, request

from controllers import TodoController

app = Flask(__name__)
todo_controller = TodoController()

@app.route('/')
def index():
    return "Hello, this is a Flask MVC application!"

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    todo_controller.add_todo(todo)
    return "To-Do added successfully!"

@app.route('/show_todos')
def show_todos():
    todo_controller.show_todos()
    return "To-Do List displayed in console!"

if __name__ == '__main__':
    app.run(debug=True)
