import global_vars from '../mech/global_vars.py'

label current_recipe_dialogue(curRecipe):
    if speedrun:
        return
    if curRecipe == allRecipes['brownie_normal']:
        call brownie_normal from _call_brownie_normal
    elif curRecipe == allRecipes['brownie_blondie']:
        call brownie_blondie from _call_brownie_blondie
    elif curRecipe == allRecipes['brownie_weed']:
        call brownie_weed from _call_brownie_weed
    elif curRecipe == allRecipes['mooncake_normal']:
        call mooncake_normal from _call_mooncake_normal
    elif curRecipe == allRecipes['mooncake_redbean']:
        call mooncake_redbean from _call_mooncake_redbean
    elif curRecipe == allRecipes['mooncake_blue']:
        call mooncake_blue from _call_mooncake_blue
    elif curRecipe == allRecipes['pineapple_bun_normal']:
        call pineapple_bun_normal from _call_pineapple_bun_normal
    elif curRecipe == allRecipes['pineapple_bun_custard']:
        call pineapple_bun_custard from _call_pineapple_bun_custard
    elif curRecipe == allRecipes['pineapple_bun_pineapple']:
        call pineapple_bun_pineapple from _call_pineapple_bun_pineapple
    elif curRecipe == allRecipes['milk_bread_normal']:
        call milk_bread_normal from _call_milk_bread_normal
    elif curRecipe == allRecipes['milk_bread_strawberry']:
        call milk_bread_strawberry from _call_milk_bread_strawberry
    elif curRecipe == allRecipes['bread_milk']:
        call bread_milk from _call_bread_milk
    elif curRecipe == allRecipes['sugar_cookie_normal']:
        call sugar_cookie_normal from _call_sugar_cookie_normal
    elif curRecipe == allRecipes['croissant_normal']:
        call croissant_normal from _call_croissant_normal
    elif curRecipe == allRecipes['croissant_chocolate']:
        call croissant_chocolate from _call_croissant_chocolate
    return

label brownie_normal:
    "Brownies are easy to make, but difficult to master."
    "You are acutely aware of this, having baked a family recipe for them numerous times; you often feel as though something is just off, whether
        that's in the consistency, the texture, or something entirely different, but you've never made a bad batch, per se."

    show boss neutral
    boss "[playerName],anyone can bake a good brownie, but an excellent brownie is a baker's white whale."
    boss  "Do not allow yourself to get hung up on perfecting what cannot be perfected."

    boss "Legend has it that the first brownie was a mistake, you know— a miracle was born out of a housewife's misfortune,
            having forgotten to put baking powder in her chocolate cake. Brownies are a species of failure, not effort, [playerName]."
    hide boss neutral
    "You heed his advice, allowing yourself to fail… perhaps too much." 
    "You are reckless with the portions of each ingredient,
        and end up adding a sprinkle of baking powder." 
    "Ironically, you end up with something far closer to a chocolate cake, although
        it ends up being a hit with your customers."

    return

label brownie_blondie:
    "Having already misperfected the brownie, the natural progression seemed obvious: it was time to 
        make her less notable cousin, the blondie."
    "While a brownie is always good, but hard to perfect,
        a blondie is always tolerable, and hard to push beyond that point."
    "A few customers pick them up,
        but it's far from your greatest triumph."

    show boss neutral
    boss "[playerName], have you ever heard of Blondie? The band, not the food. My honey always loved their music… I remember going 
        to a karaoke bar with a group of friends when we were young, and her commanding that cramped little room as she sung one of their old hits…"

    hide boss neutral
    show boss sad
    boss "Ah, my apologies. As for the desserts… I suggest making something that tastes a little better."
    hide boss sad
    return 

label brownie_weed:
    "You received a strange ingredient for your brownies today… Some sort of jarred… herb, maybe?"
    "You shrug and pour it into your mix. After taste testing one, you begin to realize you can't serve this to your customers."
    "Are your eyes red? Is your boss watching you? Do you believe in demons?"
    "EVERYONE KNOWS HOW HIGH YOU ARE. EVERYONE KNOWS HOW HIGH YOU ARE. EVERYONE KNOWS HOW HIGH YOU ARE."
    show boss neutral
    boss "[playerName] why didn't you serve the brownies you made today? Did something go wrong?"
    boss "I had one and thought it was perfectly fine— perhaps a bit funky, but nothing the average customer would turn their nose at."
    call weed_brownie_menu from _call_weed_brownie_menu
    hide boss neutral
    show boss excited
    "You begin to tell him a story about a magical herb, but he quickly loses interest. You are freer than you have ever been. You spend the rest of your shift watching Family Guy YouTube compilations."
    hide boss excited
    return

