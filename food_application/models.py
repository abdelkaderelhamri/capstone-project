from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Secrets Module (Given by Python)
import secrets

from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
#import flask login

login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    # recipe = db.relationship('Recipe', backref = 'owner', lazy = True)

    def __init__(self,email,username,first_name = '', last_name = '', id = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify
        self.username=username
        self.token = self.set_token(24)

    def set_token(self,length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'
   

class Recipe(db.Model):
    id = db.Column(db.String, primary_key = True)
    title = db.Column(db.String)
    image = None
    summary = db.Column(db.String)
    ingredients = db.Column(db.String)
    instructions = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)
    def __init__(self, id, title, image, summary, ingredients, instructions,user_token):
        self.id = id
        self.title = title
        self.image = image
        self.summary = summary
        self.ingredients = ingredients
        self.instructions = instructions
        
        self.user_token = user_token
    def set_id(self):
        return str(uuid.uuid4())
    def __repr__(self):
        return f"Recipe {self.name} has been added to the database!"
class RecipeSchema(ma.Schema): 
    class Meta:
        fields = ['id', 'title', 'image', 'summary', 'ingredients', ' instructions', 
                  'date_created ']
recipe_schema = RecipeSchema()
recipes_schema =RecipeSchema(many = True)

        