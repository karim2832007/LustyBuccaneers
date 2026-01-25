# Version event: 1
# Version game: 0.14

label nami_hangout_2:
    player "Hey [nami.n], how are you? What do you think about the crew, what's your opinion?"
    nami "Ahoy Captain!! At the moment, I see the crew in very good spirits. We all get along well, and we're becoming more united each day..."
    nami "If we keep working like this, we'll soon form a great crew!"
    nami "I'm particularly excited about our next adventure!"

    menu:
        "Keep working hard!":
            player "I like hearing that, let's keep working hard!"
            show nami c1 happy with dissolve
            nami "That's what I'll do, Captain! Back to my work!"

            $ nami_love += 1
            narrador "[nami.n] Love +1"

        "Praise her...":
            player "With crew members as sexy as you, it'll be hard not to form a great crew!!"
            player "I'm sure many will be attracted to your beauty and elegance!"
            show nami c1 shame with dissolve
            nami "Thank you, Captain! I didn't realize you saw me that way... I'll get back to my duties now. See you later."
            player "Keep it up!!"

            $ nami_lust += 1
            narrador "[nami.n] Lust +1"

        "This is a waste of time...":
            player "Good spirits?!... There's no time to waste on such nonsense in this crew..."
            player "The only thing to focus on is oneself... Only then will the crew be stronger."
            show nami c1 anger with dissolve
            nami "What a selfish and self-centered way of thinking..."
            nami "I didn't realize you were so narrow-minded... I'll get back to my work..."

            $ nami_love -= 1
            narrador "[nami.n] Love -1"

    return