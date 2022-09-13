from pickle import FALSE

from src.execption.appException import AppException
from src.infa.database.BaseStorage import BaseStorage


class Postgresql(BaseStorage):
    def __init__(self, db) -> None:
        super().__init__()
        self.db = db

    def save(self, object):
        self.db.session.add(object)
        self.db.session.commit()
        return object

    def init_db(self, app):

        self.db.init_app(app=app)
        isConnected = self.__isConnected()
        if not isConnected:
            raise AppException(message="Database wasn't connected")
        return

    def remove(self, record):
        record = self.db.session.get(type(record), record.id)
        self.db.session.delete(record)
        self.db.session.commit()
        return True

    def update(self, record, data):
        toDo = self.db.session.get(type(record), record.id)
        if toDo is not None:
            for k, v in data.items():
                setattr(toDo, k, v)
        self.db.session.commit()
        return toDo

    def __isConnected(self):
        try:
            self.db.session.execute("SELECT 1")
            return True
        except Exception:
            return False
