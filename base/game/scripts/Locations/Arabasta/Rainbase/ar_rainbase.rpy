# Version event: 2
# Version game: 0.22

label ar_rainbase():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_rainbase"
    $ arabasta_location = "Rainbase"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_rainbase

label m_ar_rainbase():
    if Arabasta.h == 9:

        show vivi serious at center with dissolve        
        vivi "Rainbase, the city of dreams!"
        vivi "From what my uncle told me, it's one of the few cities that prospered despite the droughts..."
        vivi "Mainly because of its casino and the gambling that attracts people."
        show robin neutral with dissolve:
            yalign 1.0
            xalign 0.95
        robin "That's right, I've heard it's known for being a city of high-stakes betting..."

        show nami berries with dissolve:
            yalign 1.0
            xalign 0.05
        nami "Betting... that sounds great!"

        vivi "Maybe another day, [nami.n]."
        show vivi annoyed
        vivi "Today, we must find [crocodile.n]!"
        show nami serious with Dissolve(0.2)

        player "So this is the enemy's secret base... Where can we find him?"

        vivi "[crocodile.n] runs a casino, the giant building you can see in the distance, with a huge golden Bananawani on top... That's where we'll find him!"

        player "Alright, let's go!"

        window hide
        window auto
        hide vivi
        hide nami
        hide robin
        with dissolve

        $ Arabasta.h = 10
    
    menu:
        "Go to the casino" if not game.clock.night:
            jump ar_rainbase_casino
        
        "Map" if map_arabasta and not game.clock.night:
            jump map_arabasta

        "Back":
            jump arabasta
