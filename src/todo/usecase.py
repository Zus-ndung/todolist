from src.infa.database.BaseStorage import BaseStorage
from src.todo.dto import convertListObjectToJson, convertObjectToJson
from src.todo.repo import ToDoRepo


class ToDoUseCase:
    def __init__(self, database: BaseStorage) -> None:
        self.repo = ToDoRepo(database=database)

    def getAll(self):
        todoLists = self.repo.getAll()
        return convertListObjectToJson(todoLists)

    def create(self, name, isDone):
        newTodo = self.repo.create(name=name, isDone=isDone)
        return convertObjectToJson(newTodo)

    def getOne(self, id):
        todo = self.repo.getOne(id=id)
        return convertObjectToJson(todo)

    def remove(self, id):
        return self.repo.remove(id=id)

    def update(self, id, data):
        updateToDo = self.repo.update(id, data)
        return convertObjectToJson(updateToDo)
