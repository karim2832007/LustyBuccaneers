# Version event: 1
# Version game: 0.15

label bounty_board_alvida:

    $ renpy.show_screen("s_bounty_board_nohide", _layer="master")

    if alvida_name == "???":
        call set_name_alvida from _call_set_name_alvida_bounty

    if tutorial_bounty:
        show nami c1 at center with dissolve
        pause 0.3    
        nami "Captain, are you thinking about searching for [alvida.n]?"
        #a futuro nami podría tener ojos de Berrys 
        nami "If we manage to defeat her in combat, we'll get a good reward!!"
        nami "Plus, I'm sure the crew will be motivated by this!!"
        nami "To achieve this, we must find her first..."
        nami "From the information provided by the poster, we'll find her on the nearby coast..."
        nami "We must travel and explore the seas, and then see what nearby ships we encounter..."
        nami "But we must go prepared, having some cannonballs, wood, and food would be ideal..."
        nami "Because if we find her, we'll have to face her ship!!"

        show yamato c1 at right with dissolve
        pause 0.3   
        yamato "Yesssssss! A fight at sea!"
        yamato "If we weaken her ship enough, they won't be able to move quickly, and we can board them."
        yamato "And then we can fight against [alvida.n]!!!"
        yamato "Maybe it's better to train on the ship before going to face her..."
        #a futuro nami podría tener ojos de Berrys 
        nami "At that moment, it will all depend on you, Captain! If you defeat her, we'll receive the reward!"
        yamato "So it is, Captain!!!... So, what do you say?"
        
    menu:
        narrador "Are you sure you want to accept this mission?"

        "Yes":
            $ tutorial_bounty = False
            $ alvida_wanted = True
            narrador "New mission: 'Defeat [alvida.n]'"
        "No":
            pass

    window hide
    window auto
    hide yamato 
    hide nami
    with dissolve

    hide s_bounty_board_nohide
    jump bounty_board
