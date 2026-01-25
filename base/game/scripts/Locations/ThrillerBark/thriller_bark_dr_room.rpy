# Version event: 3
# Version game: 0.9

label thriller_bark_dr_room():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ game.location = "thriller_bark_dr_room"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_thriller_bark_dr_room

label m_thriller_bark_dr_room():
    menu:
        "Investigate about the [SakuraFlower.n]" if DrumIsland.h == 1:
            jump tb_dr_room_sakura

        "Investigate the Room" if not tb_forest_map:
            jump tb_dr_room_map

        "Back":
            jump tb_mansion_01


label tb_dr_room_map():

    show nami at center with dissolve

    nami "What a beautiful woman..."
    nami "There are so many pictures of her..."
    nami "Who could she be?!... They seem to be old photos and paintings..."
        
    show nami:
        linear 0.4 xalign 0.85

    pause 0.4

    show robin with dissolve:
        yalign 1.0
        xalign 0.5        
        
    robin "The room is full of medical books..."
    robin "It also seems to belong to a man, judging by the personal items around here..."
    robin "The large number of pictures are all of the same woman... It could be a sign of obsession or fanaticism perhaps..."

        
    show robin:
        linear 0.4 xalign 0.15

    pause 0.4

    show yamato at center with dissolve       
            
    yamato "What are you doing, Captain, rummaging and checking everywhere!!"
    yamato "Hahaha what are you looking for?!..."

    player "Anything valuable, there might be something interesting..."

    window hide
    hide nami
    hide robin
    hide yamato
    with dissolve
    window auto

    player "Maybe over here..."
    player "!!!"
    player "What is this?! Look, girls..."

    window hide

    show events forest tb_forest_map with Dissolve(1.0)

    pause 2

    nami "It's a map, Captain!!"
    nami "It seems to mark a path..."   

    if perona_crew:
        perona "It's a map that serves as a guide to avoid getting lost in the dense forest near the entrance"
        perona "We could waste a lot of time or even end up lost if we don't use it..."

    player "Excellent! It seems it could be useful... I'll take it, let's move on!"

    window hide
    pause 7
    window auto


    hide events forest tb_forest_map with Dissolve(1.0)

    $ tb_forest_map = True

    jump m_thriller_bark_dr_room


label tb_dr_room_sakura():


    player "Perfect, we're here!! Let's start searching, everyone... If you find anything related to the [SakuraFlower.n], let me know!"

    pause 0.5

    show nami with dissolve:
        yalign 1.0
        xalign 0.85   

    nami "Nothing in these drawers..."


    show yamato with dissolve:
        yalign 1.0
        linear 0.4 xalign 0.15

    yamato "Nothing over here either..."

    show robin at center with dissolve

    robin "This way, Captain... Look what I found!"

    player "What is it?!"

    nami "That over there is an Eternal Pose!! The name written on it indicates it's for [DrumIsland.n]."

    robin "It's accompanied by this book, Captain. If you'll allow me a moment, I'll tell you what it's about..."

    robin "..."

    robin "It's quite interesting... Briefly, the book discusses various investigations of a famous doctor in [DrumIsland.n]..."
    robin "This doctor talks about treating several diseases using sakura flowers, and even managed to cure a previously incurable disease!!"
    robin "It seems really fascinating!"

    player "Excellent! It's exactly what we're looking for!"
    player "So, the island of [DrumIsland.n], and a strange doctor, what's her name?"

    robin "It seems she's quite an eccentric doctor, keeps a low profile, and many say she's crazy..."

    robin "In the book, she's only mentioned by the alias 'Doctorine', that's our only lead, Captain..."

    player "Perfect, let's take all of this to the ship. We need to prepare provisions for the journey..."

    player "When we're ready, I'll let you know [nami.n], and we'll set off on this new adventure... To the island of [DrumIsland.n]!"

    nami "Understood, Captain!!"

    $ epose_drum_island = True
    $ DrumIsland.h = 2

    window hide
    hide robin
    hide yamato 
    hide nami       
    with dissolve
    window auto

    jump m_thriller_bark_dr_room