from flask import Flask, g
from dynaconf import FlaskDynaconf
from infa.database.postgresql import Postgresql
from src.todo.transports.route import todoRoute

app = Flask(__name__)
# config
FlaskDynaconf(app)

# register route of module
app.register_blueprint(todoRoute, url_prefix="/todo")


# connect to database
@app.before_request
def init_db():
    if app.config["DATABASE_TYPE"] == "postgresql":
        g.db = Postgresql().connect()
    else:
        g.db = Postgresql().connect()
    return g.db


# disconnect database
@app.teardown_request
def teardown_request(exception):
    if "db" not in g:
        raise TypeError("Database wasn't existed")
    else:
        pass


@app.get("/")
def helloworld():
    return "hi!"


# print(app.config)
