# Version event: 2
# Version game: 0.12

label hancock_goodbye:
    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, i'll continue with my duties..."),
        _("Now, if you'll excuse me, I'm going to my room to relax for a bit!"),
        _("Until next time, [player.n]! You know where to find me if I can help with anything!"),
    ])

    hancock "[talk_random]"

    jump hancock_bye