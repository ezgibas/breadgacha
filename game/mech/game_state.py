from game.mech.cookbook import Cookbook
import random

debug = True

class GameState:
    def __init__(self, cookbook: Cookbook, randomIngredients, chosenIngredients, allRecipes):
        self.cookbook = cookbook;
        self.randomIngredients = randomIngredients
        self.chosenIngredients = chosenIngredients
        self.allRecipes = allRecipes

    def getCookbook(self):
        return self.cookbook
    
    def getCompletionPct(self):        
        return (len(self.cookbook) / len(self.allRecipes)) * 100
    
    def rollForItem(self):
        return random.choice(self.randomIngredients)
    
    def getRecipeFromIngredients(self, ingredient1, ingredient2):
        if ingredient1 == 'Egg':
            if ingredient2 == 'Sugar':
                return self.allRecipes['brownie_normal']
            if ingredient2 == 'Milk':
                return self.allRecipes['pineapple_bun_normal']
            
        if ingredient1 == 'Flour':
            if ingredient2 == 'Sugar':
                return self.allRecipes['mooncake_normal']
            if ingredient2 == 'Milk':
                return self.allRecipes['milk_bread_normal']

        if ingredient1 == 'Butter':
            if ingredient2 == 'Sugar':
                return self.allRecipes['sugar_cookie_normal']
            if ingredient2 == 'Milk':
                return self.allRecipes['croissant_normal']
        
        # TODO ADD THE REST OF THE RECIPES
        else:
            return None
    

    


        
