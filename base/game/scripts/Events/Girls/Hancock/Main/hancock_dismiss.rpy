# Version event: 3
# Version game: 0.15

label hancock_dismiss:
    player "That's all [hancock.n], you may leave and return to your duties."

    if hancock_love < 10: 
        show hancock anger with Dissolve(0.2)
        hancock "If there's nothing important to do, please try not to waste waste my time... And remember, no one gives me orders here!"

    elif hancock_love < 20:
        show hancock with dissolve
        hancock "Excellent, [player.n], if anything happens, you know where to find me!"

    elif hancock_love >= 20:
        show hancock with dissolve
        hancock "What a shame, [player.n]! I thought we'd spend more time together... You know you can count on me!"

        if hancock_lust >= 20:
            hancock "You're leaving so soon?!? I feel so free with you, [player.n]. When you have time, I'd like to spend more private moments with you!"
        else:
            hancock "If you need anything else, just call me!"

    jump hancock_bye