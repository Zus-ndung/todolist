from flask import Blueprint, request, make_response, jsonify, g, current_app
from src.todo.usecase import ToDoUseCase


todoRoute = Blueprint("todo", __name__)


@current_app.context_processor
def init_usecase():
    toDoUseCase = ToDoUseCase(database=g.db)


@todoRoute.get("/")
def handleGetAll():
    todoLists = toDoUseCase.getAll()
    # response = make_response(jsonify(todoLists), 200)
    return todoLists


@todoRoute.post("/")
def handleCreateTodo():
    dataRequest = request.get_json()
    newToDo = toDoUseCase.create(
        dataRequest["name"], isDone=dataRequest["isDone"])
    response = make_response(jsonify(newToDo), 201)
    return response


@todoRoute.get("/<id>")
def handleGetOne(id):
    idToDo = int(id)
    todo = toDoUseCase.getOne(id=idToDo)
    response = make_response(jsonify(todo), 209)
    return response
