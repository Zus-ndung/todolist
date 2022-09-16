from src.execption.ecode import DatabaseError
from src.infa.database.BaseStorage import BaseStorage


class Postgresql(BaseStorage):
    def __init__(self, db) -> None:
        super().__init__()
        self.db = db

    def save(self, object):
        try:
            self.db.session.add(object)
            self.db.session.commit()
            return object
        except BaseException as error:
            raise DatabaseError.warp(cause=error, message=None)

    def init_db(self, app):
        self.db.init_app(app=app)
        isConnected = self.__isConnected()
        if not isConnected:
            raise Exception("Database wasn't connected")
        return

    def remove(self, record):
        try:
            record = self.db.session.get(type(record), record.id)
            self.db.session.delete(record)
            self.db.session.commit()
            return True
        except BaseException as error:
            raise DatabaseError.warp(cause=error, message=None)

    def update(self, record, data):
        try:
            toDo = self.db.session.get(type(record), record.id)
            if toDo is not None:
                for k, v in data.items():
                    setattr(toDo, k, v)
            self.db.session.commit()
            return toDo

        except BaseException as error:
            raise DatabaseError.warp(cause=error, message=None)

    def __isConnected(self):
        try:
            self.db.session.execute("SELECT 1")
            return True
        except Exception:
            return False
