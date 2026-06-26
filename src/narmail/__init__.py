from flask import Flask
from narmail.config import Config
from narmail.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from narmail import models

    return app