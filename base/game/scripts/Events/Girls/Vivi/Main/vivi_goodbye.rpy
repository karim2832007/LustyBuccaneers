# Version event: 2
# Version game: 0.23

label vivi_goodbye:
    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, I'll continue with my duties..."),
        _("Now, if you'll excuse me, I'll be out on the bow relaxing a bit!"),
        _("You know where to find me if I can help with anything! I will be eagerly waiting to help you."),
    ])

    vivi "[talk_random]"

    jump vivi_bye