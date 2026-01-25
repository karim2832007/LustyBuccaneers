# Version event: 3
# Version game: 0.4

label m_alvida_call:
    menu:
        "Lewd":
            jump event_alvida_lewd

        "Dismiss Her":
            player "That's all, [alvida.n]. You can go now..."

            alvida "We'll meet again soon!..."

    window hide
    hide alvida with moveoutright
    pause 0.5

    $ game.clock.next()
    jump expression game.location