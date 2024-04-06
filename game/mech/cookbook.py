debug = True
# An recipe in the cookbook
# name (string): name of the recipe
# count (int): how many of the recipe


class Recipe:
    # constructor
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    # equality operator
    # two recipes are the same if they have the same name
    def __eq__(self, other):
        if not isinstance(other, Recipe):
            return False
        return self.name == other.name

    # string representation of the recipe
    def __str__(self):
        return self.name


# cookbook of the player
# recipes (list of recipe): recipes in the cookbook


class Cookbook:
    # constructor
    def __init__(self, recipes):
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
        return self.recipes[recipe]

    # add an recipe to the cookbook
    # recipe (Recipe): recipe to add
    def addrecipe(self, recipe):
        self.recipes[recipe] = True
        if (debug):
            print(self)
