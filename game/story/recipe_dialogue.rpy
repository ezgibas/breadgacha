import global_vars from '../mech/global_vars.py'

label current_recipe_dialogue(curRecipe):
    if curRecipe == allRecipes['brownie_normal']:
        call brownie_normal
    elif curRecipe == allRecipes['brownie_blondie']:
        call brownie_blondie
    elif curRecipe == allRecipes['brownie_weed']:
        call brownie_weed
    elif curRecipe == allRecipes['mooncake_normal']:
        call mooncake_normal
    elif curRecipe == allRecipes['mooncake_redbean']:
        call mooncake_redbean
    elif curRecipe == allRecipes['mooncake_blue']:
        call mooncake_blue
    elif curRecipe == allRecipes['pineapple_bun_normal']:
        call pineapple_bun_normal
    elif curRecipe == allRecipes['pineapple_bun_custard']:
        call pineapple_bun_custard
    elif curRecipe == allRecipes['pineapple_bun_pineapple']:
        call pineapple_bun_pineapple
    elif curRecipe == allRecipes['milk_bread_normal']:
        call milk_bread_normal
    elif curRecipe == allRecipes['milk_bread_strawberry']:
        call milk_bread_strawberry
    elif curRecipe == allRecipes['bread_milk']:
        call bread_milk
    elif curRecipe == allRecipes['sugar_cookie_normal']:
        call sugar_cookie_normal
    elif curRecipe == allRecipes['croissant_normal']:
        call croissant_normal
    elif curRecipe == allRecipes['croissant_chocolate']:
        call croissant_chocolate
    return

label brownie_normal:
    "Brownies are easy to make, but difficult to master."
    "You are acutely aware of this, having baked a family recipe for them numerous times; you often feel as though something is just off, whether
        that’s in the consistency, the texture, or something entirely different, but you’ve never made a bad batch, per se."

    boss "[playerName],anyone can bake a good brownie, but an excellent brownie is a baker’s white whale."
    boss  "Do not allow yourself to get hung up on perfecting what cannot be perfected."

    boss "Legend has it that the first brownie was a mistake, you know— a miracle was born out of a housewife’s misfortune,
            having forgotten to put baking powder in her chocolate cake. Brownies are a species of failure, not effort, [playerName]."

    "You heed his advice, allowing yourself to fail… perhaps too much." 
    "You are reckless with the portions of each ingredient,
        and end up adding a sprinkle of baking powder." 
    "Ironically, you end up with something far closer to a chocolate cake, although
        it ends up being a hit with your customers."

    return

label brownie_blondie:
    "Having already misperfected the brownie, the natural progression seemed obvious: it was time to 
        make her less notable cousin, the blondie. While a brownie is always good, but hard to perfect,
        a blondie is always tolerable, and hard to push beyond that point. A few customers pick them up,
        but it’s far from your greatest triumph."

    boss "[playerName], have you ever heard of Blondie? The band, not the food. My honey always loved their music… I remember going 
        to a karaoke bar with a group of friends when we were young, and her commanding that cramped little room as she sung one of their old hits…"

    boss "Ah, my apologies. As for the desserts… I suggest making something that tastes a little better."
    return 

label brownie_weed:
    "You received a strange ingredient for your brownies today… Some sort of jarred… herb, maybe?"
    "You shrug and pour it into your mix. After taste testing one, you begin to realize you can’t serve this to your customers."
    "Are your eyes red? Is your boss watching you? Do you believe in demons?"
    "EVERYONE KNOWS HOW HIGH YOU ARE. EVERYONE KNOWS HOW HIGH YOU ARE. EVERYONE KNOWS HOW HIGH YOU ARE."
    show boss_neutral
    boss "[playerName] why didn’t you serve the brownies you made today? Did something go wrong?"
    boss "I had one and thought it was perfectly fine— perhaps a bit funky, but nothing the average customer would turn their nose at."
    call weed_brownie_menu
    hide boss_neutral
    show boss_excited
    "You begin to tell him a story about a magical herb, but he quickly loses interest. You are freer than you have ever been. You spend the rest of your shift watching Family Guy YouTube compilations."
    hide boss_excited

menu weed_brownie_menu:
    "Tell him the truth":
        return
    "Tel him a lie":
        return

label mooncake_normal:
    "mooncake"
    return

label mooncake_redbean:
    "mooncake redbean"
    return

label mooncake_blue:
    "mooncake blue"
    return

label pineapple_bun_normal:
    "pineapple bun"
    return

label pineapple_bun_custard:
    "pineapple bun custard"
    return


label pineapple_bun_pineapple:
    "pineapple bun pineapple"
    return

label milk_bread_normal:
    "milk bread"
    return

label milk_bread_strawberry:
    "milk bread strawberry"
    return

label bread_milk:
    "bread milk"
    return

label sugar_cookie_normal:
    "sugar cookie"
    return

label croissant_normal:
    "Today, you muster up the courage to make a batch of croissants. The recipe is far more difficult than you imagined, and the dough you’ve laid out appears misshapen."
    show boss_neutral
    boss "[playerName], I’ve noticed you’re having difficulty making those croissants. May I teach you something, please? Remember, I’m giving you the opportunity for a world-class education for free."
    "You find difficulty in reconciling this statement with the fact you’ve been up since the crack of dawn for this unpaid apprenticeship. Anything you haven’t paid for comes with a physical and mental toll."
    boss "As you may know, I first left home when I was 18 to study abroad in Lyon, France. I arrived a week before my classes were to start, and had decided to use that extra time to explore Paris, as I had always dreamed of."
    hide boss_neutral
    show boss_sad
    boss "I quickly found myself in shock from the sheer repulsiveness of the city. Piss on the buses, drunkards on the streets, and most unseemly of all… rats running the bakeries."
    boss "Of course, this is an open secret within the culinary community, but at the time, I was an unassuming babe, just like you."
    boss " I nearly vomited when I saw one scurrying away with a croissant, only to learn that he had been in the kitchen, folding out the dough with his dainty little paws."
    hide boss_sad
    show boss_neutral
    boss "You must be the rat, [playerName].  That is the only way you will learn."
    hide boss_neutral
    "You brush off your boss’ story at first, but you find that it changed your mindset for the better. You do what you can to channel a rat you once saw in a cartoon."
    "Sooner than you know it, you’ve folded and baked a beautiful batch of croissants!"
    return

label croissant_chocolate:
    "Today the ingredients you have been left with have given you no choice but to make pan… panne… oh? Pan-o'-chocolate? Pain au chocolat."
    "You find it to be far simpler than you anticipated, especially after the herculean task of making croissants for the first time."
    "You don’t need to be the rat. You don’t even need to be the mouse!"
    show boss_happy
    "For all the desserts to be dignified with a pompous French name, this one is deceptively juvenile. It is but a croissant unclothed from the elegance of its crescent-moon shape, given arbitrary value through the little bites of chocolate nestled into it…"
    "Still, there is a certain amount of class you approached this pastry with. Good work, [playerName]."