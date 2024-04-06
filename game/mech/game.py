from game.mech.cookbook import Cookbook
import random

class Game:
    def __init__(self, cookbook: Cookbook, randomIngredients, chosenIngredients, allRecipes):
        self.cookbook = cookbook;

    def getCookbook(self):
        return self.cookbook
    
    def getCompletionPct(self):        
        return (len(self.cookbook) / len(self.allRecipes)) * 100
    
    def rollForItem(self):
        return random.choice(self.randomIngredients)
    

    


        
