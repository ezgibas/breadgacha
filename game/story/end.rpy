label game_end:
    "After you serve your [curRecipe], you are struck by an exhilarating realization: you’ve completed enough recipes to fill up your cookbook."
    " [bakeryName] Pâtisserie is beyond back in business; if anything, this location has far too much business to handle."
    "You’ve watched Ginger’s cloudy exterior begin to lighten up. He looks happier— younger, even."
    show boss happy
    boss "[playerName]... I did not know what to expect when I took you on as my apprentice. You came here ambitionless, just as I had become since… well."
    boss "Regardless, we both seemed to find enough passion to save this place, it seems. There’s just one problem…”"
    "He fiddles with his apron, averting his gaze from you. He looks distraught."
    jump game_end_menu1 

label game_end_part2:
    boss "I absorbed myself in my work until nobody wanted anything to do with me. Then I began to want nothing to do with myself." 
    show boss sad
    boss "I don’t enjoy this profession anymore, [playerName]. I don’t think I have for a long time."
    boss "[playerName]..."
    "You hear the door open up behind you. Honey is standing at the entrance, arms folded and feet tapping on the floor."
    show boss sad at left
    show wife neutral at right
    wife "[playerName]. Ginger."
    boss "Ah… Honey, I’m sorry, now is not really a good time—"
    show wife angry at right
    wife "So when is a good time, Ginger? Was it the last time when you skipped out on inspection, and left poor [playerName] to take care of it?"
    boss "That was an accident, and the only time I—"
    wife "Was it a good time when you skipped out on traveling for my mother’s funeral for a busy week of work?"
    wife  "Was it a good time when you made me spend four hours commuting back from the airport afterwards, when you would have driven down and gotten me in an eighth of that time?"
    boss "Honey, I’m sorry, I wish I had made more time for you. If you would please give me a moment before the inspection, I’m trying to talk to [playerName] about—"
    wife "This isn’t about the stupid critique, Ginger. This is about the papers."
    "A quiet hangs in the air for a moment after she says that."
    boss "Oh, I see… [playerName], would you give me a moment?"
    "You step back into the kitchen, although you can still see and hear them talking from the back. You would like to respect their privacy, but it’s pretty hard to get out of earshot, and you can’t help but be curious when they’d already put so much on display."
    wife "Well, go on. If you’re gonna explain yourself you’d better start soon."
    boss "I’m sorry, Honey. You were right."
    wife "About what?"
    boss "I haven’t taken care of you… I haven’t taken care of myself… I haven’t taken care of anything but the bakery."
    boss "I think it’s time I give it up."
    show wife shock at right
    wife "What?! Ginger, you already chose the bakery over me, now you’re choosing nothing?"
    boss "God damn it, Honey, would you please let me finish? Yes, maybe I’ve done wrong, but you aren’t exempt from any responsibility either."
    wife "..."
    boss "I’m not ‘choosing nothing’. I’m choosing to be alive, I’m choosing to stop tethering myself to something that doesn’t love me back. Something that can’t love me back."
    wife "So you’re saying…"
    boss "Yes, Honey. I’m quitting the bakery. I don’t know where to go. Maybe back to China, France, Denmark. Maybe somewhere new."
    show wife neutral at right
    wife "Hah. You’ve grown old throughout your pact to this place. Are you sure you can hold your own on an international excursion?"
    boss "Well, that’s awfully presumptuous of you."
    wife "What is, saying you’ve grown old? You certainly have, even your wrinkles have wrinkles."
    boss "We’re still young, Honey, but that’s not what I’m talking about anyway. I still might need help up the airplane steps…"
    wife "What are you saying, Ginger?"
    boss "I’m saying that I want you to come with me, Honey."
    show wife shock at right
    wife "Oh, Ginger…"
    boss "I’m not saying that things have to go back to normal. I do not expect them to. But the months I spent alone in the bakery and the human companionship that brought me back on my feet have reminded me that loneliness should never be mistaken for normalcy."
    wife "Ginger… you really are an idiot, aren’t you?"
    boss "..."
    wife "..."
    boss "That’s what you love about me, right, princess?"
    wife "Peh. Bring it in, prince."
    scene end
    "The husband and wife wrap their arms around each other for the first time in what feels like a lifetime." 
    "Their reunion is not one of romance, but of love; two things that are inextricably linked, but still hold a weight of their own."
    "Where they were and who they are is not what matters; only that they found their way back to one another, regardless of whether or not they find themselves in the same place."
    boss "[playerName]! Come here."
    "You feign disinterest, slowly returning from the kitchen and making eye contact with Ginger, arms still wrapped around Honey. He gives you a knowing wink."
    boss "[playerName], you’re the one to thank for all of this. I’ve been so focused on the bakery, myself, and my honey that I’ve neglected to ask you about any of this."
    boss "I come to you now, not as a boss or a mentor, but as a business partner and a friend. All of this could be yours, if you want it— but only if you’re sure it’s what you want. Running something like this comes at a cost, as I’m sure you’ve learned… All that matters is that this decision is your own, no one else’s."
    boss "What I mean to say is: [playerName], where do you want to go from here?"
    jump final_menu 

label game_end_part3:
    wife "Look, we’ve got a trip to plan for. Whether you want to pat each other’s backs and sing Kumbaya or throw a kegger, you should make it quick. I’ll see you at home, Ginger."
    hide wife with dissolve
    boss "Heh."
    boss "Thanks for everything, [playerName]. Until next time."
    return


menu game_end_menu1:
    "You still want to sell the place?":
        boss "Not exactly, but there is some truth to that…"
        jump game_end_part2
    "You want to fire me?":
        boss "What?! No, quite the contrary, [playerName]..."
        jump game_end_part2
    "You’re still upset about Honey?":
        boss "I wasn’t talking about that, but if you really must know…"
        jump game_end_part2

menu final_menu:
    "Take over [bakeryName] Pâtisserie.":
        boss "I wouldn’t leave it in the hands of anybody else, [playerName]."
        jump game_end_part3
    "Quit baking and retire to a life of crime.":
        boss "Heh, you and me both, kid."
        jump game_end_part2
    "I’m not sure…":
        boss "That’s okay, [playerName]. It took me much more time to come to my own decision."
        jump game_end_part3





