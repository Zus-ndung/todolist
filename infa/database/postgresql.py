from sqlite3 import connect
from infa.database.database import Database
import psycopg2


class Postgresql(Database):
    def __init__(self):
        super().__init__()

    def connect(self):
        try:
            self.conn = psycopg2.connect(host=self.DATABASE_HOST, database=self.DATABASE_NAME,
                                         user=self.DATABASE_USER, password=self.DATABASE_PASSWORD)
        except Exception as error:
            print("Can't connect to postgresql", error)
        else:
            print("Connect successfully")

    def disconnect(self):
        if self.conn is None:
            raise TypeError("This application wasn't connected to postgresql")
        else:
            self.conn.close()
