# Version event: 2
# Version game: 0.22

label ar_rainbase_casino_in():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ ui_interface = True
    $ game.location = "ar_rainbase_casino_in"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    #. sound casino
    $ music_arabasta()
    jump m_ar_rainbase_casino_in

label m_ar_rainbase_casino_in():
    if Arabasta.h == 11:
        pause 0.8

        

        nami "Uff, this place is huge... And it's full of people too!"  
        robin "It's quite elegant, though a bit eccentric..."  
        yamato "I don't see any guards anywhere... That's quite strange!"  
        robin "Look over there, in the east wing, there's a huge door that seems to be the VIP section..."  
        player "It's a good place to search, let's go there!"  
        

        $ Arabasta.h = 12
    
    menu:
        "Vip" if Arabasta.h == 12:
            jump ar_rainbase_h

        "Back":
            jump ar_rainbase_casino
