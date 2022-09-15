import subprocess
import unittest

from src.app import create_app
from src.execption.appException import Code
from src.infa.database.Postgresql import Postgresql
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
from dynaconf import FlaskDynaconf

from src.todo.repo import ToDoRepo
from flask_migrate import Migrate


class TestRepo(unittest.TestCase):
    def setUp(self) -> None:
        print("Set up testing")
        super().setUp()
        app = FlaskAPI(__name__)
        FlaskDynaconf(app)
        app.config["FLASK_ENV"] = "test"
        migrate = Migrate()
        db = SQLAlchemy()
        with app.app_context():
            self.database = Postgresql(db=db)
            self.database.init_db(app)
            migrate.init_app(app, db)
            self.repo = ToDoRepo(database=self.database)
            print("xxxxxx2222222222223xxxxxxxxxxxxxx", self.database.isConnected())
            subprocess.run(["flask", "--app", "src/app", "db", "upgrade"])

    def test_create(self):
        testCases = [
            {"name": "abc", "isDone": False, "isCreated": True},
            # {"name": "abc2", "isDone": True, "isCreated": True},
            # {"name": "abc3", "isDone": False, "isCreated": True},
            # {"name": "abc4", "isDone": False, "isCreated": True},
            # {"name": "abc5", "isDone": False, "isCreated": True},
            # {"name": "abc6", "isDone": False, "isCreated": True}
        ]
        for item in testCases:
            with self.subTest(msg=f"object:{item.get('name')} - {item.get('isDone')}"):
                try:
                    print("xxxxxxxxxxxxxxxxxxxx", self.database.isConnected())
                    todo = self.repo.create(name=item.get("name"), isDone=item.get("isDone"))
                except Code as code:
                    print("xxx", code.error.cause.__str__())
                if todo is not None:
                    existedToDo = self.repo.getOne(todo.id)
                    self.assertEqual(item.get("name"), existedToDo.get("name"), "abc")
                    self.assertEqual(item.get("isDone"), existedToDo.get("isDone"), "abc1")

    def tearDown(self) -> None:
        print("turnDown testing")
        subprocess.run(["flask", "--app", "src/app", "db", "downgrade"])
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
