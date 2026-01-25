# Version event: 1
# Version game: 0.14

label nami_refuse:
    show nami anger with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("If you're not interested in reaching an agreement, don't waste my time."),
        _("You're not very good at negotiating, are you, Captain?... Let's not waste any more time..."),
        _("You don't seem very interested in reaching an agreement... Maybe next time you'll have a better proposal..."),
    ])

    nami "[talk_random]"
    nami "I better get back to my tasks... I'll pretend like nothing happened here..."

    $ nami_love -= 1
    $ nami_lust -= 1

    narrador "[nami.n] Love -1 and Lust -1"

    player "(Perhaps I should have waited a bit before moving forward with this...)"

    jump nami_bye