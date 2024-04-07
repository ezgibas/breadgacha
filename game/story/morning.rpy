

label morning_scenes:
    if game_state.countCompletedRecipes() == 12:
        call complete_12
    else:
        "good morning"

    return

label complete_12:
    $ where_ginger_menu = True
    "You find your way into the bakery early in the morning, only to realize that Ginger is not there."
    "You try calling his name and search through the kitchen, but you cannot find him. As you're still searching, you hear a knock on the door."
    wife "Let me in, [playerName]. I know you can hear me!"
    "Part of you wants to leave her outside… the store hasn't even opened yet! You imagine the look on her face only growing more sour as she waits outside."
    "You imagine that eventually, she would have to give up, right…? That may not be entirely realistic. You unlock the door, having decided not to wait around and find out."
    show wife neutral
    wife "Finally, I was scared I was going to freeze to death out there. Now, where's Ginger?"
    "You are caught off guard by the question. Stammering and staring, you tell her…"
    $ show_kitchen = True
    $ show_bathroom = False
    $ show_behind_you = False
    jump where_ginger_menu

label complete_12_part2:
    show wife neutral 
    wife "Hmm… how unlike him. I realize it's different than my typical appointments, but I did schedule this time to speak to him… Peh, what a coward."
    "Honey pulls out a clipboard and a ballpoint pen, tapping at the end of it erratically."
    wife "I apologize for his insolence, [playerName]. In the meantime, I'm still going to need to review one of your pastries."
    wife " I realize these [curRecipe] aren't fresh, but I'll take that into consideration in my review. Now, would you please find me a plate?"
    "As much as you find this to be an unusual request, you head to a cabinet of porcelain dishware in the kitchen."
    "You use these for the rare occasions where the [bakeryName] Pâtisserie is booked for catering. Honey laughs to herself as you set it down in front of her."
    wife "Just as I suspected. I don't know if this is him being a romantic, a cynic, or a cheapskate. Now, the [curRecipe]."
    "Unresponsive to her assumed non-sequitur, you hand her the [curRecipe], slightly stale from the day before."
    # hide wife neutral
    show wife shock
    wife "Hmm… I have to say, [playerName]. I wasn't expecting this. You've improved as a baker, you know."
    wife "An old dog can't learn new tricks, but they may teach a pup their own. You have enormous potential, [playerName]. My advice? Don't waste it here."
    show wife neutral
    call honey_advice_menu
    wife "Regardless, you shouldn't marry yourself to the work. Only keep doing this if you're sure it's what you really want. Take it from me."
    "For a moment, you recognize an ounce of compassion in Honey's tone. She is far less fulfilled than you suspected."
    wife "I wasn't always like this, you know. Ginger was always so saccharine, even if he's mellowed out now. He was always too afraid to hurt someone's feelings, to let someone go… "
    wife "He never argued with me, never insulted me, but he knew his way around subtlety. If he was the prince of the culinary world, I was the dragon guarding his tower— no, I was the tower."
    wife "He is the promise of the stained-window, ornate and fragile."
    "..."
    wife "I apologize if this is overwhelming, [playerName]. Just… do not mistake fragility for kindness. Know that before you build your life around this world."
    "You hear the door open up behind you."
    hide wife neutral
    show boss neutral
    boss "Please forgive my tardiness [playerName]], there was a flood in my apartment, and I tried to call you but you didn't answer, and this is entirely unfair to you, after-"
    hide boss neutral
    show wife neutral at left
    wife "Ahem"
    show boss neutral at right
    boss "Oh, m— sorry, Honey… You're here for the inspection, right?"
    wife "It's already over, Ginger. Thank you for your time, [playerName]."
    hide wife neutral with dissolve
    boss "[playerName], I apologize for all of that… she didn't say anything about me, did she?"
    "..."
    boss "Nevermind, that was unprofessional, sorry… please get to work for the day. Do not let my lack of discipline infect you."
    hide boss neutral
    return

menu where_ginger_menu:
    "He's in the kitchen." if show_kitchen:
        $ show_kitchen = False
        $ show_bathroom = True
        wife "[playerName], I believe I've advised you not to lie to me before."
        jump where_ginger_menu
    "He's in the bathroom." if show_bathroom:
        $ show_bathroom = False
        $ show_behind_you = True
        wife "Your lies may grow more convincing, but I am no fool. Tell me where he is, [playerName]."
        jump where_ginger_menu
    "He's… right behind you?" if show_behind_you:
        $ show_behind_you = False
        "Honey shifts her head slightly and darts her eyes back and forth, pretending not to look."
        # hide wife neutral
        show wife angry
        wife "Try to fool me once, shame on you. Try to fool me twice, shame on your family. Try to fool me THREE TIMES?"
        wife "I don't know how you've managed to keep this job, you little hooligan. You don't know where he is, do you?"
        jump where_ginger_menu
    "He's not here":
        jump complete_12_part2

menu honey_advice_menu:
    "I'm just doing my job, lady.":
        wife "Of course. And how much is he paying you for that?"
        "..."
        wife "Right. Oh, well…"
    "Where else would I go?":
        wife "Wherever you want, darling. You certainly won't be baking pastries for Noma, that's for sure, but perhaps somewhere with a boss who doesn't avoid confrontation like it's the plague…"
    