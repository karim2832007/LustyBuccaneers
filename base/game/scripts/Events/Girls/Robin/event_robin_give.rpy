# Version event: 3
# Version game: 0.1

label event_robin_give:
    menu:
        "Give her a Totem" if totem_robin > 0:
                $ totem_robin -= 1
                player "While passing through our last destination, I managed to gather some good materials and put together this [robin.n]..."
                player "I hope you like it, I recreated something I heard about out there!!"

                show robin happy with dissolve
                robin "What a beautiful replica, Captain!... I really appreciate the gesture, you know I love these kinds of details. Thank you very much!"

                $ robin_love += 2
                $ robin_lust += 1
                narrador "[robin.n] Love +2 | [robin.n] Lust +1"

        "Give her a Book" if book_robin > 0:
                $ book_robin -= 1
                player "I have the following gift for you, [robin.n]..."
                player "I'm sure you'll love it!!"

                show robin happy with dissolve
                robin "I'll definitely enjoy reading your gift, Captain! You know I'm interested."
                $ robin_love += 4
                $ robin_lust += 2
                narrador "[robin.n] Love +4 | [robin.n] Lust +2"

        "Give her a Bento" if bento_yamato > 0:
                $ bento_yamato -= 1
                player "While passing through our last destination, I managed to gather some good materials and put together this [robin.n]..."
                player "I hope you like it, I recreated something I heard about out there!!"

                #show robin with dissolve
                robin "Hmm, I suppose it's nice... It's a bit unexpected, I might like it, I'm not sure, to be honest!..."
                $ robin_love -= 2
                $ robin_lust -= 1

                narrador "[robin.n] Love -2 | [robin.n] Lust -1"

        "Back":
            return


    hide robin with moveoutright
    pause 0.5

    $ game.clock.next()
    jump expression game.location
