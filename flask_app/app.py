from flask import Flask, render_template
from config import Config
import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    @app.route('/')
    # @app.route('/home')
    def homepage():
        return render_template('homepage.html')
    @app.route('/about')
    def about():
        return render_template('about.html',title='About')

    # decorated function...route method
    @app.route('/account')
    def account():
        return render_template('account.html',title='Account')
    
    # decorated function...route method
    @app.route('/register')
    def register():
        return render_template('register.html',title='Register')

    # decorated function...route method
    @app.route('/login')
    def login():
        return render_template('login.html',title='Login') 

    # Register blueprints here

    return app
