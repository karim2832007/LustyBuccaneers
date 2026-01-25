# Version event: 3
# Version game: 0.10

label amazon_lily():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "amazon_lily"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_amazonlily()
    
    jump m_amazon_lily

label m_amazon_lily():
    if AmazonLily.h == 0:
        unknown "This is a warning! If you come any closer to the island, we will fire the cannons!!"
        unknown "You are not welcome here, pirates!!"
        unknown "Hebihime-Sama has forbidden the entry of any visitors!!"
        unknown "If you value your lives, turn back now, this is your final warning!!"

        nami "Captain! For now, we need to turn back, we can't advance, they have the advantage here!"
        
        menu m_m_amazon_lily:
            "Tell them about the flower" if sakuraflower > 0:
                #. narrador "This event is available in version 0.10.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                jump event_amazonlily_sakura
            
            "Back":
                jump ship_mid
    else:
        menu:
            "Go to the City":
                jump amazon_lily_city
            
            "Back":
                jump ship_mid 