init python:
    curIndex = 0
    viewedItem = game_state.getRecipeByIdx(curIndex)

image cookbook = "../images/cookbook/cookbook.png"
image arr_left = "../images/cookbook/arrow_left.png"
image arr_right = "../images/cookbook/arrow_right.png"

screen cookbook_button:
    grid 1 1:
        xalign 0.1
        yalign 0.1
        textbutton "Cookbook" action Show("view_cookbook") xalign 0.5

screen view_cookbook:
    window id "Cookbook":
        grid 3 1:
            vbox:
                imagebutton:
                    idle "../images/cookbook/arrow_left.png"
                    action [Call("go_back")]
            vbox:
                image "cookbook"
                text "[viewedItem.name]"
                text "[viewedItem.description]"
            imagebutton:
                idle "arr_right"
                action [Call("go_forward")]
            
label go_back:
    $ viewedItem = game_state.getPrevRecipe(curIndex)
    if curIndex > 0:
        $ curIndex -= 1
    return

label go_forward:
    $ viewedItem = game_state.getNextRecipe(curIndex)
    if curIndex < len(game_state.recipes) - 1:
        $ curIndex += 1
    return

