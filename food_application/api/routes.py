from flask import Blueprint, request, jsonify
from food_application.helpers import token_required
from food_application.models import db, Recipe, recipe_schema, recipes_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
@token_required
def getdata(our_user):
    return {'some': 'value'}


# #Create recipe Endpoint
@api.route('/recipes', methods = ["POST"])
@token_required
def create_recipe(our_user):
    
    title = request.json['title']
    image = request.json['image']
    summary = request.json['summary']
    ingredients = request.json['ingredients']
    instructions = request.json['instructions']
    date_created= request.json['date_created']
       
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    recipe = Recipe(title, image, summary, ingredients, instructions, date_created, user_token = user_token )

    db.session.add(recipe)
    db.session.commit()

    response = recipe_schema.dump(recipe)

    return jsonify(response)

#Retrieve(READ) all recipes recipes
@api.route('/recipes', methods = ['GET'])
@token_required
def get_recipes(our_user):
    owner = our_user.token
    recipes = Recipe.query.filter_by(user_token = owner).all()
    response = recipes_schema.dump(recipes)

    return jsonify(response)

#retrieve one sigular individual lonely recipe

@api.route('/recipes/<id>', methods = ['GET'])
@token_required
def get_recipe(our_user, id):    
    if id:
        recipe = Recipe.query.get(id)
        response = recipe_schema.dump(recipe)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Id equired'}), 401
    
#update recipe by id
@api.route('/recipes/<id>', methods = ["PUT"])
@token_required
def update_recipe(our_user, id): 
    recipe = Recipe.query.get(id)   
    recipe.title = request.json['title']
    recipe.image = request.json['image']
    recipe.ingredients = request.json['ingredients']
    recipe.instructions= request.json['instructions']
    recipe.date_created = request.json[' date_created']
    
    
    recipe.user_token = our_user.token  

    db.session.commit()

    response = recipe_schema.dump(recipe)

    return jsonify(response)
#Delete recipe  by id
@api.route('/recipes/<id>', methods = ['DELETE'])
@token_required
def delete_recipes(our_user, id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()

    response = recipe_schema.dump(recipe)
    return jsonify(response)
