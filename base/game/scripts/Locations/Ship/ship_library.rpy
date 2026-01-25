# Version event: 2
# Version game: 0.9

default ship_library_unlocked = False
default ship_library_room = False

label ship_library_room():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = True
    $ game.location = "ship_library_room"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ ambient_ship()
    $ music_time_day()
    
    call m_ship_library_room from _call_ship_library_room


label m_ship_library_room():
    if ship_library_room:
        menu:
            "Investigate the  [SakuraFlower.n]" if not game.clock.night and DrumIsland.h == 0:

                pause 0.5
                show robin at center with dissolve
                
                player "Hey [robin.n], what have you found? Any new information that might be useful about the flowers that woman was searching for?"

                robin "Captain! From what I've been reading, it seems like [hancock.n] was pretty well-informed..."
                robin "She was heading in the right direction by investigating at [ThrillerBark.n]..."
                robin "The island's doctor is a great expert and researcher in all things related to human anatomy..."
                robin "But in his recent research, he's been delving deep into the field of rare diseases and biological dangers..."
                robin "Who knows what he was trying to develop..."
                robin "But what's important for us is that in his latest research, he was obsessed with an extraordinary healing plant..."
                player "Our plant!"
                robin "Exactly, the [SakuraFlower.n]! A plant with multiple healing properties and uses..."
                robin "Unfortunately, I don't have much additional information... but I came up with an idea..."
                robin "The last time we were at [ThrillerBark.n], we found out that he was on a long journey..."
                robin "We could go back and investigate his room... Maybe we'll find something useful!"
                player "Perfect! That's a great idea, let's head back to the doctor's room in [ThrillerBark.n]'s castle to investigate!"

                $ DrumIsland.h = 1
                window hide
                hide robin       
                with dissolve
                window auto

                $ game.clock.next()
                jump m_ship_library_room

            "Back":
                #$ ui_strength = False
                jump ship_mid
    else:
        menu:
            "Repair the library Room" if not game.clock.night:
                menu:
                    narrador "Requires: 12 wood, 5 books and 200 [Berries.n]"
                    "Yes":
                        if wood >= 12 and book_robin >= 5 and berries >= 200:
                            $ wood -= 12
                            $ book_robin -= 5
                            $ berries -= 200

                            play sound "repair"
                            $ ship_library_room = True

                            window hide
                            with t_black
                            window auto
                            $ game.clock.next()
                            jump m_ship_library_room 
                        else:
                            narrador "Insufficient resources"
                    "No":
                        pass
                
                jump m_ship_library_room

            "Back":
                jump ship_mid