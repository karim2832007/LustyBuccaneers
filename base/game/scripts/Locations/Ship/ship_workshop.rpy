# Version event: 5
# Version game: 0.4

label ship_workshop():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = True
    $ game.location = "ship_workshop"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_time_day()
    call m_ship_workshop from _call_ship_workshop

label m_ship_workshop():
    menu:
        "Crafting":
            jump crafting_workshop
        "Ship":
            jump workshop_ship
        "Back":
            jump ship_mid

label workshop_ship():
    $ ui_ship = True
    menu:
        "Repair with wood{space=140}+50 HP":
            if ship_player_health >= ships_hp_max[ship_player_lvl]:
                yamato "The ship is now in perfect condition, Captain!"
                jump workshop_ship

            if wood >= 1:
                $ wood -= 1
                player "Repair the ship!"
                play sound "repair"
                $ ship_player_health += 50

                if ship_player_health > ships_hp_max[ship_player_lvl]:
                    $ ship_player_health = ships_hp_max[ship_player_lvl]
    
            else:
                $ talk_random = renpy.random.choice([
                    _("Captain, we're out of wood."),
                    _("We're out of wood reserves, Captain."),
                ])

                yamato "[talk_random]"

        "Back":
            $ ui_ship = False
            jump m_ship_workshop
    
    jump workshop_ship


label crafting_workshop():
    menu:
        #+ Craft Materials book
        "Craft Gifts":
            jump craft_gifts_workshop
        "Craft Items":
            jump craft_items_workshop
        "Back":
            jump m_ship_workshop

label craft_gifts_workshop():
    menu:
        "Bracelet{space=140}-1 Gold":
            if gold >= 1:
                $ bracelet_nami += 1
                $ gold -= 1

                narrador "-1 Gold | +1 Bacelet"
            else:
                player "I don't have Gold"

        "Book{space=190}-4 Paper":
            if paper >= 4:
                $ book_robin += 1
                $ paper -= 4

                narrador "-1 Paper | +1 Book"
            else:
                player "I have [paper] paper, but I need 4."

        "Earrings{space=150}-1 Gold":
            if gold >= 1:
                $ earrings_yamato += 1
                $ gold -= 1

                narrador "-1 Gold | +1 Earrings"
            else:
                player "I don't have Gold"

        "Back":
            jump crafting_workshop

    jump craft_gifts_workshop


label craft_items_workshop():
    menu:
        "Cannon ball x2{space=140}-1 Iron":
            if iron >= 1:
                $ cannonball += 2
                $ iron -= 1

                narrador "-1 Iron | +2 Cannon ball"
            else:
                player "I don't have Iron"

        "Book{space=260}-4 Paper":
            if paper >= 4:
                $ book_robin += 1
                $ paper -= 4

                narrador "-1 Paper | +1 Book"
            else:
                player "I have [paper] paper, but I need 4."

        "Back":
            jump crafting_workshop

    jump craft_items_workshop