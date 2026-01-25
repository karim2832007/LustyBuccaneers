# Version event: 3
# Version game: 0.5

label perona_room():
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "perona_room"
    scene BG locations:
        blur 3

    if not perona_crew:
        show perona c1 at center
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_perona_room

label m_perona_room():
    if ThrillerBark.h == 9:
        window hide
        pause 1.2
        window auto

        player "(What a beautiful woman!!!)"
        player "(To think I came looking for gold... and found such a gem!!)"

        call set_name_perona from _call_set_name_perona

        perona "What are you doing here and who are you?"
        player "Hello, I am [player.n]"

        if player_goal == "Pirate":
            player "And I will be the King of the Pirates!"
            $ perona_love += 2
            narrador "[perona.n] Love +2"

        elif player_goal == "Swordsman":
            player "And I will be the greatest swordsman in the world."
            $ perona_love += 1
            $ perona_subm += 1
            narrador "[perona.n] Love +1 and Submission +1"

        elif player_goal == "Harem":
            player "And I will have the largest harem in the world."
            $ perona_lust += 1
            $ perona_subm += 1
            narrador "[perona.n] Lust +1 and Submission +1"

        elif player_goal == "King":
            player "And I will be the King of the World."
            $ perona_subm += 2
            narrador "[perona.n] Submission +2"

            perona "Horo horo horo... you're quite strange..."
            perona "How did you get here?"
            perona "Where's the zombie samurai that was guarding the entrance?"
            player "He tried to attack us, so I had no choice but to defeat him..."
            perona "Wow, you must be strong! The rest were good-for-nothings... But the samurai was in another league..."
            perona "So, you're a pirate... and those back there are your crew..."
            show perona happy c1 at center with dissolve
            perona "Sounds like a lot of fun! Horo horo horo!"

        $ ThrillerBark.h = 10

    if ThrillerBark.h == 10:
        perona "I would like to join your crew."

        menu:
            "Yes":
                player "Great, the more the merrier! (I didn't think it would be so easy)"
                player "Grab your things and let's go!"

                window hide
                hide perona with dissolve
                window auto
                
                $ perona_crew = True
                $ ThrillerBark.h = 11

                pause 0.5
                $ game.clock.next()
                #aca pondría ir directo al barco como opción tmb

            "I need to think about it":
                player "I need to think about it"
                perona "That's okay. If you change your mind, I'll be here!"

    menu:
        "Back":
            jump tb_mansion_03

