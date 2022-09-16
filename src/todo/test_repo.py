import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.execption.appException import Code
from src.infa.database.Postgresql import Postgresql
from dynaconf import FlaskDynaconf
from flask_migrate import Migrate, Config, command
from src.todo.repo import ToDoRepo
class TestRepo(unittest.TestCase):
    def setUp(self) -> None:
        app = Flask(__name__)
        db = SQLAlchemy()
        FlaskDynaconf(app)
        # print(app.config)
        migrate = Migrate()
        config = Config("migrations/alembic.ini")
        with app.app_context():
            self.database = Postgresql(db=db)
            self.database.init_db(app)
            self.repo = ToDoRepo(database=self.database)
            migrate.init_app(app=app, db=db)
            config.set_main_option("script_location", "migrations")
            command.upgrade(config, "head")

        app.app_context().push()

    def test_create(self):
        testCases = [
            {"name": "abc", "isDone": False, "isCreated": True},
            {"name": "abc2", "isDone": True, "isCreated": True},
            {"name": "abc3", "isDone": False, "isCreated": True},
            {"name": "abc4", "isDone": False, "isCreated": True},
            {"name": "abc5", "isDone": False, "isCreated": True},
            {"name": "abc6", "isDone": False, "isCreated": True}
        ]
        for testCase in testCases:
            with self.subTest(msg=f"testCase: {testCase.get('name')} - {testCase.get('isDone')}"):
                try:
                    todo = self.repo.create(name=testCase.get("name"), isDone=testCase.get("isDone"))
                    self.assertEqual(todo.name, testCase.get("name"))
                except Code as code:
                    print(code.error.cause.__str__())

    def tearDown(self) -> None:
        pass
