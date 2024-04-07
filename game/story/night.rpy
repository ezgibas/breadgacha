label night_scenes:
    if game_state.countCompletedRecipes() == 3:
        "As you begin to close up, you see your boss sulking in the kitchen."
        "He is staring up at a flickering light above him. He almost shrinks under it as you see him muttering under his breath."
        show boss_sad
        boss "...Damn lightbulb. Can't afford to keep tending to this kitchen."
        hide boss_sad
        show boss_neutral
        boss "Oh, [playerName]! You are finished for the day, yes? Fine… You may go."
        "You grab your things and head out, only for him to call to you when you're at the door."
        boss "Wait! [playerName], I would like to ask you a question. Have you ever been in love?"
        call yes_no
        boss "I see… I don't believe you've met my honey before. I'm not sure if she would love you or hate you. Heh."
        hide boss_neutral
        show boss_sad
        "You catch a glimmer of regret in his eye as he stares at the ground. He looks tired. He looks like he's been tired for a long time."
        boss "Very well, [playerName]. You may go."
        hide boss_sad

    if game_state.countCompletedRecipes() == 6:
        "The clock strikes five o'clock, and you prepare to head out for the day, as the sun still shimmers over the city out the window"
        "Your boss taps you on the shoulder, his typically mopey expression replaced by a half-hearted grin."
        show boss_happy
        boss "[playerName]… You should be proud, you know. You've mastered each of [bakeryName] Pâtisserie's classic recipes. How do you feel now, kiddo?"
        hide boss_happy
        call core_recipes_complete
    if debug:
        call core_recipes_complete
    
    return

menu yes_no:
    "Yes":
        return
    "No":
        return

menu core_recipes_complete:
    "Excited to push the menu even further, sir!":
        show boss_happy
        boss "Heh. That is what I like to hear."
        hide boss_happy
    "That was it? It wasn't so hard.":
        show boss_neutral
        boss "Oh, tough guy, are you now? Do not let your hubris supercede your talent."
        hide boss_neutral
    "Um… can I go now?":
        show boss_happy
        boss "Ha! Good one. You still have much to learn."
        hide boss_happy

