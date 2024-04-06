debug = True
# An recipe in the cookbook
# name (string): name of the recipe
# description (string): description of the recipe


class Recipe:
    # constructor
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    # string representation of the recipe
    def __str__(self):
        return self.name


# cookbook of the player
# recipes (list of recipe): recipes in the cookbook


class Cookbook:
    # constructor
    def __init__(self):
        # hashset of recipes
        self.recipes = {}

    # string representation of the cookbook
    def __str__(self):
        result = "Cookbook: \n"
        for recipe in self.recipes:
            result += str(recipe) + "\n"
        return result

    # check if the cookbook has an recipe
    # recipe (Recipe): recipe to check
    def hasrecipe(self, recipe):
        return self.recipes[recipe.name]

    # add an recipe to the cookbook
    # recipe (Recipe): recipe to add
    def addrecipe(self, recipe):
        self.recipes[recipe.name] = True
        if (debug):
            print(self)
