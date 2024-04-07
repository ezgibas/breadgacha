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
        brownie_weed = Recipe("Space Brownie", brownie_normal.description)

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
        sugar_cookie_pink = Recipe("Pink Sugar Cookie", sugar_cookie_normal.description)
        sugar_cookie_birthday = Recipe("Sugar Cookie with Birthday Sprinkles", sugar_cookie_normal.description)

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
        allRecipes['sugar_cookie_pink'] = sugar_cookie_pink
        allRecipes['sugar_cookie_birthday'] = sugar_cookie_birthday
        allRecipes['pineapple_bun_normal'] = pineapple_bun_normal
        allRecipes['pineapple_bun_custard'] = pineapple_bun_custard
        allRecipes['pineapple_bun_pineapple'] = pineapple_bun_pineapple
        allRecipes['croissant_normal'] = croissant_normal
        allRecipes['croissant_almond'] = croissant_almond
        allRecipes['croissant_chocolate'] = croissant_chocolate

        imagemap = {}

        imagemap['Bread Milk'] = "images/food/bread_milk.png"
        imagemap['Strawberry Milk Bread'] = "images/food/bread_strawberry.png"
        imagemap['Milk Bread'] = "images/food/bread_plain.png"
        imagemap['Pain au Chocolat'] = "images/food/croissant_chocolat.png"
        imagemap['Almond Croissant'] = "images/food/croissant_almond.png"
        imagemap['Croissant'] = "images/food/croissant_plain.png"
        imagemap['Sugar Cookie with Birthday Sprinkles'] = "images/food/cookie_birthday.png"
        imagemap['Pink Sugar Cookie'] = "images/food/cookie_pink.png"
        imagemap['Sugar Cookie'] = "images/food/cookie_plain.png"
        imagemap['Pineapple Pineapple Bun'] = "images/food/pineapple_pineapple.png"
        imagemap['Custard Bun'] = "images/food/pineapple_cream.png"
        imagemap['Pineapple Bun'] = "images/food/pineapple_plain.png"
        imagemap['Blue Mooncake'] = "images/food/mooncake_blue.png"
        imagemap['Red Bean Mooncake'] = "images/food/mooncake_red.png"
        imagemap['Mooncake'] = "images/food/mooncake_plain.png"
        imagemap['Space Brownie'] = "images/food/brownie_weed.png"
        imagemap['Blondie'] = "images/food/brownie_blondie.png"
        imagemap['Brownie'] = "images/food/brownie_plain.png"

        # image tart normal = "images/food/tart_plain.png"

        game = GameState(Cookbook(), randomIngredients, chosenIngredients, allRecipes) 

        return bakeryName, playerName, game, allRecipes, randomIngredients, chosenIngredients, imagemap




                                        