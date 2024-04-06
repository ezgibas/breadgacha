from game.mech.cookbook import Cookbook, Recipe
from game.mech.game import Game


def init():
    global bakeryName, playerName, game, allRecipes, randomIngredients, chosenIngredients, cookbook
    bakeryName = ''
    playerName = ''

    randomIngredients = ['Egg, Flour, Butter']
    chosenIngredients = ['Sugar, Milk']


    # recipes
    allRecipes = []

    # brownies
    global brownie_normal, brownie_blondie
    brownie_normal = Recipe("Brownie", "Egg, Sugar")
    brownie_blondie = Recipe("Blondie", brownie_normal.description)
    

    # croissants
    global croissant_normal
    croissant_normal = Recipe("Croissant", "Butter, Milk")
    

    allRecipes.add() # TODO ADD ALL OF THE RECIPES TO THIS LIST

    cookbook = Cookbook()
    game = Game(cookbook, randomIngredients, chosenIngredients, allRecipes)




                                        