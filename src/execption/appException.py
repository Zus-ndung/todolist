class Code(BaseException):
    def __init__(self, statusCode: int, errorCode: int) -> None:
        super().__init__()
        self.statusCode = statusCode
        self.errorCode = errorCode
        self.params = None
        self.error = None
        return

    def setParams(self, *args):
        self.params = args
        return self

    def warp(self, cause: BaseException, message=""):
        self.error = WithMessage(cause=cause, message=message)
        return self

    def convertToObject(self) -> dict:
        obj = {
            "statusCode": self.statusCode,
            "errorCode": self.errorCode,
        }
        if self.params is not None:
            obj["params"] = self.params
        if self.error is not None:
            if self.error.message is not None:
                obj["message"] = self.error.message
            if self.error.cause is not None:
                obj["cause"] = self.error.cause.__str__()
        return obj


class WithMessage(BaseException):
    def __init__(self, cause: BaseException = None, message: str = None) -> None:
        self.cause = cause
        self.message = message
        return
