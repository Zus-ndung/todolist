from src.execption.ecode import DatabaseNotResponse, NotFound
from src.infa.database.BaseStorage import BaseStorage
from src.todo.model import Todo


class ToDoRepo:
    def __init__(self, database: BaseStorage) -> None:
        self.database = database

    def getAll(self):
        try:
            todoLists = Todo.query.all()
            return todoLists
        except BaseException as error:
            raise DatabaseNotResponse.warp(cause=error, message=None)

    def create(self, name, isDone):
        newToDo = Todo(name=name, isDone=isDone)
        newToDo = self.database.save(newToDo)
        return newToDo

    def getOne(self, id):
        try:
            toDo = Todo.query.get(id)
        except BaseException as error:
            raise DatabaseNotResponse.warp(cause=error, message=None)
        return toDo

    def remove(self, id):
        toDo = self.getOne(id=id)
        if toDo is not None:
            return self.database.remove(toDo)
        else:
            raise NotFound.warp(
                cause=None, message=f"Resource Todo - {id} wasn't existed"
            ).setParams({"idToDo": id})

    def update(self, id, data):
        toDo = self.getOne(id)
        if toDo is not None:
            return self.database.update(toDo)
        else:
            raise NotFound.warp(
                cause=None, message=f"Resource Todo - {id} wasn't existed"
            ).setParams({"idToDo": id})
