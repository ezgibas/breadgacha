from game.mech.cookbook import Cookbook, Recipe
from game.mech.game_state import GameState


class Variables:
    def __init__(self):
        # nothing
        return

    def getVariables(self):
        bakeryName = ''
        playerName = ''

        randomIngredients = ['Egg', 'Flour', 'Butter']
        chosenIngredients = ['Sugar, Milk']


        # recipes
        allRecipes = {}

        # brownies
        brownie_normal = Recipe("Brownie", "Egg, Sugar")
        brownie_blondie = Recipe("Blondie", brownie_normal.description)

        # mooncake
        mooncake_normal = Recipe("Mooncake", "Flour, Sugar")

        # pineapple bun
        pineapple_bun_normal = Recipe("Pineapple Bun", "Egg, Milk")

        # milk bread
        milk_bread_normal = Recipe("Milk Bread", "Flour, Milk")

        # sugar cookie
        sugar_cookie_normal = Recipe("Sugar Cookie", "Butter, Sugar")

        # croissants
        croissant_normal = Recipe("Croissant", "Butter, Milk")


        allRecipes['brownie_normal'] = brownie_normal
        allRecipes['brownie_blondie'] = brownie_blondie
        allRecipes['croissant_normal'] = croissant_normal
        allRecipes['mooncake_normal'] = mooncake_normal
        allRecipes['milk_bread_normal'] = milk_bread_normal
        allRecipes['sugar_cookie_normal'] = sugar_cookie_normal
        allRecipes['pineapple_bun_normal'] = pineapple_bun_normal
        

        cookbook = Cookbook()
        game = GameState(cookbook, randomIngredients, chosenIngredients, allRecipes) 

        return bakeryName, playerName, game, allRecipes, randomIngredients, chosenIngredients, cookbook




                                        