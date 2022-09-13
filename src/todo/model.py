from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    isDone = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return "Work: <%s>" % self.name
