from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from food_application.forms import RecipeForm
from food_application.models import Recipe, db





site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    print("show something in the terminal")
    return render_template('index.html')
@site.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    my_recipe = RecipeForm()

    try:
        if request.method == "POST" and my_recipe.validate_on_submit():
            title = my_recipe.title.data
            image = my_recipe.image.data
            summary=my_recipe.summary.data
            ingredients = my_recipe.ingredients.data
            instructions = my_recipe.instructions.data
            date_created = my_recipe.date_created.data
            user_token=current_user.token
           
           

            recipe = Recipe(title, image,summary, ingredients, instructions, date_created, user_token)

            db.session.add(recipe)
            db.session.commit()

            return redirect(url_for('site.profile'))
    except:
        raise Exception("Recipe not created, please check your form and try again!")
    
    current_user_token = current_user.token

    recipes = Recipe.query.filter_by(user_token=current_user_token)

    
    return render_template('profile.html', form=my_recipe, recipes = recipes)


