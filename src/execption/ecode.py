from flask_api import status

from src.execption.appException import Code

Internal = Code(
    statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, errorCode=100000)

NotFound = Code(statusCode=status.HTTP_404_NOT_FOUND, errorCode=200000)
