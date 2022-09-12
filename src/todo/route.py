from flask import Blueprint, request, jsonify
from src.infa.database.BaseStorage import BaseStorage
from src.infa.logging.BaseLogging import BaseLogging
from src.todo.usecase import ToDoUseCase
from flask_api import status


todoRoute = Blueprint("todo", __name__)


def create_route(database=BaseStorage, logging=BaseLogging):
    toDoUseCase = ToDoUseCase(database)

    @todoRoute.get("/")
    def handleGetAll():
        todoLists = toDoUseCase.getAll()

        logging.warning("hello dung ne")

        return jsonify(todoLists), status.HTTP_200_OK

    @todoRoute.post("/")
    def handleCreateTodo():
        dataRequest = request.data
        newToDo = toDoUseCase.create(
            dataRequest["name"], isDone=dataRequest["isDone"])
        return jsonify(newToDo), status.HTTP_201_CREATED

    @todoRoute.get("/<id>")
    def handleGetOne(id):
        idToDo = int(id)
        todo = toDoUseCase.getOne(id=idToDo)
        return jsonify(todo), status.HTTP_200_OK

    return todoRoute
