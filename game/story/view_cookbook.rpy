python:
    curIndex = 0
    viewedItem = None

screen view_cookbook:
    window id "Cookbook":


label go_back:
    $ viewedItem = global_vars.getCookbook().getPrevRecipe(viewedItem)
    return

label go_forward:
    $ viewedItem = global_vars.getCookbook().getNextRecipe(viewedItem)
    return

