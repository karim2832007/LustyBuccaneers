# Version event: 2
# Version game: 0.12

label hancock_refuse:
    show hancock anger with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("I can't believe you insinuated that! I'm leaving, and if you don't want me to turn you into stone..."),
        _("You're quite bold to propose something like that with so little trust... I'll be leaving for now!"),
        _("I don't know why you feel so close to propose this to me, but I'll pretend nothing happened!"),
    ])

    hancock "[talk_random]"
    hancock "It's better if I don't see you until my anger passes...."

    $ hancock_love -= 1
    $ hancock_lust -= 1

    narrador "[hancock.n] Love -1 and Lust -1"

    player "(Perhaps I should have waited a bit before moving forward with this...)"

    jump hancock_bye