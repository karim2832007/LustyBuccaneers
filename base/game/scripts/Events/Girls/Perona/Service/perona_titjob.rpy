# Version event: 2
# Version game: 0.14

default perona_titjob = 0

label event_perona_titjob:
    if perona_titjob == 0:
        player "How are you, [perona.n]?...  we're really starting to enjoy spending time together."
        show perona c1 shame with dissolve        
        perona "It's all thanks to you, [player.n]..."
        player "Let's try something new this time..."
        player "Kneel down [perona.n], I'll tell you what to do... You'll help me relax, maybe you'll even like it..."

    else:
        player "How are you [perona.n]?? ... what do you think if we have a new session like the last time..."
        player "We're really starting to enjoy spending time together!"
        show perona c1 shame with dissolve  
        perona "That sounds pretty good, i feel like this time i'll be able to do even better..."
        player "I have no doubt about that, now get on your knees [perona.n], be a good girl..."


    call lewd_perona_check pass (check_love = 35, check_lust = 35) from _lewd_perona_check_titjob

    $ perona_titjob += 1

    show perona neutral with dissolve
    window hide
    window auto
    show perona c1_naked with dissolve
    pause 0.4

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events perona titjob perona_titjob_f0
    hide screen screen_black with Dissolve(0.8)

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    pause 1.0

    perona "[player.n]'cock is so big... Is so, soo amazing"
    perona "It's so hard... it smells so good too... it's very manly..."
    perona "it feels supergoooood to have your cock between my tits..."
    perona "I hope you're enjoying it as much as I am!"
    perona "The smell's making me dizzy..."
    perona "I love it!!!"


    jump event_perona_titjob_slow


label event_perona_titjob_slow:
    window hide
    window auto
    show a_perona_titjob with Dissolve(0.2)
    hide a_perona_titjob_fast

    pause 3.0

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            pause
            jump event_perona_titjob_slow

        "Faster":
            jump event_perona_titjob_fast


label event_perona_titjob_fast:
    window hide
    window auto
    show a_perona_titjob_fast with Dissolve(0.2)
    hide a_perona_titjob

    pause 3.0
    #dialogos repetitivos´
    
    $ talk_random = renpy.random.choice([
        _("I want yo so badly... But first things first, I want you to cum for my!"),
        _("Are you enjoying it as much as I am!?!, let it all outside for me!!"),
    ])

    perona "[talk_random]"
    
    window hide
    window auto
    pause 2.0

    menu:
        "Slower":
            jump event_perona_titjob_slow

        "Keep going":
            pause
            jump event_perona_titjob_fast

        "Cum":
            jump event_perona_titjob_cum


label event_perona_titjob_cum:
    show events perona titjob perona_titjob_cum with hpunch
    hide a_perona_titjob_fast
    play sound "cum_01"
    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    perona "Uwaahhh it's flying everywhere!!"
    perona "You're gettin it al over my face [player.n]!"
    perona "Look at all this thick and rich cum of yours!!!"
    perona "I love it!!!"
    perona "We can continue later! or not?"

    window hide
    window auto
    pause 1.0
    jump event_perona_titjob_end


label event_perona_titjob_end:
    window hide
    show screen screen_black with Dissolve(0.6)
    show perona neutral
    $ ui_interface = True
    hide events perona titjob
    hide screen screen_black with Dissolve(0.6)
    
    $ renpy.music.set_volume(1.0, delay=1, channel='music')
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    window auto

    $ perona_lust += 2
    narrador "[perona.n] Lust +2"  

    window hide
    show perona c1_underwear with dissolve
    pause 0.2
    show perona c1 with dissolve

    jump perona_bye


image a_perona_titjob:
    "events perona titjob perona_titjob_f0" with Dissolve(.05)
    pause 0.2
    "events perona titjob perona_titjob_f1" with Dissolve(.05)
    pause 0.2
    "events perona titjob perona_titjob_f2" with Dissolve(.05)
    pause 0.2
    "events perona titjob perona_titjob_f3" with Dissolve(.05)
    block:
        choice:
            function (frame_sound("titjob_1", channel="sound"))
        choice:
            pass

    pause 0.3
    repeat

image a_perona_titjob_fast:
    "events perona titjob perona_titjob_f0" with Dissolve(.05)
    pause 0.1
    "events perona titjob perona_titjob_f1" with Dissolve(.05)
    pause 0.1
    "events perona titjob perona_titjob_f2" with Dissolve(.05)
    pause 0.1
    "events perona titjob perona_titjob_f3" with Dissolve(.05)
    block:
        choice:
            function (frame_sound("titjob_1", channel="sound"))
        choice:
            pass

    pause 0.2
    repeat