# Version event: 1
# Version game: 0.28

label uta_dismiss:
    player "That's all [uta.n], you may leave and return to your duties."

    if uta_love < 10: 
        show uta anger with Dissolve(0.2)
        uta "I thought you had something important to tell me. If you remember what, call me [player.n]."

    elif uta_love < 20:
        show uta with dissolve
        uta "Excellent, [player.n], if anything happens, you know where to find me!"

    elif uta_love >= 20:
        show uta with dissolve
        uta "What a shame, [player.n]! You know how much I enjoy spending time with you... You know you can count on me!"

        if uta_lust >= 20:
            uta "You're leaving so soon?!? I feel so comfortable with you, [player.n]. I want to learn and enjoy so many things with you, I'll come see you later, okay?"
        else:
            uta "If you need anything else, just call me!"

    jump uta_bye