menu weed_brownie_menu:
    "Tell him the truth":
        return
    "Tel him a lie":
        return

label mooncake_normal:
    "Your ingredients today have left you with a dreadfully daunting process ahead of you: making mooncakes. A part of you is terrified, familiar with all the complex patterns sculpted into them."
    "You imagine structuring an ornate design onto the top of the cake. You have an exacto-knife prepared and everything."
    show boss neutral
    boss "Ah, [playerName], is this your first time making mooncakes? The mold is in the upper cabinet next to the sink, middle drawer."
    "You run your finger through the drawers to reach the one you're looking for, and pull out the molds; their complexity is marvelous. There are only three different kinds, marked mung bean, red bean, and lotus. You opt for mung, today. Getting the exact measurements is about as difficult as you imagine, but you feel a sense of pride as you cool them to be served tomorrow."
    boss "You know, [playerName], as a child, I would only eat mooncakes once a year, during the Mid-Autumn festival. The first year that me and my honey were together, I baked some for our own local festival." 
    boss "She told me it was the best thing I had ever baked— which, I was, and still am, skeptical to believe, but ever since then, I decided to bake them year-round…"
    boss  "Er, anyway, good work, [playerName]. I hope these mooncakes can bring our customers the same joy they once brought me…"
    hide boss neutral
    return

label mooncake_redbean:
    "Having gained some experience in making the mooncakes before this, you now feel confident enough to give it another shot."
    "This time, you go for the red bean filling, which is far more familiar to you. A mother comes in with her starry-eyed son, who begs her for a mooncake. She tells him that not only are they out of season, they're more expensive than a regular tart. She picks up a loaf of bread and orders him a single sugar cookie. You slip a mooncake into the bag."
    show boss neutral
    boss "You know, [playerName], you ought to be careful how often you give out free samples. If you let it become a habit, we'll run out of pastries far before closing!"
    "Ginger is in the middle of chewing one of your mooncakes as he says this."
    boss "Don't look at me like that. If you should ever be so lucky to become a world-renowned baker, you too will be allowed to eat away your feelings… and your inventory."
    hide boss neutral
    return

label mooncake_blue:
    "You receive a strange ingredient for the mooncakes you’re making today— a strikingly blue lotus flower." 
    "You incorporate it into the lotus filling; an azure paste, sparkling under the kitchen’s fluorescent light. You use blue food coloring to make the exterior of the pastry match the inside… blue mooncakes."
    show boss neutral
    boss "You know, my honey used to keep track of the cycle of the moon. She would insist that we go out on evenings when the moon was full, marking supermoons and eclipses on her calendar. One night she told me of a blue moon, so we spent the night under the stars…"
    show boss sad
    boss  "I was disappointed to learn the moon would not actually appear blue. If anything, it looked exactly the same as usual. She laughed at me when I confessed this to her, but that was enough to make my ignorance feel worthwhile…"
    boss "I’m sorry, [playerName]. I hope that soon you can find someone who would give you the moon, too."
    hide boss sad
  
    return

label pineapple_bun_normal:
    "With the ingredients you’ve selected for the day, you’ve decided to bake some pineapple buns— which, despite the name’s implication, do not contain pineapple, only imitating the look of them, though perhaps some day they would…"
    show boss neutral
    boss "[playerName], I don’t believe I’ve told you the story of the first time I made pineapple buns. Deep in the frigid months of winter, both of my parents had come down with a nasty cold."
    boss  "My grandmother, rather than worrying about cheering my own parents up, wanted to do something to make me feel better for the lack of focus they could give me— although, now that I think about it, I suspect it was a way to keep me busy more than anything."
    boss  "She taught me how to make pineapple buns, using a shortcut recipe so that we could make extra batches… I still have it in my own cookbook, perhaps you could put it in yours?"
    "The pineapple buns come out slightly misshapen, the diagonal hatching on them not entirely consistent, but you figure that adds to their charm. There is nothing more human than imperfection, and this batch certainly demonstrates that."
    hide boss neutral
    return

