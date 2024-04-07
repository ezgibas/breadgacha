label night_scenes:
    if game_state.countCompletedRecipes() == 1:
        "Congrats on completing your first day at [bakeryName] Pâtisserie!"
        return
    if game_state.countCompletedRecipes() == 3:
        call core_half_complete
        
    if game_state.countCompletedRecipes() == 6:
        call core_full_complete

    if game_state.countCompletedRecipes() == 16:
        call complete_16
    else:
        "Another day at [bakeryName] Pâtisserie comes to a close."
        return
        
    return


label core_half_complete:
    "As you begin to close up, you see your boss sulking in the kitchen."
    "He is staring up at a flickering light above him. He almost shrinks under it as you see him muttering under his breath."
    show boss sad
    boss "...Damn lightbulb. Can't afford to keep tending to this kitchen."
    hide boss sad
    show boss neutral
    boss "Oh, [playerName]! You are finished for the day, yes? Fine… You may go."
    "You grab your things and head out, only for him to call to you when you're at the door."
    boss "Wait! [playerName], I would like to ask you a question. Have you ever been in love?"
    call yes_no
    boss "I see… I don't believe you've met my honey before. I'm not sure if she would love you or hate you. Heh."
    hide boss neutral
    show boss sad
    "You catch a glimmer of regret in his eye as he stares at the ground. He looks tired. He looks like he's been tired for a long time."
    boss "Very well, [playerName]. You may go."
    hide boss sad
    return


menu yes_no:
    "Yes":
        return
    "No":
        return

label core_full_complete:
    "The clock strikes five o'clock, and you prepare to head out for the day, as the sun still shimmers over the city out the window"
    "Your boss taps you on the shoulder, his typically mopey expression replaced by a half-hearted grin."
    show boss happy
    boss "[playerName]… You should be proud, you know. You've mastered each of [bakeryName] Pâtisserie's classic recipes. How do you feel now, kiddo?"
    call core_recipes_complete_menu
    hide boss happy
    show boss happy
    boss "You know, the bakery wasn't in the best state before you got here. I don't think I've taken care of it, or myself, in a while. 
        You've really turned things around, you know? What I mean to say is thank you, [playerName]."
    "The quiet moment you share is interrupted by a banging on the door. You look through the glass to see a chicly dressed middle-aged woman wearing expensive jewelry and a scowl on her face."
    wife_unknown "For the love of all that is holy, could you open up the door?! NOW."
    boss "Ah, just give me a moment, [playerName]."
    "Ginger taps you on the shoulder and gives you a warm, reassuring smile, stepping over to unlock the door."
    # hide boss happy
    show boss happy at left
    show wife angry at right
    wife_unknown "Took you long enough. Who's the kid?"
    boss "Ah, this is [playerName], my new apprentice. [playerName], this is my honey-"
    "The woman slaps at Ginger's shoulder. Her petite stature diminishes her aggression, although it does startle the both of you."
    wife_unknown "I am not {i}yours{/i} anymore, Ginger. You still haven't signed the papers, you know."
    show boss sad at left
    boss "I apologize, I've just been so busy that—"
    wife_unknown "I don't care. That's not what I've come here to talk about, regardless. I've come for my quarterly review."
    boss "Oh, I see…"
    wife_unknown "[playerName], allow me to introduce myself, although I'm sure you've already heard much about me."
    wife_unknown  "My name is Honey Gāo. I am a food critic. I do not hold back. I will not let any flowery sentiments or unearned pity sugarcoat my critique today."
    boss "Sugarcoating is the least of my concerns, really…"
    hide boss sad
    hide wife angry
    show wife angry # show her at center
    wife "“Hmph. [playerName], did you make this [curRecipe]*?"
    call honey_critique_menu
    "Honey cautiously takes a bite of the [curRecipe], covering her face with a handkerchief as she chews. She swallows and sets it down, taking pause to contemplate."
    wife "Hmm… It's not half-bad, actually. But I have notes, of course. You used too much [ingredient1] and not enough [ingredient2]."
    wife "The consistency is awful, perhaps because it is far too overcooked. Still, you have drive, it seems."
    wife "If your boss has not driven you mad by the time I return, you may have actually amassed the skills to make a salvageable pastry. Ta-ta, for now."
    "She exits just as abruptly as she entered, expensive heels click-clacking on the pâtisserie's floor."
    hide wife angry
    show boss sad
    "You turn to Ginger, his face relaxed back into its typical lethargy."
    boss "Sorry… about all of that. I'll see you tomorrow, [playerName]..."
    hide boss sad

    return

menu honey_critique_menu:
    "Yes":
        "I could tell. Your presentation is atrocious."
    "No":
        "Don't lie to me! You may cheat your way through making this [curRecipe] with your sloppy technique, but you will not deceive a professional such as myself."

menu core_recipes_complete_menu:
    "Excited to push the menu even further, sir!":
        boss "Heh. That is what I like to hear."
        hide boss happy
    "That was it? It wasn't so hard.":
        # hide boss happy
        show boss neutral
        boss "Oh, tough guy, are you now? Do not let your hubris supercede your talent."
        hide boss neutral
    "Um… can I go now?":
        boss "Ha! Good one. You still have much to learn."
        hide boss happy

label complete_16:
    "You’ve noticed there’s scarcely a moment where the bustle of customers dies down anymore. What you would now deem a slow day would have been the busiest you’ve ever experienced when you first started here."
    "It’s a lot to handle, of course, but you can’t help but feel a sense of accomplishment. As you reminisce over your time at [bakeryName] Pâtisserie, you are interrupted by your expectant boss."
    show boss happy
    boss "[playerName], I’ve been meaning to talk to you about something. I’m sure you’ve recognized that things have gotten much busier around here."
    boss " I was on the verge of selling before you started here. You know, when I first hired you, I didn’t expect you’d have this much of an impact on the pâtisserie, but here we are… How do you feel about all this, [playerName]?"
    call complete_16_menu
    boss "Ah, I see... [playerName], you should understand that this is no small feat."
    boss "When I was your age, my dreams may have far surpassed a small business such as this one, but in terms of my actual accomplishments… Well, it’s not time for celebration."
    boss "Not yet, anyway. Your cookbook is nearing completion. Only a few more recipes and you’ll be done."


menu complete_16_menu:
    "Proud.":
        return 
    "Scared.":
        return
    "Ambivalent.":
        return


