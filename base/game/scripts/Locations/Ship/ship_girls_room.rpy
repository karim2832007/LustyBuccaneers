# Version event: 5
# Version game: 0.14

label ship_girls_room():
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ ui_interface = True
    $ game.location = "ship_girls_room_door"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_time_day()
    call m_ship_girls_room from _call_ship_girls_room

label m_ship_girls_room():

    #jump nami_room_ship

    if renpy.random.choice([True, False, False, False, False]):
        pause 0.5
        window hide
        show screen screen_black with Dissolve(0.6)
        $ game.location = "ship_girls_room"
        scene BG locations:
            blur 3
        hide screen screen_black with Dissolve(0.3)
        window auto

        if Haki.h == 5 and not haki_robin_panties:
            menu:
                "Take [robin.n]'s panties":
                    jump haki_h5_robin

                "Back":
                    pass
        else:
            narrador "Bad luck..."
            narrador "There's no one around here, maybe I'll have better luck later."

    else:

        $ list_girls = [nami_name, robin_name]

        #if perona_crew:
        #    $ list_girls.append(perona_name)
        
        $ random_girl = renpy.random.choice(list_girls)

        $ random_x = renpy.random.choice([1, 2, 3])
        
        
        if random_girl == nami_name:
            jump nami_room_ship

        elif random_girl == robin_name:
            jump robin_room_ship

        else:
            pause 0.5
            window hide
            show screen screen_black with Dissolve(0.6)
            $ game.location = "ship_girls_room"
            scene BG locations:
                blur 3
            hide screen screen_black with Dissolve(0.3)
            window auto
            
        #if random_girl == robin_name:
        #    if random_x == 1:
        #        show robin c1_bra anger with dissolve
        #
        #    elif random_x == 2:
        #        show robin c1_underwear anger with dissolve
        #
        #    else:
        #        show robin c1_breasts anger with dissolve
        #
        #    robin "What are you doing entering our room without knocking, Captain!"
        #    robin "It's disrespectful!! leave right now!"
        #
        #    $ robin_love -= 1
        #    narrador "[robin.n] Love -1"

        #if random_girl == yamato_name:
        #    if random_x == 1:
        #        show yamato c1_bra anger with dissolve

        #    elif random_x == 2:
        #        show yamato c1_underwear anger with dissolve

        #    else:
        #        show yamato c1_breasts anger with dissolve

        #    yamato "What are you doing barging in like that without warning!" 
        #    yamato "Get out right now or you'll see what I'm capable of when I'm angry!"

        #    $ yamato_love -= 1
        #    narrador "[yamato.n] Love -1"

        #elif random_girl == perona_name:
        #    if random_x == 1:
        #        show perona c1_bra anger with dissolve

        #    elif random_x == 2:
        #        show perona c1_underwear anger with dissolve

        #    else:
        #        show perona c1_breasts anger with dissolve

        #    perona "What are you doing entering like that without knocking?!"
        #    perona "Don't think that just because you're the Captain, you can do whatever you want. Get out of here right now!"

        #    $ perona_love -= 1
        #    narrador "[perona.n] Love -1"

    $ game.clock.next()
    jump ship_mid
