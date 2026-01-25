# Version event: 2
# Version game: 0.12

label robin_refuse:
    show robin anger with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("I can't believe you're telling me this.... I don't know why you think we have that much trust"),
        _("I didn't think you'd be so brazen with me, Captain..."),
        _("You have a lot of nerve asking me this... Your way of thinking is quite childish..."),
    ])

    robin "[talk_random]"
    robin "I'd better continue with my research... I'll pretend like nothing happened here..."

    $ robin_love -= 1
    $ robin_lust -= 1

    narrador "[robin.n] Love -1 and Lust -1"

    player "(Perhaps I should have waited a bit before moving forward with this...)"

    jump robin_bye