# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define boss = Character('Ginger Fāng')
define wife = Character('Honey Gao')

init python:
    speedrun = True
    debug = True
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
    call name_entry 
    "[bakeryName] Pâtisserie: once a critically-acclaimed bakery, now on the verge of bankruptcy."
    "You weren’t qualified to take this job, certainly. In fact, you have absolutely no formal training. In fact, it’s not even a real job."
    "For tax purposes, this is qualified as an apprenticeship, but in reality, this is a favor."

    "For you, a directionless, jobless drifter, this is a chance to get your foot in the door of a real business, albeit one that has seen far better days."
    "For Ginger Fāng, a family friend and a formerly world-renowned baker, the help you are providing will lift some of the weight off his shoulders. It’s not quite a win-win, but you can’t say you aren’t excited."
    call day_loop


label name_entry:
    if not speedrun:
        $ playerName = renpy.input("What is your name?", length=15)
        $ playerName = playerName.strip()
        $ bakeryName = renpy.input("Name your bakery", length=15)
        $ bakeryName = bakeryName.strip()
    
    if not playerName:
        $ playerName = 'Default' # TODO GIVE A CUTE DEFAULT NAME
    if not bakeryName:
        $ bakeryName = 'Default' # TODO GIVE A CUTE DEFAULT NAME
    return

label day_loop:
    "good morning"
    call bake

label bake:
    "now you are baking"
    # TODO buttons for rolling ingredients
    call screen baking_screen_1
    call screen baking_screen_2
    call show_recipe_dialogue
    
    # TODO buttons for picking ingredients
    # TODO buttons for rolling flavors (when core recipes are complete)
    # TODO buttons for baking

    jump day_loop