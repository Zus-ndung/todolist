from src.infa.database.BaseStorage import BaseStorage
from src.todo.dto import convertListObjectToJson, convertObjectToJson
from src.todo.repo import ToDoRepo
import logging


class ToDoUseCase:

    def __init__(self, database: BaseStorage) -> None:
        self.repo = ToDoRepo(database=database)

    def getAll(self):
        todoLists = self.repo.getAllTodoList()
        # logging.basicConfig(filename='example.log',
        #                     encoding='utf-8', level=logging.DEBUG)
        # logging.debug('This message should go to the log file')
        # logging.info('So should this')
        # logging.warning('And this, too')
        # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

        return convertListObjectToJson(todoLists)

    def create(self, name, isDone):
        return self.repo.createToDo(name=name, isDone=isDone)

    def getOne(self, id):
        todo = self.repo.getOneToDo(id=id)
        logging.basicConfig(filename='example.log', format='%(funcName)s %(levelname)s',
                            encoding='utf-8', level=logging.DEBUG)
        logging.debug('Ngueyn van dung')
        return convertObjectToJson(todo)
