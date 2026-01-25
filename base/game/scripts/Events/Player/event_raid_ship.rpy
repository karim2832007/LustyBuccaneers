# Version event: 1
# Version game: 0.3

define Seas_Ships = ["Small ship"]
default raid_ship_day = 0
default raid_ship_clock = ""

label raid_ship:
    python:
        if game.clock.getTime != raid_ship_clock or game.clock.getDay != raid_ship_day:
            raid_ship_clock = game.clock.getTime
            raid_ship_day = game.clock.getDay

            Seas_Ships = []
            if renpy.random.choice([True, False]):
                Seas_Ships.append("Small ship")
                
                if alvida_wanted:
                    Seas_Ships.append("Alvida ship")

                if zala_wanted:
                    Seas_Ships.append("Zala ship")

    if len(Seas_Ships) == 0:
        nami "There are no ships in sight, Captain!"
        jump m_ship_captains_cabin


    python:
        list_ships = []
        for x in Seas_Ships:
            list_ships.append("Raid the " + x)#Attack
        
        list_ships.append("Back")

    call screen choice_list(list_ships)

    if choice_id < len(Seas_Ships):
        jump ship_battle
    
    jump m_ship_captains_cabin