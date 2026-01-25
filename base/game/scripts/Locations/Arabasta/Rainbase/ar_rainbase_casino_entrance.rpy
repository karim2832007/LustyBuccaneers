# Version event: 2
# Version game: 0.22

label ar_rainbase_casino():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_rainbase_casino"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_arabasta()
    jump m_ar_rainbase_casino

label m_ar_rainbase_casino():
    if Arabasta.h == 10:
        pause 0.8
        vivi "We arrived, this is Rain Dinners, the casino managed by [crocodile.n]"  
        player "Wow... This place is huge! So this is the enemy's base..."  
        vivi "Yes, it's the biggest building in this city... We'll have to be careful not to get lost inside!"  
        yamato "It must be guarded as well, let's be cautious!"  
        player "Alright, let's go in. I'm going to defeat that bastard and make him pay for everything he's doing!"  
     

        $ Arabasta.h = 11
    
    menu:
        "Get in":
            jump ar_rainbase_casino_in

        "Back":
            jump ar_rainbase
