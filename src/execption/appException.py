import traceback


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

    def warp(self, error: BaseException, message: str):
        self.error = WithMessage(error=error, message=message)
        return self

    def convertToObject(self) -> dict:
        obj = {
            "statusCode": self.statusCode,
            "errorCode": self.errorCode,
        }
        if self.params is not None:
            obj["params"] = self.params
        if self.error is not None:
            obj["message"] = self.error.message
        return obj


class WithMessage(BaseException):
    def __init__(self, error: BaseException = None, message: str = "") -> None:
        self.cause = error
        self.message = message
        return


class AppException(Exception):
    def __init__(self, *args: object, message: str) -> None:
        super().__init__(message)
        self.warp = {}

    def warp(self, key, value) -> None:
        self.warp[key] = value

    def print_track(self, **kargs):
        traceback.print_stack(**kargs)

    def __str__(self) -> str:
        return super().__str__()
