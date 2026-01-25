# Version event: 2
# Version game: 0.23

label vivi_refuse:
    show vivi anger with Dissolve(0.2)

    $ talk_random = renpy.random.choice([
        _("You was so polite when we first met, I can't believe he's letting me down like this... I'll go think about what happened, don't look for me."),
        _("I'm surprised by what you're telling me... I... I... I don't know what to say, I think you're overstepping your bounds here!"),
        _("I don't know why you feel so close to propose this to me, but I'll pretend nothing happened!"),
    ])

    vivi "[talk_random]"
    vivi "It's better if I don't see you until my anger passes...."

    $ vivi_love -= 1
    $ vivi_lust -= 1

    narrador "[vivi.n] Love -1 and Lust -1"

    player "(Perhaps I should have waited a bit before moving forward with this...)"

    jump vivi_bye