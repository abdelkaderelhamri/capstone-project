import os
from dotenv import load_dotenv
basedir= os.path.abspath(os.path.dirname(__file__))
#give access

load_dotenv(os.path.join(basedir, '.env'))
class Config():
    """ set configuration for  the flask app
    using environment variables where available
    otherwise create the config variable if not done already"""
    FLASK_APP=os.environ.get('FLASK_APP')
    FLASK_ENV=os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get("SECRET_KEY") or "nana nana boo boo youll never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turns of messages from sqlalchemy regarding updates to our db 