from marshmallow import Schema, fields


class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __repr__(self):
        return f'<Recipe(name={self.name!r})>'


class RecipeSchema(Schema):
    name = fields.Str()
    ingredients = fields.List(fields.Str())
    instructions = fields.List(fields.Str())