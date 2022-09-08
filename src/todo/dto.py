from src.todo.model import Todo


def convertObjectToJson(object: Todo):
    return {
        "id": object.id,
        "name": object.name,
        "isDone": object.isDone
    }


def convertListObjectToJson(objects: list[Todo]):
    results = []
    for object in list(objects):
        results.append(convertObjectToJson(object=object))
    return results
