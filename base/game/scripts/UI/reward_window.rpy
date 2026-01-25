# Version event: 1
# Version game: 0.1

default rewards = []
default n_reward_gold = 0
default n_reward_berries = 0
default n_reward_cannonball = 0

label rewards_give:
    $ rewards = []

    if n_reward_gold > 0:
        $ rewards.append((n_reward_gold, "gold"))
        $ gold += n_reward_gold
        $ n_reward_gold = 0

    if n_reward_berries > 0:
        $ rewards.append((n_reward_berries, "berries"))
        $ berries += n_reward_berries
        $ n_reward_berries = 0

    if n_reward_cannonball > 0:
        $ rewards.append((n_reward_cannonball, "cannonball"))
        $ cannonball += n_reward_cannonball
        $ n_reward_cannonball = 0

    call screen reward_window with Dissolve(0.5)
    return

screen reward_window():
    modal True
    zorder 15

    imagebutton:
        idle "black_40"
        hover "black_40"
        action [Return()]

    frame:
        background None
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 525

        add "GUI windows small_window"

        vbox:
            xalign 0.5
            yalign 0.5
            for reward in rewards:
                hbox:
                    spacing 20

                    frame:
                        background None
                        xsize 130
                        ysize 130

                        text "[reward[0]!tu]":
                            font gui.interface_text_font
                            color "#6b5440"
                            xalign 1.0
                            yalign 0.5
                            size 60

                    frame:
                        background None
                        xsize 130
                        ysize 130
                        add "obj_" + reward[1]
            
