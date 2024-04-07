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
        brownie_weed = Recipe("Weed Brownie", brownie_normal.description)

        # mooncake
        mooncake_normal = Recipe("Mooncake", "Flour, Sugar")
        mooncake_redbean = Recipe("Red Bean Mooncake", mooncake_normal.description)
        mooncake_blue = Recipe("Blue Mooncake", mooncake_normal.description)

        # pineapple bun
        pineapple_bun_normal = Recipe("Pineapple Bun", "Egg, Milk")
        pineapple_bun_custard = Recipe("Custard Bun", pineapple_bun_normal.description)
        pineapple_bun_pineapple = Recipe("Pineapple Pineapple Bun", pineapple_bun_normal.description)


        # milk bread
        milk_bread_normal = Recipe("Milk Bread", "Flour, Milk")
        milk_bread_strawberry = Recipe("Strawberry Milk Bread", milk_bread_normal.description)
        bread_milk = Recipe("Bread Milk", milk_bread_normal.description)

        # sugar cookie
        sugar_cookie_normal = Recipe("Sugar Cookie", "Butter, Sugar")

        # croissants
        croissant_normal = Recipe("Croissant", "Butter, Milk")
        croissant_almond = Recipe("Almond Croissant", croissant_normal.description)
        croissant_chocolate = Recipe("Pain au Chocolat", croissant_normal.description)


        allRecipes['brownie_normal'] = brownie_normal
        allRecipes['brownie_blondie'] = brownie_blondie
        allRecipes['brownie_weed'] = brownie_weed
        allRecipes['mooncake_normal'] = mooncake_normal
        allRecipes['mooncake_redbean'] = mooncake_redbean
        allRecipes['mooncake_blue'] = mooncake_blue
        allRecipes['milk_bread_normal'] = milk_bread_normal
        allRecipes['milk_bread_strawberry'] = milk_bread_strawberry
        allRecipes['bread_milk'] = bread_milk
        allRecipes['sugar_cookie_normal'] = sugar_cookie_normal
        # TODO sugar cookie variants
        allRecipes['pineapple_bun_normal'] = pineapple_bun_normal
        allRecipes['pineapple_bun_custard'] = pineapple_bun_custard
        allRecipes['pineapple_bun_pineapple'] = pineapple_bun_pineapple
        allRecipes['croissant_normal'] = croissant_normal
        allRecipes['croissant_almond'] = croissant_almond
        allRecipes['croissant_chocolate'] = croissant_chocolate

        

        cookbook = Cookbook()
        game = GameState(cookbook, randomIngredients, chosenIngredients, allRecipes) 

        return bakeryName, playerName, game, allRecipes, randomIngredients, chosenIngredients, cookbook




                                        