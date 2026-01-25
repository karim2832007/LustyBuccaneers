# Version event: 1
# Version game: 0.14

label event_nami_walk:
    show nami c1 with dissolve

    player "Hey [nami.n], how are you? I was wondering if you'd like to explore the island with me..."
    player "Who knows, maybe we'll stumble upon a good business opportunity if we take a look around!"

    if nami_love < 3: 
        narrador "Requires [nami.n] love greater than 3"
        jump event_nami_refuse_walk

    show nami happy with dissolve
    nami "That's a great idea, Captain! I'm sure we'll find something good during our stroll!"

    $ nami_love += 2
    narrador "[nami.n] Love +2"

    jump nami_bye

label event_nami_refuse_walk:
    #show nami anger with Dissolve(0.2)
    nami "I'm a bit busy at the moment, Captain. Perhaps another time."

    jump nami_bye