# Version event: 2
# Version game: 0.23

label vivi_dismiss:
    player "That's all [vivi.n], you may leave and return to your duties."

    if vivi_love < 10: 
        show vivi anger with Dissolve(0.2)
        vivi "I thought you had something important to tell me. If you remember what, call me [player.n]."

    elif vivi_love < 20:
        show vivi with dissolve
        vivi "Excellent, [player.n], if anything happens, you know where to find me!"

    elif vivi_love >= 20:
        show vivi with dissolve
        vivi "What a shame, [player.n]! You know how much I enjoy spending time with you... You know you can count on me!"

        if vivi_lust >= 20:
            vivi "You're leaving so soon?!? I feel so comfortable with you, [player.n]. I want to learn and enjoy so many things with you, I'll come see you later, okay?"
        else:
            vivi "If you need anything else, just call me!"

    jump vivi_bye