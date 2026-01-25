# Version event: 3
# Version game: 0.11

default nami_titjob = 0

label event_nami_titjob:

    if nami_titjob == 0:

        player "[nami.n] how are you? I'm here for you again..."
        nami "Captain! all good! How can I help you?"
        player "I want to enjoy your services again..."
        show nami c1 shame with dissolve
        nami "Hehe! At it again, Captain..."
        player "You know how beautiful your breasts are, this time I want you to use them for me..."
        nami "You know how this world works Captain..."

    else:
        nami "Do you want another session Captain?"
        nami "I'd love to... But you know how this works..."
        

    menu:
        "40 berries" if berries >= 40:
            call nami_check pass (check_love = 30, check_lust = 30, check_berries = 40) from _nami_check_titjob_40
            show nami happy with dissolve

        "Bargain, 20 berries" if berries >= 20:
            call nami_check pass (check_love = 33, check_lust = 33, check_berries = 20) from _nami_check_titjob_20
            show nami happy with dissolve

        "No payment":
            call nami_check pass (check_love = 35, check_lust = 35, check_berries = 0) from _nami_check_titjob_0
            show nami neutral with dissolve
           

    $ nami_titjob += 1

    pause 1.0
    window hide
    show nami neutral c1_naked with dissolve

    pause 0.3

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events nami titjob nami_titjob_1 at vibration
    hide screen screen_black with Dissolve(0.8)

    pause 3.0
    window hide
    pause 0.8
    window auto

    player "[nami.n], these tits... They are amazing... I've never seen tits as huge as yours!"
    player "Also, you've got such beautifull nipples..."
    nami "Hahaha calm down you little perv!!"
    nami "My initial desire was to just stuff it in my mouth..."
    nami "But... Stuffing this cock between my breasts, that's something else entirely!!!"
    nami "I looove your big, hard and manly cock Captain!!"    
    nami "I'm going to start!!"

    window hide
    window auto
    show screen screen_black with Dissolve(0.8)
    show events nami titjob nami_titjob_2
    hide screen screen_black with Dissolve(0.8)

    show events nami titjob nami_titjob_2 at vibration with vpunch
    
    pause 2.0
    nami "Lubed up with all organic sweat and saliva lotion!!!"
    nami "Let's see how long can you hold out!!"
    player "So rought.... Fuck...."
    player "I'll conquer yout tits properly"
    nami "I'll stroke it lots and lots.... Until your smell runs into my boobs!!"
    nami "Ready too cum yet?!? Just relax and enjoy yourself okay?"

    window hide
    pause 1.0
    window auto

    # Disable vibration
    show events nami titjob nami_titjob_2 at truecenter

    play sound "titjob_1" fadein 0.5 loop

    show events nami titjob nami_titjob_2:
        xalign 0.5 yalign 0.0 zoom 1.02
        linear 0.45 zoom 1.12 yalign 0.8
        ease 0.3 zoom 1.02 yalign 0.0
        repeat
    
    pause 3
    player "Ahhh.... I'm cumming... You clevage makes the best pussy!!!!"
    nami "Let it ouut... Cuum for momy!!!"

    window hide
    pause 0.5
    window auto

    play sound "cum_01"
    show events nami titjob nami_titjob_3 with flash
    show events nami titjob nami_titjob_3 at vibration with vpunch
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2

    pause 3.0

    nami "Ahhhhh you're spurting like a hosee!!"   
    nami "Daaamn, it's so thick and sticky... lumpy too!!"
    nami "You must've been saving up for a lot of time captain!"
    nami "So hot... So filthy..."
    nami "Soooo creamy!!! I love it!"
    nami "Yummy Yummy!!"
    nami "Thanks for the meal!!"

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

    show nami happy with dissolve
    
    nami "You know where to find me if you want to repeat!!"
    nami "It was very very good and funny!!"

    $ nami_lust += 2
    $ nami_love += 2
    narrador "[nami.n] Lust +2 and Love +2" 

    window hide
    show nami c1_underwear with dissolve
    pause 0.2
    show nami c1 with dissolve

    jump nami_bye