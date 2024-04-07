debug = True
# An recipe in the cookbook
# name (string): name of the recipe
# description (string): description of the recipe


class Recipe:
    # constructor
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

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
    def __init__(self):
        # hashset of recipes
        self.recipes = {}

    # string representation of the cookbook
    def __str__(self):
        result = "Cookbook: \n"
        for recipe in self.recipes:
            result += str(recipe) + "\n"
        return result
    
    def __len__(self):
        return len(self.recipes)

    # check if the cookbook has an recipe
    # recipe (Recipe): recipe to check
    def hasrecipe(self, recipe):
        return recipe.name in self.recipes.keys()

    # add an recipe to the cookbook
    # recipe (Recipe): recipe to add
    def addrecipe(self, recipe):
        self.recipes[recipe.name] = True
        if (debug):
            print(self)

    def getPrevRecipe(self, recipe):
        indexOfRecipe = self.recipes.keys().index(recipe.name)
        if indexOfRecipe > 0:
            nameOfPrev = self.recipes.keys()[indexOfRecipe - 1]
            return self.recipes[nameOfPrev]
        else:
            return recipe
        
    def getNextRecipe(self, recipe):
        indexOfRecipe = self.recipes.keys().index(recipe.name)
        if indexOfRecipe < len(self.recipes.keys()) - 1:
            nameOfNext = self.recipes.keys()[indexOfRecipe + 1]
            return self.recipes[nameOfNext]
        else:
            return recipe