label pineapple_bun_custard:
    "Your ingredients have left you inclined to make pineapple buns yet again, this time with a custard cream filling."
    "Custard always makes you think of those British children’s television mascots, standing in technicolor at their amazonian height, crowded around a machine pumping out pepto-bismol toned custard."
    "You think of Tinky Winky, the purple titan, clutching his red Valentino purse around his limp wrist."
    "You think of how they made him into a martyr. A diva who danced too close to the sun."
    show boss neutral
    boss "I was always partial to Po."
    boss "What, I have nieces and nephews! They loved that show."
    "Disregarding Ginger’s comments, you dedicate the custard cream pineapple bun in Tinky Winky’s honor. All of those customers indulging in its saccharine pleasure remain oblivious to the impact he had."
    return


label pineapple_bun_pineapple:
    "You’ve decided that today is one of those rare days where you feel experimental." 
    "You aren’t making normal pineapple buns today— you are making pineapple-flavored, pineapple-filled, pineapple buns. Pineapple pineapple buns!"
    show boss neutral
    boss "[playerName], I believe that title may be misleading. If the dough has pineapple, the filling has pineapple, and it is shaped into a pineapple bun, ‘pineapple pineapple’ may seem like it cancels out."
    boss "Thus, I believe the most honest course of action would be to sell them as ‘pineapple pineapple pineapple buns’. That way there’s no confusion.”"
    "You feel you’re in no position to defy orders from the boss, but you quickly suspect that the triple usage of pineapple has begun to confuse customers."
    "Each one of them asks you to explain it about three times before ordering— for the sake of clarity, you note them down in your cookbook as ‘triple pineapple buns’."

    return

label milk_bread_normal:
    "Your selection of ingredients today encourages you to make milk bread— unfortunately, you have no idea what that entails."
    "Ginger walks in on you soaking a bag of store-bought sandwich bread in a bowl of milk."
    show boss neutral
    boss "[playerName], what are you doing?"
    call milk_bread_menu from _call_milk_bread_menu
    boss "Now, there are a number of methods to make milk bread, even if I'm not familiar with the one you were trying… "
    boss "The way I've always made it is using tangzhong, a roux that we boil in milk in order to soften the bread. Now, luckily, I already have some dough prepared…"
    boss "I trust that you can work out how to bake it from here."
    "Most of the work has already been done for you, but you liked your milk bread technique far more… Perhaps you'll have to revisit it in the future. The public aren't quite ready for bread milk."
    hide boss neutral
    return

menu milk_bread_menu:
    "What does it look like I'm doing? I'm making MILK BREAD.":
        boss " I see… I have to admit, I'm not familiar with your technique. While it intrigues me, I don't believe now is the time for experimentation."
        return
    "...":
        "Ginger snatches the bowl off of the counter, dumping it all down the drain. The bag of what had been perfectly good sandwich bread is devoured by the garbage disposal before you have time to react."
        return
        boss "Now, where were we…"

label milk_bread_strawberry:
    "milk bread strawberry"
    return

label bread_milk:
    "They called it crazy. They called it sacrilege. You were a false prophet, a reprobate, a heathen in the face of the laws of baking."
    "But now, bread milk wasn't just a pipe dream. The palms of your hands could wrap around a plastic cup, filled with milk and little crumbs of soggy sandwich bread. You could almost cry. Almost."
    show boss neutral
    boss "I hate to say it, [playerName]... as disgusting as it sounds, I think you were onto something with “bread milk”."
    boss "I suggest you add it to your cookbook. The world deserves to know of this delicacy. Just don't let it get to your head."
    hide boss neutral
    "For a moment, it does. Bread milk is not the type of thing that could be dreamt up by man. This was the work of a future god, or perhaps someone chosen by one."
    "Although perhaps it was all a fever dream; the bread milk you made disappeared, as did any evidence it ever existed. You still choose to document this. Bread milk will not die in vain."
    return

label sugar_cookie_normal:
    "Today you have selected the ingredients for sugar cookies, and this is the first time you find yourself confident enough to cook without a guide."
    "Their appeal lies in their simplicity, both for the consumer and the producer… it's best not to overcomplicate things. You find that they don't sell particularly well, but considering how little effort and resources they require, you still make a reasonable profit."
    show boss happy
    boss "There is an honest charm to the sugar cookie, [playerName]. Although my honey was a critic, she was no baker— the few times she would bake, she would always come up with a batch of sugar cookies."
    boss "As a professional, she was, of course, her own worst critic. She found that they were too dry, too crumbly, lacking a certain je ne sais quoi, but for me, they were my favorite cookies I'd ever tasted."
    "Ginger's lips begin to form into his habitual frown."
    hide boss happy
    show boss sad
    boss "Ahem. You did a good job with these cookies, but they are a bit too dry. Try adding something to give them more panache in the future."
    hide boss sad
    return

