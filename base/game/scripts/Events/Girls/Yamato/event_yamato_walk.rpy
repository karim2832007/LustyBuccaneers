# Version event: 2
# Version game: 0.2

label event_yamato_walk:
    show yamato c1 with dissolve

    player "Hey [yamato.n], how are you? I was wondering if you'd like to explore the island with me..."
    player "Who knows, maybe we'll get lucky and find something interesting, a new adventure, a confrontation, or something useful for our journey!"
    
    if yamato_love < 3: 
        narrador "Requires [yamato.n] love greater than 3"
        jump event_yamato_refuse_walk

    show yamato happy with dissolve
    yamato "If there's a chance for adventure, Captain, count me in! I'm excited, hopefully, we'll get lucky!"

    $ yamato_love += 2
    narrador "[yamato.n] Love +2"

    jump event_yamato_end_walk

label event_yamato_refuse_walk:
    
    #show yamato anger with Dissolve(0.2)
    yamato "I'm a bit busy at the moment, Captain. Perhaps another time."

    jump event_yamato_end_walk

label event_yamato_end_walk:
    window hide
    hide yamato with moveoutright
    pause 0.5

    $ game.clock.next()
    jump expression game.location