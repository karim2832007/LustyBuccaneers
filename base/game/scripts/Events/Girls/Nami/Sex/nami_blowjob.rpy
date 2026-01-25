# Version event: 1
# Version game: 0.14

default nami_blowjob = 0

label event_nami_blowjob:
    if nami_blowjob == 0:
        player "[nami.n], after so many negotiations, I think I deserve a reward. What do you say we take the next step?!"
        show nami c1 shame with dissolve
        nami "What do you mean by taking the next step? Knowing you, Captain, I can think of several things..."
        player "I want you to help me relax... And I have a very good idea on how to do it with that beautiful mouth of yours."

        $ nami_blowjob += 1

    else:
        player "[nami.n] I want you to help me relax... I need your services again!"
        
    nami "I'm sure I could greatly please you, Captain, but nothing in this life is free..."

    menu:
        "40 berries" if berries >= 40:
            call nami_check pass (check_love = 18, check_lust = 18, check_berries = 40) from _nami_check_blowjob_40
            show nami happy with dissolve

        "Bargain, 20 berries" if berries >= 20:
            call nami_check pass (check_love = 20, check_lust = 20, check_berries = 20) from _nami_check_blowjob_20
            show nami happy with dissolve

        "No payment":
            call nami_check pass (check_love = 22, check_lust = 22, check_berries = 0) from _nami_check_blowjob_0
            show nami neutral with dissolve
            nami "I was thinking of charging you, Captain... but this time, the fun's on me..."

    window hide
    show nami c1_naked with dissolve
    pause 0.4

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events nami blowjob nami_blowjob
    hide screen screen_black with Dissolve(0.8)
    $ renpy.music.set_volume(0.1, delay=1, channel='music')
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')
    play sound [ "blowjob_mid_01","<silence 0.2>","blowjob_02","blowjob_03","blowjob_01","<silence 0.2>","blowjob_01"] loop
    pause 1
    window auto

    nami "(Wooow, how big he is!!, You had everything hidden Captain...)"
    nami "I don't think it will all fit in my mouth..." 
    nami "You got like this for me... you're really perverted [player.n]..."
    player "You have to take responsibility [nami.n]..."
    nami "I hope you're ready... I'm going to make you see stars..."
    #pause 0.4
    nami "I love having a hot cock in my mouth..."
    #pause 0.4
    nami "Feels good, right?... I can see it in your expression..."
    nami "I'm going to help you relax..."
    #pause 0.4
    nami "nnm... nmnm... *Suck*... *Suck*..."
    player "T-this is perfect... You do it so well..."
    nami "*Suck*...*Suck*...nnm... nmnm... *Suck*...*Suck*..."

    window hide
    play sound [ "blowjob_mid_01","deepthroat_01"]
    show events nami blowjob nami_blowjob_cum with Dissolve(0.4)
    with flash
    pause 1.2
    window auto

    player "Ufff you are so good [nami.n]... You do it so well, you are an expert..."
    nami "You got it all out.... So delicious..."
    nami "I'm glad to know you enjoyed it, I loved making you feel good."
    nami "Maybe next time I'll do it for free..."

    window hide
    window auto

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events nami blowjob nami_blowjob
    hide screen screen_black with Dissolve(0.6)

    $ renpy.music.set_volume(1.0, delay=1, channel='music')
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')


    nami "Now if you'll excuse me, I'll continue with my duties..."

    $ nami_lust += 1
    narrador "[nami.n] Lust +1"  

    window hide
    show nami c1_underwear with dissolve
    pause 0.2
    show nami c1 with dissolve

    jump nami_bye