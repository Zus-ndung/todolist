from src.infa.database.BaseStorage import BaseStorage
from src.todo.dto import convertListObjectToJson, convertObjectToJson
from src.todo.repo import ToDoRepo


class ToDoUseCase:

    def __init__(self, database: BaseStorage) -> None:
        self.repo = ToDoRepo(database=database)

    def getAll(self):
        todoLists = self.repo.getAllTodoList()
        
        return convertListObjectToJson(todoLists)

    def create(self, name, isDone):
        return self.repo.createToDo(name=name, isDone=isDone)

    def getOne(self, id):
        todo = self.repo.getOneToDo(id=id)
        return convertObjectToJson(todo)
