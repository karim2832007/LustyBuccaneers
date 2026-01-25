# Version event: 1
# Version game: 0.28

label uta_refuse:
    show uta anger with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("You was so polite when we first met, I can't believe he's letting me down like this... I'll go think about what happened, don't look for me."),
        _("I'm surprised by what you're telling me... I... I... I don't know what to say, I think you're overstepping your bounds here!"),
        _("I don't know why you feel so close to propose this to me, but I'll pretend nothing happened!"),
    ])

    uta "[talk_random]"
    uta "It's better if I don't see you until my anger passes...."

    $ uta_love -= 1
    $ uta_lust -= 1

    narrador "[uta.n] Love -1 and Lust -1"

    player "(Perhaps I should have waited a bit before moving forward with this...)"

    jump uta_bye