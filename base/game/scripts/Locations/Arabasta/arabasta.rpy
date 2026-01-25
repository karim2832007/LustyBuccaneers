# Version event: 3
# Version game: 0.20

label arabasta():
    window hide
    show screen screen_black with Dissolve(0.6)
    
    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None

    $ ui_interface = True
    $ game.location = "arabasta"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_arabasta()
    
    jump m_arabasta

label m_arabasta():
    if Arabasta.h == 0:

        nami "Island in sight, Captain!"
        player "Wow, it's a massive desert."
        yamato "It's such a huge island! All you can see is sand everywhere..."
        nami "This is perfect, we can get a good tan here!"
        player "Hahaha, there's no time for that right now, [nami.n]..."
        player "(Although I'd love to see all of them in swimsuits...)"
        yamato "So this is [Arabasta.n]..."
        robin "Technically speaking, this is Sandy Island, one of the largest islands in Paradise."
        robin "And here lies the Kingdom of [Arabasta.n], one of the twenty kingdoms that founded the World Government."
        vivi "You're quite well-informed, [robin.n]! Everything you've said is absolutely correct!"
        robin "Thank you. I had planned to come here... It's a land rich in history and historical sites..."
        robin "There's so much to do here..."
        vivi "You'll all have time to see and enjoy all its beauty..."
        vivi "But for now, let's focus..."
        vivi "Is a very large island, and the high temperatures make traveling between the different cities difficult."
        vivi "Especially now, as we're suffering from a severe drought..."
        vivi "This is, unfortunately, one of the reasons for the widespread discontent among the people..."
        yamato "On top of everything else, we need to avoid drawing attention. Baroque Works might be looking for us."
        vivi "Exactly!!"
        vivi "The best course of action is to head to Nanohana first. It's a large port city not far from here."
        vivi "We can stock up on everything we need there, and with so many people around, we can keep a low profile."
        vivi "Afterward, the next step would be to head to a small oasis town, the village of Yuba."
        vivi "That's why we need to gather supplies first to reach it."
        player "Alright, sounds like a good plan! You heard her, let's head to Nanohana!"


        $ Arabasta.h = 1

    menu:
        "Map" if map_arabasta and not game.clock.night:
            jump map_arabasta

        "Go to Nanohana" if not map_arabasta:
            jump ar_nanohana
        
        "Back":
            jump ship_mid