# Version event: 2
# Version game: 0.2

label event_robin_walk:
    show robin c1 with dissolve

    player "Hello [robin.n]! I was wondering if you wanted to explore the island with me."
    player "Who knows, maybe we'll get lucky and find something interesting for your research or useful information for our journey!"

    if robin_love < 3: 
        narrador "Requires [robin.n] love greater than 3"
        jump event_robin_refuse_walk

    show robin happy with dissolve
    robin "That sounds like an interesting idea, Captain! We might find something good during the walk. Let's see what we come across!"

    $ robin_love += 2
    narrador "[robin.n] Love +2"

    jump event_robin_end_walk

label event_robin_refuse_walk:
    
    #show robin anger with Dissolve(0.2)
    robin "I'm a bit busy at the moment, Captain. Perhaps another time."

    jump event_robin_end_walk

label event_robin_end_walk:
    window hide
    hide robin with moveoutright
    pause 0.5

    $ game.clock.next()
    jump expression game.location