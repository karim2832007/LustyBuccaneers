# Version event: 4
# Version game: 0.9

label ship_mid():
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ ui_interface = True
    $ game.location = "ship_mid"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_time_day()
    call m_ship_mid from _call_ship_mid

label m_ship_mid():
    menu:
        "Chat with someone" if not game.clock.night:
            jump chat_with_someone
        "Check the Girls Room" if not game.clock.night:
            jump ship_girls_room
        "Check the Girls Sleeping" if game.clock.night:
            jump ship_girls_sleeping

        "Rooms" if not game.clock.night:
            menu m_ship_rooms:
                "Go to the Kitchen" if not game.clock.night:
                    jump ship_kitchen
                "Go to the Workshop" if not game.clock.night:
                    jump ship_workshop
                "Go to the Training Room" if not game.clock.night:
                    jump ship_training_room
                "Go to the Library" if not game.clock.night and ship_library_unlocked:
                    jump ship_library_room
                "Go to the bathroom" if not game.clock.night:
                    #narrador "This event is available in version 0.[version_id_next].\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                    #jump m_ship_rooms
                    jump ship_bathroom
                "Return to the main deck":
                    jump m_ship_mid

        "Get off the ship" if (not game.clock.night) and (not location_map == "Seas"): #! posible error si cambia de mar
            jump ship_off_the_ship
        "Fishing" if (not game.clock.night) and (location_map == "Seas"):
            if not tool_rod:
                narrador "Fishing rod required"
                jump m_ship_mid

            jump ship_fishing
        "Return to the captain's cabin":
            jump ship_captains_cabin

label chat_with_someone:

    $ list_girls = [nami_name, robin_name, yamato_name]

    if perona_crew:
        $ list_girls.append(perona_name)
    
    if hancock_crew:
        $ list_girls.append(hancock_name)
    
    $ random_girl = renpy.random.choice(list_girls)
            
    if random_girl == nami_name:
        jump nami_chat
        #call event_nami_hangout from _call_event_nami_hangout_ship_mid

    elif random_girl == robin_name:
        call event_robin_hangout from _call_event_robin_hangout_ship_mid
    
    elif random_girl == yamato_name:
        call event_yamato_hangout from _call_event_yamato_hangout_ship_mid

    elif random_girl == perona_name:
        call event_perona_hangout from _call_event_perona_hangout_ship_mid

    elif random_girl == hancock_name:
        jump hancock_chat
        #call event_perona_hangout from _call_event_perona_hangout_ship_mid

    $ game.clock.next()
    jump ship_mid


label ship_girls_sleeping:
    menu:
        "[nami.n]":
            jump event_nami_sleep

        "[robin.n]":
            jump event_robin_sleep
            
        "[yamato.n]":
            jump event_yamato_sleep

        "[perona.n]" if perona_crew:
            jump event_perona_sleep

        "[hancock.n]" if hancock_crew:
            jump event_hancock_sleep

        "[vivi.n]" if vivi_crew or CactusIsland.h >= 3:
            jump event_vivi_sleep

        "[uta.n]" if uta_crew:
            jump event_uta_sleep

        "Back":
            jump ship_mid

label ship_off_the_ship:
    if location_map == "Shells Town":
        jump shells_town
    elif location_map == "Thriller Bark":
        jump thriller_bark
    elif location_map == "Amazon Lily":
        jump amazon_lily
    elif location_map == "Drum Island":
        jump drum_island
    elif location_map == "Cactus Island":
        jump cactus_island
    elif location_map == "Arabasta":
        jump arabasta
    elif location_map == "Elegia":
        jump elegia
    elif location_map == "Dressrosa":
        jump dressrosa

    jump m_ship_mid