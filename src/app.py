from flask_api import FlaskAPI
from dynaconf import FlaskDynaconf
from src.infa.database.Postgresql import Postgresql
from src.todo.route import create_route
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = FlaskAPI(__name__)
    # config
    FlaskDynaconf(app)

    db = SQLAlchemy()
    if app.config["DATABASE_TYPE"] == "postgresql":
        postgresql = Postgresql(db=db)
        postgresql.init_db(app=app)
    else:
        pass
    # register route of module
    todoRoute = create_route(postgresql)
    app.register_blueprint(todoRoute, url_prefix="/todo")

    app.app_context().push()
    app.run()
    return app


if __name__ == '__main__':
    create_app()
