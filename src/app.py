from flask import Flask, g
from dynaconf import FlaskDynaconf
from src.infa.database.Postgresql import Postgresql
from src.todo.route import todoRoute
from flask_sqlalchemy import SQLAlchemy


def create_instace_db(app):
    db = SQLAlchemy()
    if app.config["DATABASE_TYPE"] == "postgresql":
        postgresql = Postgresql(db=db)
        postgresql.init_db(app=app)
        g.db = postgresql
    else:
        pass


def create_app():
    app = Flask(__name__)
    # config
    FlaskDynaconf(app)

    # register route of module
    app.register_blueprint(todoRoute, url_prefix="/todo")

    # init_database
    with app.app_context():
        create_instace_db(app=app)

    app.run()
    return app


if __name__ == '__main__':
    create_app()
