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
        try:
            self.db.init_app(app=app)
        except TypeError as error:
            print(error)
        else:
            print("Connect to database successfully")

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
