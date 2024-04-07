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
    
    def countCompletedRecipes(self):
        return len(self.cookbook)
    
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
        
        else:
            return None
        
    def getVariantsOfRecipe(self, recipe):
        if recipe == self.allRecipes['brownie_normal']:
            return [self.allRecipes['brownie_blondie'], self.allRecipes['brownie_weed']]
        if recipe == self.allRecipes['mooncake_normal']:
            return [self.allRecipes['mooncake_redbean'], self.allRecipes['mooncake_blue']]
        if recipe == self.allRecipes['pineapple_bun_normal']:
            return [self.allRecipes['pineapple_bun_custard'], self.allRecipes['pineapple_bun_pineapple']]
        if recipe == self.allRecipes['milk_bread_normal']:
            return [self.allRecipes['milk_bread_strawberry'], self.allRecipes['bread_milk']]
        if recipe == self.allRecipes['sugar_cookie_normal']:
            return [self.allRecipes['sugar_cookie_pink'], self.allRecipes['sugar_cookie_birthday']]
        if recipe == self.allRecipes['croissant_normal']:
            return [self.allRecipes['croissant_almond'], self.allRecipes['croissant_chocolate']]
        
    def rollForVariation(self, recipe):
        return random.choice(self.getVariantsOfRecipe(recipe))
    
    def getRecipeByIdx(self, idx):
        recipeName = list(self.allRecipes.keys())[idx]
        return self.allRecipes[recipeName]

    def getPrevRecipe(self, idx):
        if idx > 0:
            return self.getRecipeByIdx(idx - 1)
        else:
            return self.getRecipeByIdx(idx)
        
    def getNextRecipe(self, idx):
        if idx < len(self.allRecipes) - 1:
            return self.getRecipeByIdx(idx + 1)
        else:
            return self.getRecipeByIdx(idx)

    


        
