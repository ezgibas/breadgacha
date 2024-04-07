screen baking_screen_1:
    grid 1 1:
        xalign 0.5
        yalign 0.5
        button:
            text "Get an ingredient"
            action [Call("roll_ingredient1")]


label roll_ingredient1():
    $ ingredient1 = game_state.rollForItem()
    "You got [ingredient1]!"
    return

screen baking_screen_2:
    text "What else do you need?"
    grid 1 2:
        xalign 0.5
        yalign 0.5
        button:
            text "Sugar"
            action [Call("get_recipe", ingredient1, "Sugar")]
        
        button:
            text "Milk"
            action [Call("get_recipe", ingredient1, "Milk")]


label get_recipe(ingredient1, ingredient2):
    # $ curRecipe = game_state.getRecipeFromIngredients(ingredient1, ingredient2)
    $ curRecipe = game_state.getRecipeFromIngredients("Egg", "Sugar")
    $ recipeName = curRecipe.name
    $ game_state.getCookbook().addrecipe(curRecipe)
    "You used [ingredient1] and [ingredient2] to make a [recipeName]!"
    return
    # TODO roll for recipe variation
    