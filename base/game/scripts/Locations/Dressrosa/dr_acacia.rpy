# Version event: 2
# Version game: 0.32

label dr_acacia():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "dr_acacia_1"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    stop ambient fadeout 2.0
    $ music_dressrosa()
    jump m_dr_acacia

label m_dr_acacia():
    if Dressrosa.h == 1:
        pause 1.0

        player "Wow!! So this is Acacia!!!"  

        show robin at center with dissolve  
        robin "That's right, Captain, this is the port city of Acacia."  
        robin "From what I've read, every foreigner who comes here is fascinated for three reasons..."  
        robin "First, for its flower fields and beautiful floral fragrances, or its delicious food and aromatic dishes..."  
        robin "Second, for the fire of its passionate women and their beautiful dances!"  
        player "(That sounds really good!!! I won't be bored around here!)"  
        robin "And lastly... For that..."  
        robin "I didn't believe it either... but look over there..."  

        player "!!!"  
        player "What the hell!?!"  

        $ black_to_img("events dressrosa h1 h1_1")
        pause 0.5
        nami "P-plush dolls?!?"  
        nami "It's like... as if they were their partners or friends!?!"  
        yamato "But how... Look over there!"  

        $ black_to_img("events dressrosa h1 h1_2")
        pause 0.5
        robin "Yes, that's right... This sight leaves everyone astonished..."  

        $ black_to_img("events dressrosa h1 h1_3")
        pause 0.5
        player "It's a bunch of toys! Hahaha how fun!!"  

        $ black_to_img("BG locations", hide="events dressrosa h1")

        show nami with dissolve:  
            xalign 0.10  
            yalign 1.0  

        show yamato with dissolve:  
            xalign 0.90  
            yalign 1.0  

        player "This is really amazing!!! How is it possible that they're walking?!?"  
        robin "It's a truly fascinating phenomenon... I didn't believe the reports I read... But being here and seeing it with my own eyes, there's no doubt."  
        robin "It's a mystery I'd like to uncover..."  
        yamato "Nobody here seems surprised by them..."  
        yamato "It's like it's something normal..."  
        nami "Everywhere, and so naturally, toys live together with humans... no wonder this feels strange to all visitors."  
        yamato "It's really very strange... Maybe we'll learn more once we walk the streets and talk to the people around here."
        show nami serious with Dissolve(0.2)    
        nami "Could it be related to the new king of this island? All that [robin.n] told us when we read about the tournament..."  
        nami "I don't really know much about the culture here, but I don't remember it ever being mentioned that toys were walking around everywhere from the start..."
        show robin annoyed with Dissolve(0.2)      
        robin "It could be related, but obviously it wouldn't come to light if that were the case..."  
        robin "The navy and the world government would have it tightly sealed if it were connected... We're talking about a Shichibukai!"  
        player "Hmm, all this is suspicious..."  
        player "But I don't care if toys walk around!! Let's go to the coliseum!"  
        player "Once we have the fruit in our possession, we'll see what we can uncover about these mysterious toys!"  
        player "Let's go!!"

        hide nami
        hide robin
        hide yamato 
        with dissolve  

        $ Dressrosa.h = 2

    menu:
        "Go to Colosseum":
            jump dr_ac_colosseum

        "Shop":
            call shop_default from _call_shop_dressrosa
            jump m_dr_acacia

        "Back":
            jump dressrosa
