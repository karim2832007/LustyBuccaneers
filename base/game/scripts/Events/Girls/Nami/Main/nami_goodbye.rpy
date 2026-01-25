# Version event: 2
# Version game: 0.14

label nami_goodbye:
    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, i'll continue with my duties..."), 
        _("Now, if you'll excuse me, I'll get back to my duties. I'll be here whenever you need me!"),
        _("Until next time, Captain! I'll continue with my tasks!"),
    ])

    nami "[talk_random]"

    jump nami_bye