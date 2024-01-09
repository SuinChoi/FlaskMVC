# models.py
class TodoModel:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def get_todos(self):
        return self.todos
