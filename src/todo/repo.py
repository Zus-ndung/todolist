from src.todo.model import Todo
from src.infa.database.BaseStorage import BaseStorage


class ToDoRepo():
    def __init__(self, database: BaseStorage) -> None:
        self.database = database

    def getAll(self):
        todoLists = Todo.query.all()

        return todoLists

    def create(self, name, isDone):
        newToDo = Todo(name=name, isDone=isDone)
        newToDo = self.database.save(newToDo)
        return newToDo

    def getOne(self, id):
        toDo = Todo.query.get_or_404(id)
        return toDo

    def remove(self, id):
        toDo = Todo.query.get(id)
        if toDo is not None:
            return self.database.remove(toDo)
        else:
            return False

    def update(self, id, data):
        toDo = Todo.query.get(id)
        if toDo is not None:
            return self.database.update(toDo, data)
        else:
            return False
