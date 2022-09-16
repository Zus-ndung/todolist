from flask import Blueprint, jsonify, request
from flask_api import status

from src.execption.appException import Code
from src.infa.database.BaseStorage import BaseStorage
from src.infa.logging.BaseLogging import BaseLogging
from src.todo.usecase import ToDoUseCase
from src.todo.validateForm import validateFormPost

todoRoute = Blueprint("todo", __name__)


def create_route(database=BaseStorage, logging=BaseLogging):
    toDoUseCase = ToDoUseCase(database)

    @todoRoute.get("/")
    def handleGetAll():
        try:
            todoLists = toDoUseCase.getAll()
            return jsonify(todoLists), status.HTTP_200_OK
        except Code as error:
            return jsonify(error.convertToObject()), error.statusCode

    @todoRoute.post("/")
    def handleCreateTodo():
        dataRequest = request.data
        error, isValid = validateFormPost(dataRequest)
        if not isValid:
            return jsonify(error), status.HTTP_400_BAD_REQUEST

        try:
            newToDo = toDoUseCase.create(
                dataRequest["name"], isDone=dataRequest["isDone"]
            )
            return jsonify(newToDo), status.HTTP_201_CREATED
        except Code as error:
            return jsonify(error.convertToObject()), error.statusCode

    @todoRoute.get("/<id>")
    def handleGetOne(id):
        try:
            idToDo = int(id)
            todo = toDoUseCase.getOne(id=idToDo)
            return jsonify(todo), status.HTTP_200_OK
        except Code as error:
            return jsonify(error.convertToObject()), error.statusCode

    @todoRoute.delete("/<id>")
    def handleDelete(id):
        try:
            idToDo = int(id)
            toDoUseCase.remove(id=idToDo)
            return status.HTTP_204_NO_CONTENT
        except ValueError as error:
            return jsonify({"message", error.__str__()}), status.HTTP_400_BAD_REQUEST
        except Code as error:
            return jsonify(error.convertToObject()), error.statusCode

    @todoRoute.put("/<id>")
    def handleUpdate(id):
        dataForm = request.data
        error, isValid = validateFormPost(dataForm)
        if not isValid:
            return jsonify(error), status.HTTP_400_BAD_REQUEST
        try:
            idTodo = int(id)
            isUpdated = toDoUseCase.update(id=idTodo, data=dataForm)
        except ValueError as error:
            return jsonify({"message", error.__str__()}), status.HTTP_400_BAD_REQUEST
        except Code as error:
            return jsonify(error.convertToObject()), error.statusCode

        if isUpdated:
            message = "Update resource successfully"
            return jsonify({"message": message}), status.HTTP_200_OK
        else:
            message = "Cann't update resource"
            return jsonify({"message": message}), status.HTTP_204_NO_CONTENT

    return todoRoute
