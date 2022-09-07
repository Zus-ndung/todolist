from flask import current_app


class Database:

    def __init__(self) -> None:
        self.DATABASE_HOST = current_app.config["DATABASE_HOST"]
        self.DATABASE_USER = current_app.config["DATABASE_USER"]
        self.DATABASE_PASSWORD = current_app.config["DATABASE_PASSWORD"]
        self.DATABASE_NAME = current_app.config["DATABASE_NAME"]
        print(self.DATABASE_HOST, self.DATABASE_USER,
              self.DATABASE_NAME, self.DATABASE_PASSWORD)

    def connect(self):
        pass

    def disconnect(self):
        pass
