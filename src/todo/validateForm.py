def validateFormPost(dataRequest: dict):
    name = dataRequest.get("name")
    isDone = dataRequest.get("isDone")
    error = {}
    if not type(name) is str:
        error["name"] = {"isRequired": True,
                         "message": "name field is required"}

    if not type(isDone) is bool:
        error["isDone"] = {"isRequired": True,
                           "message": "isDone field is required"}
    return error, len(error.keys()) == 0
