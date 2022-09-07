from src.infa.database.BaseStorage import BaseStorage
from src.todo.repo import ToDoRepo


class ToDoUseCase:

    def __init__(self, database: BaseStorage) -> None:

        self.repo = ToDoRepo(database=database)

    def getAll(self):
        todoLists = self.repo.getAllTodoList()
        return todoLists

    def create(self, name, isDone):
        return self.repo.createToDo(name=name, isDone=isDone)

    def getOne(self, id):
        return self.repo.getOneToDo(id=id)
