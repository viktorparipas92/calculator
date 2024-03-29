import os
from flask import Flask

from . import db, calculate


# Application factory function (shall be named create_app or make_app)
# Alternatively set env variable FLASK_APP to "calculator:my_function('dev')"
def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'calculator.sqlite'),
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    # ensure that instance folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    app.register_blueprint(calculate.bp)
    
    return app
