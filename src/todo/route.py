
from asyncore import read
import os
from flask import Blueprint, jsonify, request, current_app
from flask_api import status
from flask_babel import gettext, ngettext

from src.execption.appException import Code
from src.execption.ecode import DatabaseError
from src.infa.database.BaseStorage import BaseStorage
from src.infa.logging.BaseLogging import BaseLogging
from src.pkg.localiza.l10n import format_datetime, format_percent, format_currency
from src.todo.usecase import ToDoUseCase
from src.todo.validateForm import validateFormPost
from datetime import date, datetime
from werkzeug.utils import secure_filename

todoRoute = Blueprint("todo", __name__)


def create_route(database: BaseStorage, logging: BaseLogging):
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
        dataRequest = dict(request.data)
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
        dataForm = dict(request.data)
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
            message = "Can't update resource"
            return jsonify({"message": message}), status.HTTP_204_NO_CONTENT

    @todoRoute.get("/time")
    def get_time():
        message = gettext("EDB01")
        return jsonify({"time": format_datetime(datetime.now()), "currency": format_currency(40000), "message": gettext("EDB01")})

    @todoRoute.post("/upload_file")
    def upload_file():
        if "file" not in request.files:
            return jsonify({"message": "no file part"})
        try:
            file = request.files.get("file")
            filename = secure_filename(filename=file.filename)
            if filename != "":
                file_ext = filename.split(".")[-1].lower()
                if file_ext in current_app.config["ALLOWED_EXTENSIONS"].split(","):
                    f = open(os.path.join(
                        current_app.config['UPLOAD_FOLDER'], filename), "w")
                    __handle_stream__file(file.stream, f)
                    f.close()
            logging.info(filename)
            return jsonify({"message": "ok"})
        except BaseException as error:
            return jsonify(DatabaseError.warp(cause=error)), DatabaseError.statusCode

    return todoRoute


def __handle_stream__file(stream, f):
    while 1:
        data = stream.read(1024 * 1024 * 10)
        if len(data) > 0:
            f.write(data.decode("utf16"))
        else:
            break
    return True
