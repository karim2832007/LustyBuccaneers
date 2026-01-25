# Version event: 3
# Version game: 0.4

default first_travel_seas = True

label event_travel:
    player "Ahoy, [nami.n]!! It's time to set sail for our next adventure! Onward to [location_map]!"
    # Anchor // -Raise the anchor!!
    player "Hoist the sails!! It's time to venture out to sea once again!"

    show nami c1 with dissolve
    nami "Understood, Captain!"

    window hide
    hide nami with moveoutright

    jump sleep

label event_travel_seas:
    if first_travel_seas:
        $ first_travel_seas = False
        player "[nami.n]!! It's time to set sail for our next adventure!"
        player "Raise the anchor!! Hoist the sails!!"

        show nami c1 with dissolve

        nami "Understood, Captain! I'm at your command!" 

        player "We have a sea full of adventures and mysteries ahead!!"
        player "New islands, new challenges..."
        player "(Perhaps I could recruit some new beautiful women for my crew!!!)"
        nami "Gold, Captain!! Maybe we could find an island full of gold."
        nami "We have supplies for several days at sea, but it would be ideal to decide on a destination soon!"
        player "Let's see what the ocean has in store for us."
    else:
        #ERROR "es momento de explorar nuevas aguas // -Onward to [location_map]!"
        player "Ahoy, [nami.n]!! It's time to set sail for our next adventure!"
        player "Raise the anchor!! Hoist the sails!! It's time to venture out to sea once again!"

        show nami c1 with dissolve
        nami "Understood, Captain!"

    window hide
    hide nami with moveoutright

    $ game.clock.next()
    jump expression game.location