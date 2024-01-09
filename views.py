# views.py
class TodoView:
    def show_todos(self, todos):
        print("To-Do List:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
