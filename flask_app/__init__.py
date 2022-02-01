from flask import Flask
from flask_app.routes import main
app = Flask(__name__)
app.register_blueprint(main)