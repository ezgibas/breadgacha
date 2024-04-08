

screen baking_screen_1:
    imagebutton:
        idle "images/ui/button_get_an_ingredient.png"
        action [Call("roll_ingredient1")]


label roll_ingredient1:
    $ ingredient1 = game_state.rollForItem()
    "You got [ingredient1]!"
    return

screen baking_screen_2:
    grid 1 3:
        xalign 0.75
        yalign 0.5
        text "What else do you need?"
        imagebutton:
            idle "images/ui/button_sugar.png"
            action [Call("get_recipe", ingredient1, "Sugar")]
        
        imagebutton:
            idle "images/ui/button_milk.png"
            action [Call("get_recipe", ingredient1, "Milk")]


label get_recipe(ingredient1, ingredient2_name):
    $ ingredient2 = ingredient2_name
    $ curRecipe = game_state.getRecipeFromIngredients(ingredient1, ingredient2)
    if game_state.countCompletedRecipes() >= 6:
        if game_state.countCompletedRecipes() == 6:
            "You've made a lot of recipes! You should try to make a new one." # TODO placeholder dialogue
        call screen roll_for_recipe_variation
        $ curRecipe = game_state.rollForVariation(curRecipe)
        $ recipeName = curRecipe.name
    call show_recipe(curRecipe) from _call_show_recipe
    return


label show_recipe(curRecipe):
    $ recipeName = curRecipe.name
    $ recipeImagePath = imagemap[recipeName]
    show image [recipeImagePath] at top
    "You used [ingredient1] and [ingredient2] to make a [recipeName]!"
    hide recipe_image
    call show_recipe_dialogue(curRecipe) from _call_show_recipe_dialogue

    return

label show_recipe_dialogue(recipe):
    if cookbook.hasrecipe(recipe):
        show boss neutral
        boss "[playerName], have I previously given you any advice on how to bake [recipeName]?"
        hide boss neutral
        call repeat_recipe_dialogue from _call_repeat_recipe_dialogue
    else:
        $ game_state.getCookbook().addrecipe(curRecipe)
        call current_recipe_dialogue(curRecipe) from _call_current_recipe_dialogue
    return
    

menu repeat_recipe_dialogue:
    "Yes, you already told me.":
        show boss sad
        boss "I see. I suppose you've grown tired of my stories. Perhaps one day, you will learn to lament the wisdom you once rejected."
        hide boss sad
    "Yes, but tell me again.":
        show boss happy
        boss "Ah, but of course. I've scarcely met someone quite as eager to learn as you."
        call current_recipe_dialogue(curRecipe) from _call_current_recipe_dialogue_1
        hide boss happy

screen roll_for_recipe_variation:
    imagebutton:
        idle "images/ui/button_get_a_variation.png"
        action [Return()] 