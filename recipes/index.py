import json
from flask import Flask, jsonify, request

from recipes.model.recipe import Recipe, RecipeSchema

app = Flask(__name__)

with open('../data/data.json', 'r+') as jf:
    data = json.load(jf)


@app.route('/recipes/')
def get_recipes():
    recipe_names = {
        "recipeNames": [x['name'] for x in data['recipes']]
    }
    return jsonify(recipe_names), 200


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)