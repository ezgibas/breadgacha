# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define boss = Character('Ginger Fāng')
define wife = Character('Honey Gao')

init python:
    from game.mech.global_vars import Variables
    global_vars = Variables()
    bakeryName, playerName, game_state, allRecipes, randomIngredients, chosenIngredients, cookbook = global_vars.getVariables()
    curRecipe = None
    # game.mech.global_vars.init()
    # ask for player's name
    # playerName = renpy.input("What is your name?", length=15)
    # playerName = playerName.strip()
    # if not playerName:
    #     playerName = 'Default' # TODO GIVE A CUTE DEFAULT NAME
    # # ask for bakery name
    # bakeryName = renpy.input("Name your bakery", length=15) # TODO CHANGE THIS PROMPT (or move it somewhere else    )
    # bakeryName = bakeryName.strip()
    # if not bakeryName:
    #     bakeryName = 'Default' # TODO GIVE A CUTE DEFAULT NAME

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    call day_loop

label day_loop:
    "good morning" # TODO
    jump bake


label bake:
    "now you are baking"
    # TODO buttons for rolling ingredients
    call screen baking_screen_1
    call screen baking_screen_2
    jump show_recipe_dialogue
    
    # TODO buttons for picking ingredients
    # TODO buttons for rolling flavors (when core recipes are complete)
    # TODO buttons for baking

    jump day_loop