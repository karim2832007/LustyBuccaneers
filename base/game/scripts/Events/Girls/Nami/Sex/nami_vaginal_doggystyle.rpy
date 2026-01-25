# Version event: 1
# Version game: 0.14

default nami_doggystyle = 0

label event_nami_doggystyle:

    if nami_doggystyle == 0:

        player "[nami.n] how's everything going? I wanted to tell you that business has been going really well lately!"
        player "Our situation is improving rapidly..."
        show nami happy with dissolve
        nami "That's great, Captain. You know you can always count on me when it comes to finances..."
        player "That's exactly why I was looking for you. I need to relax… I couldn't think of anyone better…"
        show nami neutral with dissolve
        player "This time unlike our previous encounters... I want it all, you know what I mean, right?"
        player "I'll pay well! That's for sure hahaha"


    else:
        nami "Do you want to repeat Captain?"
        nami "I'm delighted... But you know how this works..."

    menu:
        "40 berries" if berries >= 40:
            call nami_check pass (check_love = 20, check_lust = 20, check_berries = 40) from _nami_check_doggystyle_40
            show nami happy with dissolve

        "Bargain, 20 berries" if berries >= 20:
            call nami_check pass (check_love = 22, check_lust = 22, check_berries = 20) from _nami_check_doggystyle_20
            show nami happy with dissolve

        "No payment":
            call nami_check pass (check_love = 24, check_lust = 24, check_berries = 0) from _nami_check_doggystyle_0
            show nami neutral with dissolve
           

    $ nami_doggystyle += 1

    pause 1.0
    window hide
    show nami neutral c1_naked with dissolve

    pause 0.3

    nami "What do you think, Captain? Look at me!!... I expect a lot from you!"
    player "And I will live up to your expectations! Get on all fours!"


    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events nami doggystyle nami_doggystyle_0
    hide screen screen_black with Dissolve(0.8)


    pause 3.0
    window hide
    pause 0.8
    window auto

    player "Ufff... what good views I have here..."
    play gems "gem_01"
    nami "You see this pussy?"
    nami "This hot wet wanting pussy?"
    nami "It's like this... Beacuse i want you soooo bad!!"
    nami "Its all yours"
    nami "It wants you. It needs you"
    nami "Just please come take it... Don't make me wait any longer!"
    player "I love when you talk like that!! I won't make you wait any longer..."

    show screen screen_black with Dissolve(0.8)
    show events nami doggystyle nami_doggystyle_1
    hide screen screen_black with Dissolve(0.8)

    pause 3.0

    play gems "gem_01"
    nami "Ohh yess..."
    nami "Fuck that's Good.."
    nami "Yes... like that..."
    pause 1.0
    play gems "gem_02"
    nami "Mnnmnm... I love your cock!!"
    nami "It's so goood!!"
    player "Fuuuuck... You're so wet, I can't take it anymore!"
    nami "Yes!!! Yes!!!"
    play gems "gem_01"
    nami "Ohh yess..."
    nami "I wanted it Deep in me!!! I still want it!!!!"
    nami "Your cock! Your cum! You!!"
    nami "All of you!!"
    nami "I want you inside me so bad!"

    show events nami doggystyle nami_doggystyle_cum 
    hide a_nami_doggystyle_speed
    play sound "cum_01"
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 4.0
    play gems "gem_01"
    nami "Ooohh..."

    nami "Good job, Captain!... To think I was going to charge you for this..."

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    window hide
    pause 0.5
    window auto

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events nami doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    player "Wow you were incredible..."
    show nami happy with dissolve
    nami "You weren't bad at all for the first time... If you always do it so well, I'll think about not charging you next time!"

    $ nami_lust += 2
    $ nami_love += 2
    narrador "[nami.n] Lust +2 and Love +2" 

    window hide
    show nami c1_underwear with dissolve
    pause 0.2
    show nami c1 with dissolve

    jump nami_bye

