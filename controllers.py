# controllers.py
from models import TodoModel
from views import TodoView

class TodoController:
    def __init__(self):
        self.model = TodoModel()
        self.view = TodoView()

    def add_todo(self, todo):
        self.model.add_todo(todo)

    def show_todos(self):
        todos = self.model.get_todos()
        self.view.show_todos(todos)
