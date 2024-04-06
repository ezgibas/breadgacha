# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define boss = Character('Ginger Fāng')
define wife = Character('Honey Gao')

python:
    global_vars.init()
    # ask for player's name
    playerName = renpy.input("What is your name?", length=15)
    playerName = playerName.strip()
    if not playerName:
        playerName = 'Default' # TODO GIVE A CUTE DEFAULT NAME
    # ask for bakery name
    bakeryName = renpy.input("Name your bakery", length=15) # TODO CHANGE THIS PROMPT (or move it somewhere else    )
    bakeryName = bakeryName.strip()
    if not bakeryName:
        bakeryName = 'Default' # TODO GIVE A CUTE DEFAULT NAME

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
