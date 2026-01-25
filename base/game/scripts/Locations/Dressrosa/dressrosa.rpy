# Version event: 2
# Version game: 0.32

label dressrosa():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "dressrosa"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_dressrosa()
    jump m_dressrosa

label m_dressrosa():
    if Dressrosa.h == 0:
        pause 1.0

        nami "Island in sight, Captain!"  
        nami "There's an island up ahead!!!"  
        player "Wow, look at those rocks, they're huge!!"  
        robin "[Dressrosa.n], the country of love and passion!"  
        robin "The country is well-known for its flower fields, its cuisine, its passionate women, and its battle colosseum!"  
        yamato "Incredible, I can't wait to see what adventures await us!!"  
        nami "Uff, it's so hot!! The weather is splendid here! I'm sure there will be plenty to do!"  
        player "At last, [Dressrosa.n], it's been a long journey!"  
        robin "There should be a port city around this area, Acacia, we should head there!"  
        player "Alright, sounds like a good plan! You heard her, let's head to Acacia!"  

        
        $ Dressrosa.h = 1

    menu:
        "Go to Acacia":
            jump dr_acacia

        "Back":
            jump ship_mid
