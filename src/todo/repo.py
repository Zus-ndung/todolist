from src.todo.model import Todo
from src.infa.database.BaseStorage import BaseStorage


class ToDoRepo():
    def __init__(self, database: BaseStorage) -> None:
        self.database = database

    def getAllTodoList(self):
        todoLists = Todo.query.all()
        
        return todoLists

    def createToDo(self, name, isDone):
        newToDo = Todo(name=name, isDone=isDone)
        newToDo = self.database.save(newToDo)
        return newToDo

    def getOneToDo(self, id):
        toDo = Todo.query.get_or_404(id)
        return toDo
