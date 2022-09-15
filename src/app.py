import sys

from dynaconf import FlaskDynaconf
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.infa.database.Postgresql import Postgresql
from src.infa.logging.Logging import Logging
from src.todo.route import create_route


def create_app():
    app = FlaskAPI(__name__)
    # config
    FlaskDynaconf(app)

    db = SQLAlchemy()
    migrate = Migrate()
    # create Logger
    with app.app_context():
        logging = Logging()

        if (
            app.config["DATABASE_TYPE"] == "postgresql"
            and app.config["SQLALCHEMY_DATABASE_URI"] is not None
        ):
            postgresql = Postgresql(db=db)
            try:
                logging.warning(app.config["SQLALCHEMY_DATABASE_URI"])
                postgresql.init_db(app=app)
                migrate.init_app(app=app, db=db)
            except Exception as error:
                logging.critical(message=error)
                sys.exit(-1)
            else:
                logging.info(message="Connect to database successfully")
        else:
            logging.critical(
                message="DATABASE_TYPE or DATABASE_URI isn't configured")
            sys.exit(-1)

    # register route of module
    todoRoute = create_route(postgresql, logging)
    app.register_blueprint(todoRoute, url_prefix="/todo")

    app.app_context().push()
    app.run()
    return app


if __name__ == "__main__":
    create_app()
