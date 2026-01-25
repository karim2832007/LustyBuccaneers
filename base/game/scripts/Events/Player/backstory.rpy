# Version event: 5
# Version game: 0.18

default mia_bathroom_03 = False

label backstory:
    $ quick_menu = False
    $ game.location = "main_menu"

    scene black_100
    stop sound fadeout 1

    show events backstory backstory with Dissolve(2.0):
        blur 3

    narrador "Wealth, fame, power. The King of the Pirates, a legendary pirate, achieved everything this world had to offer."
    
    narrador "My treasure? It's yours if you want it. Find it! I left everything the world has on that last island!..."
    
    narrador "With just those words, prior to his death, he stirred the entire world to search for the greatest pirate treasure."
    
    narrador "And so, men set their sights on the Grand Line, chasing after their dreams. The world has truly entered a Great Pirate Era!"


    window hide
    hide events backstory with Dissolve(2.0)

    call set_player_name from _call_set_player_name_backstory
    window auto
    

    player "I am [player.n], a young pirate unlike any other..."

    player "My main goal is to travel across the world, visiting island after island to...:"

    menu:
        "To become the King of the Pirates":
            player "I'll be a free spirit, living from adventure to adventure, forming the best crew! I'll defeat anyone who gets in my way. My crew, especially me, will claim the greatest rewards... we'll be the most wanted and earn the respect and recognition of the entire world..."
            
            $ Strength += 1
            $ Charisma += 1
            $ player_goal = "Pirate"

            narrador "Strengh +1 | Charisma +1" 

        "To become the greatest swordsman in the world":
            player "I will become the greatest swordsman of all seas! I've sworn to myself to become the best, so I'll train tirelessly to defeat the current recognized number one in the world and take away that title... No one will be able to stop me in a fight!"

            $ Strength += 2
            $ player_goal = "Swordsman"

            narrador "Strengh +2" 

        
        "To form the best harem in the world.":
            player "Women!!! Clearly the most important thing in this life... I'll search far and wide for the best women in the world, assemble my own harem as a crew, and live with them wherever that cursed treasure may be, away from the rest of the world..."

            $ Charisma += 2
            $ player_goal = "Harem"

            narrador "Charisma +2" 

        "To become the king of the world":
            player "From the bottom of the chain, I will reach the top! There's nothing stopping me from moving forward, there are no differences between right and wrong. By any means necessary, I will become the king who dominates everything!"
            
            $ Strength += 1
            $ Luck += 1

            $ player_goal = "King"

            narrador "Strengh +1 | Luck +1"
    
    player "(And so, I decided to set sail... I'll start with a small crew... Even though they're all women, don't be deceived, these are the cleverest, strongest, and smartest around...)"


    $ game.location = "ship_door"
    scene BG locations with Dissolve(2.0):
        blur 3

    window hide
    show nami c1 with dissolve
    pause 1.2
    window auto

    narrador "One of the best navigators I've ever met..."
    narrador "Skilled in business, theft, and piracy, indispensable for sailing the seas..."

    call set_name_nami from _call_set_name_nami_backstory

    nami "Ahoy, Captain! I'll guide us through the seas in search of the greatest treasures."
    nami "Rest assured that with my guidance, we'll travel a path of fortunes like none you've ever seen."

    hide nami c1 with dissolve

    narrador "The next addition was one of the smartest individuals I've ever met..."
    narrador "Not only does she know a lot about history and politics, but she's also familiar with many ancient languages, exotic fruits, and all kinds of vital information to progress on our journey..."

    window hide
    show robin c1 with dissolve
    pause 1.2
    window auto

    call set_name_robin from _call_set_name_robin_backstory

    robin "It's a pleasure, Captain! Let's discover together the mysteries and teachings hidden within the seas and different civilizations."

    hide robin c1 with dissolve

    narrador "Lastly, a strong and brave woman, always seeking new experiences and challenges alike..."
    narrador "A fanatic of training and self-improvement, with a wild heart thirsty for adventures..."

    window hide
    show yamato c1 with dissolve
    pause 1.2
    window auto

    call set_name_yamato from _call_set_name_yamato_backstory

    yamato "Hi, Captain! Rest assured that with me on this journey, you'll have a strong ally when facing any other crew."
    yamato "I'm eager for our next adventure and to confront other pirates!"

    hide yamato c1 with dissolve

    narrador "And so, with my goals set firmly, I decided to set sail to achieve my objective!"

    window hide
    show robin c1 at center:
        xalign 0.15

    show yamato c1 at center:
        xalign 0.85
        
    show nami c1 at center:
        xalign 0.5

    with dissolve
    pause 0.2
    window auto

    player "With these three sexy, intelligent, and strong ladies, I will set my plan in motion..."
    player "I plan to recruit a few more members along the way... Let's see who we can find on the next islands..."
    player "For now, it's time to prepare everything... Let's set sail!!"

    window auto


    window hide
    return