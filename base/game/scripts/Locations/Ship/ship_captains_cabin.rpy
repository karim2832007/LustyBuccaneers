# Version event: 6
# Version game: 0.9

label ship_captains_cabin():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None

    $ ui_interface = True
    $ game.location = "ship_captains_cabin"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto
    
    $ ambient_ship()
    $ music_time_day()
    
    call m_ship_captains_cabin from _call_ship_captains_cabin

label m_ship_captains_cabin():
    menu:
        "Go to the main deck":
            jump ship_mid

        "Work" if not game.clock.night:
            jump work

        "Call a girl" if not game.clock.night:
            jump call_girl

        "Travel" if not game.clock.night:
            jump travel

        "Raid" if not game.clock.night and location_map == 'Seas':
            jump raid_ship

        "Sleep":
            player "It's a good time for me to go to bed."
            
            if renpy.random.choice([True, False, False, False, False, False]):
                jump event_dream

            jump sleep

label work:
    narrador "You decide to delve into your work for a bit."
    $ berries += 40
    narrador "+40 Berries"

    $ game.clock.next()
    jump ship_captains_cabin


label call_girl():
    menu:
        "[nami.n]":
            jump nami_call

        "[robin.n]":
            jump event_robin_call

        "[yamato.n]":
            jump event_yamato_call

        "[perona.n]" if perona_crew:
            jump event_perona_call

        "[hancock.n]" if hancock_crew:
            jump hancock_call

        "[vivi.n]" if vivi_crew:
            jump vivi_call

        "[uta.n]" if uta_crew:
            jump uta_call

        "Back":
            jump m_ship_captains_cabin

label travel:
    menu menu_travel_1:
        "Explore the Seas" if location_map != 'Seas':
            $ location_map = "Seas"
            jump event_travel_seas

        "Shells Town" if location_map != 'Shells Town':
            $ location_map = "Shells Town"
            jump event_travel

        "Thriller Bark" if (location_map != 'Thriller Bark') and (epose_thriller_bark):
            $ location_map = "Thriller Bark"
            jump event_travel

        "Amazon Lily" if (location_map != 'Amazon Lily') and (epose_amazon_lily):
            $ location_map = "Amazon Lily"
            jump event_travel

        "Drum Island" if (location_map != 'Drum Island') and (epose_drum_island):
            $ location_map = "Drum Island"
            jump event_travel

        "Cactus Island" if (location_map != 'Cactus Island') and (epose_cactus_island):
            $ location_map = "Cactus Island"
            jump event_travel

        "Arabasta" if (location_map != 'Arabasta') and (epose_arabasta):
            $ location_map = "Arabasta"
            jump event_travel

        ">>>" if (epose_elegia or epose_dressrosa):
            menu menu_travel_2:
                "Elegia" if (location_map != 'Elegia') and (epose_elegia):
                    $ location_map = "Elegia"
                    jump event_travel

                "Dressrosa" if (location_map != 'Dressrosa') and (epose_dressrosa):
                    #narrador "This event is available in version 0.32.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                    #jump travel
                    $ location_map = "Dressrosa"
                    jump event_travel

                "<<<":
                    jump menu_travel_1

                "Back":
                    jump m_ship_captains_cabin

        "Back":
            jump m_ship_captains_cabin

