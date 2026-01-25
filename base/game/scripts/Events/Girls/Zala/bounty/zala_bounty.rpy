# Version event: 3
# Version game: 0.31

label bounty_board_zala:

    $ renpy.show_screen("s_bounty_board_nohide", _layer="master")

    if zala_name == "???":
        call set_name_zala from _call_set_name_zala_bounty

    menu:
        narrador "Are you sure you want to accept this mission?"

        "Yes":
            $ zala_wanted = True
            narrador "New mission: 'Defeat [zala.n]'"
        
            pause 0.3   
            show nami c1 at center with dissolve
            pause 0.3    
            nami "Captain, are you thinking about searching for [zala.n]?"
            pause 0.3  
            show nami c1 berries with Dissolve(0.2)
            nami "If we manage to defeat her in combat, we'll get a good reward!!"
            nami "To achieve this, we must find her first..."
            pause 0.3  
            show nami c1 happy with Dissolve(0.2)
            nami "From the information provided by the poster, we'll find her on the nearby coast..."
            nami "We must travel and explore the seas, and then see what nearby ships we encounter..."
            show nami c1 serious with Dissolve(0.2)   
            nami "But we must go prepared, having some cannonballs, wood, and food would be ideal..."
            nami "Because if we find her, we'll have to face her ship!!"

            show robin at right with dissolve
            pause 0.3
            show robin annoyed with Dissolve(0.2)   
            robin "[zala.n]... Mnmnmg..."
            robin "I think I remember this name... There are many rumors about her..."
            robin "From what I've heard, she belongs to a strange group, most likely linked to the criminal underworld..." 
            robin "But there's little reliable information."
            robin "It seems this group wants to stay in the shadows, so they usually eliminate anyone who has information about them."           
            robin "We should be careful, we might be inviting trouble with her organization if we get involved with her."

        "No":
            pass

    window hide
    window auto
    hide robin
    hide nami
    with dissolve

    hide s_bounty_board_nohide
    jump bounty_board
