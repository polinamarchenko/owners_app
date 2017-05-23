from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-blueprints'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

from project.owners.views import owners_blueprint
from project.cars.views import cars_blueprint
#register blueprints with application and define the base route URL
app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(cars_blueprint, url_prefix='/cars')

@app.route('/')
def root():
    return "Hello blueprints"
