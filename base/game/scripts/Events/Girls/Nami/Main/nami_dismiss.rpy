# Version event: 1
# Version game: 0.14

label nami_dismiss:
    player "That's all, [nami.n]. You can go back to your tasks."

    if nami_love < 10:
        show nami c1 anger with Dissolve(0.2)
        nami "If there's nothing important to do, please try not to waste my time. Time is money, Captain!"

    elif nami_love < 20:
        show nami c1 with dissolve
        nami "No problem, Captain. If you need me for anything else, just call me!"

    elif nami_love >= 20:
        show nami c1 with dissolve
        nami "That's a shame, Captain! I'd like to spend more time with you next time."

        if nami_lust >= 20:
            nami "If you need anything else, call me! I'm completely at your disposal... We can even meet tonight if you prefer!"
        else:
            nami "If you need anything else, just call me!"

    jump nami_bye