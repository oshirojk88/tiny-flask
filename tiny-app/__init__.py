import os

# Import all necessary junk
from flask import Flask

# Global stuff

# Initialize app
def create_app(test_config=None):
    # create and configure the app

    # app = Flask creates a Flask object instance
    app = Flask(__name__, instance_relative_config=True)

    # I haven't learned what secret_key is yet
    # DATABASE is specifying where the database 'tiny.sqlite' is
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tiny.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app
