from src.todo.model import Todo
from src.infa.database.BaseStorage import BaseStorage


class ToDoRepo():
    def __init__(self, database: BaseStorage) -> None:
        self.database = database

    def getAllTodoList():
        todoLists = Todo.query.all()
        return todoLists

    def createToDo(self, name, isDone):
        newToDo = Todo(name=name, isDone=isDone)
        newToDo = self.database.save()
        return {"id": newToDo.id}

    def getOneToDo(id):
        toDo = Todo.query.filter_by(id=id)
        return toDo
