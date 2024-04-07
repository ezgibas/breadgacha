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
    $ curRecipe = game_state.getRecipeFromIngredients(ingredient1, ingredient2)
    $ recipeName = curRecipe.name
    "You used [ingredient1] and [ingredient2] to make a [recipeName]!"
    call show_recipe_dialogue(curRecipe)

    return
    # TODO roll for recipe variation

label show_recipe_dialogue(recipe):
    if cookbook.hasrecipe(recipe):
        show boss_neutral
        boss "[playerName], have I previously given you any advice on how to bake [recipeName]?"
        hide boss_neutral
        call repeat_recipe_dialogue
    else:
        $ game_state.getCookbook().addrecipe(curRecipe)
        call current_recipe_dialogue(curRecipe)
    return
    

menu repeat_recipe_dialogue:
    "Yes, you already told me.":
        show boss_sad
        boss "I see. I suppose you’ve grown tired of my stories. Perhaps one day, you will learn to lament the wisdom you once rejected."
        hide boss_sad
    "Yes, but tell me again.":
        show boss_happy
        boss "Ah, but of course. I’ve scarcely met someone quite as eager to learn as you."
        call current_recipe_dialogue(curRecipe)
        hide boss_happy
