from src.infa.database.BaseStorage import BaseStorage


class Postgresql(BaseStorage):

    def __init__(self, db) -> None:
        super().__init__()
        self.db = db

    def save(self):
        self.db.add(self)
        self.db.commit()
        return self.id

    def init_db(self, app):
        try:
            self.db.init_app(app=app)
        except TypeError as error:
            print(error)
        else:
            print("Connect to database successfully")