label sugar_cookie_pink:
    "Today you’ve been given the ingredients to make sugar cookies again, but a part of you yearns for something more primal; these will not be artisanal bakery sugar cookies, but an imitation of sterile, store-bought sugar cookies, frosting and all."
    "You perfect the recipe to have a plasticine texture, tasting uncannily more like the idea of a cookie than the actual thing. The people love it. Ginger does not."
    show boss neutral
    boss "This is a disgrace! This is an obliteration of the sanctity of the sugar cookie! We are not a bloodthirsty American supermarket chain, we are an honest bakery for honest people. It is a form of deception to call these cookies."
    "You watch as he berates your work, waiting for him to actually try one."
    boss "Hmm… these aren’t the worst thing I’ve tasted. You’ve done the best that you can for something like this, just don’t do it again in the future. We have a reputation to uphold."
    "When he thinks you can’t see him, Ginger comes back to grab a couple more sugar cookies back with him. Regardless of the reprimand you faced earlier, you think this was a success."
    hide boss neutral
    return

label sugar_cookie_birthday:
    "Something calls to you to make your sugar cookies festive today. It could be your birthday. It could be Ginger’s."
    "Hell, it could be Honey’s— or maybe a customer will come by to celebrate, instinctively knowing you did this just for them. Much to think about… Much to celebrate…"
    show boss neutral
    boss "Ah, [playerName], we need to evacuate the building. There’s been a gas leak."
    "Ginger is always so modest! It really must be the old coot’s birthday! You sing your way out of the bakery, prismatically sprinkled cookies in hand."
    "It turns out the driver from the gas company was having a rough day— it was his birthday, and everyone else had forgotten! Lucky him, you still had the cookies on you, although he didn’t particularly like them… Oh, well! You’ll have leftovers later."
    hide boss neutral
    return

label croissant_normal:
    "Today, you muster up the courage to make a batch of croissants. The recipe is far more difficult than you imagined, and the dough you've laid out appears misshapen."
    show boss neutral
    boss "[playerName], I've noticed you're having difficulty making those croissants. May I teach you something, please? Remember, I'm giving you the opportunity for a world-class education for free."
    "You find difficulty in reconciling this statement with the fact you've been up since the crack of dawn for this unpaid apprenticeship. Anything you haven't paid for comes with a physical and mental toll."
    boss "As you may know, I first left home when I was 18 to study abroad in Lyon, France. I arrived a week before my classes were to start, and had decided to use that extra time to explore Paris, as I had always dreamed of."
    hide boss neutral
    show boss sad
    boss "I quickly found myself in shock from the sheer repulsiveness of the city. Piss on the buses, drunkards on the streets, and most unseemly of all… rats running the bakeries."
    boss "Of course, this is an open secret within the culinary community, but at the time, I was an unassuming babe, just like you."
    boss " I nearly vomited when I saw one scurrying away with a croissant, only to learn that he had been in the kitchen, folding out the dough with his dainty little paws."
    hide boss sad
    show boss neutral
    boss "You must be the rat, [playerName].  That is the only way you will learn."
    hide boss neutral
    "You brush off your boss' story at first, but you find that it changed your mindset for the better. You do what you can to channel a rat you once saw in a cartoon."
    "Sooner than you know it, you've folded and baked a beautiful batch of croissants!"
    return

label croissant_chocolate:
    "Today the ingredients you have been left with have given you no choice but to make pan… panne… oh? Pan-o'-chocolate? Pain au chocolat."
    "You find it to be far simpler than you anticipated, especially after the herculean task of making croissants for the first time."
    "You don't need to be the rat. You don't even need to be the mouse!"
    show boss happy
    "For all the desserts to be dignified with a pompous French name, this one is deceptively juvenile. It is but a croissant unclothed from the elegance of its crescent-moon shape, given arbitrary value through the little bites of chocolate nestled into it…"
    "Still, there is a certain amount of class you approached this pastry with. Good work, [playerName]."
    hide boss happy dissolve