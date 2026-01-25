# Version event: 4
# Version game: 0.26

default hancock_blowjob = 0

label event_hancock_blowjob:
    if hancock_blowjob == 0:

        player "[hancock.n] lately we're getting along better and better..."
        player "You no longer have to pretend to be tough and cold, you're truly attractive and sexy when you don't..."
        player "I feel like our relationship isn't the same as it was at the beginning, now we can keep moving forward..."
        show hancock c1 shame with dissolve           
        hancock "Always saying such flattering things about me [player.n]..."
        hancock "What is it that you want to do?"
        player "Kneel down [hancock.n], I'll tell you what to do... Maybe you'll even like it..."

    else:
        player "Every day you're more attractive and sexy, [hancock.n]..."
        player "How about we repeat what we did last time?"
        player "Why don't Kneel down [hancock.n], I know you liked it...."

    call hancock_check pass (check_love = 20, check_lust = 20) from _hancock_check_blowjob

    $ hancock_blowjob += 1

    show hancock neutral with dissolve
    window hide
    window auto
    show hancock c1_naked with dissolve
    pause 0.4

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events hancock blowjob hancock_blowjob_f0
    hide screen screen_black with Dissolve(0.8)

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    pause 1.0

    hancock "(Wow!!!! Why it so huge!!?!)"
    hancock "(Is soo fat, big and burly... So masculine...)"
    hancock "(This smelll too... So obscene and so strong...)"
    hancock "(A young man's dick.... [player.n]'s dick...)"
    hancock "(This is what couples do... And I'm about to do it with [player.n]...)"
    hancock "(I have to stop being mesmerized by his figure and start... I don't want [player.n] to get bored...)"
    hancock "Now I'll start [player.n], I hope I do well!!"

    window hide
    window auto
    show screen screen_black with Dissolve(0.8)
    show events hancock blowjob hancock_blowjob_f1
    hide screen screen_black with Dissolve(0.8)

    hancock "Ooffff your big fat, juicylooking cock"
    hancock "My darling's is so delicious"
    player "(She's getting loose little by little...)"
    player "You are doing very well [hancock.n]... Fuuuckk...."

    jump event_hancock_blowjob_slow


label event_hancock_blowjob_slow:
    window hide
    window auto
    show a_hancock_blowjob with Dissolve(0.2)
    hide a_hancock_blowjob_fast

    pause 3.0

    hancock "(The scent of this cock is making my body react...)"
    hancock "(Ohhhmmm, mnmnm...)"
    hancock "(Just from licking it i'm gonna... Or rather, I already came a bit!!)"
    hancock "Soooo, Sooo delicious.... [player.n]'s cock..."
    hancock "I'm going to milk the cum out of your testicles dont have drop left!"
    hancock "hola, como estas?"
    

    window hide
    window auto
    pause 2.0

    menu:
        "Keep going":
            pause
            jump event_hancock_blowjob_slow

        "Faster":
            jump event_hancock_blowjob_fast


label event_hancock_blowjob_fast:
    window hide
    window auto
    show a_hancock_blowjob_fast with Dissolve(0.2)
    hide a_hancock_blowjob

    pause 3.0
    #dialogos repetitivos
    
    pause 2.0

    menu:
        "Slower":
            jump event_hancock_blowjob_slow

        "Keep going":
            pause
            jump event_hancock_blowjob_fast

        "Cum":
            jump event_hancock_blowjob_cum


label event_hancock_blowjob_cum:
    player "(Fuuck... I'm reaching my limit...She do it so well!)"

    menu:
        "Cum inside":
            jump event_hancock_blowjob_cum_inside

        "Cum outside":
            jump event_hancock_blowjob_cum_outside


label event_hancock_blowjob_cum_inside:
    show events hancock blowjob hancock_blowjob_cum_inside at vibration with hpunch
    hide a_hancock_blowjob_fast
    play sound "cum_01"
    play sound ["deepthroat_01", "<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    hancock "Sooo hot!!"
    hancock "Sooo delicious... [player.n]'s cum is the best..."

    window hide
    window auto
    pause 1.0
    jump event_hancock_blowjob_end



label event_hancock_blowjob_cum_outside:
    show events hancock blowjob hancock_blowjob_cum_outside with hpunch
    hide a_hancock_blowjob_fast
    play sound "cum_01"
    pause 0.1
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 0.2
    with flash
    pause 2.0

    hancock "Looks like you enjoyed it [player.n]!"
    hancock "Look at the mess you made!!"
    hancock "I'll take care of cleaning it up!"

    window hide
    window auto
    pause 1.0
    jump event_hancock_blowjob_end


label event_hancock_blowjob_end:
    window hide
    show screen screen_black with Dissolve(0.6)
    show hancock neutral
    $ ui_interface = True
    hide events hancock blowjob
    hide screen screen_black with Dissolve(0.6)
    
    $ renpy.music.set_volume(1.0, delay=1, channel='music')
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    window auto

    $ hancock_lust += 2
    narrador "[hancock.n] Lust +2"  
    jump hancock_bye


image a_hancock_blowjob:
    "events hancock blowjob hancock_blowjob_f1" with Dissolve(.1)
    pause 0.4
    "events hancock blowjob hancock_blowjob_f2" with Dissolve(.1)
    pause 0.4
    "events hancock blowjob hancock_blowjob_f3" with Dissolve(.2)
    block:
        choice:
            function (frame_sound("blowjob_03", channel="sound"))
        choice:
            function (frame_sound("blowjob_02", channel="sound"))
        choice:
            function (frame_sound("blowjob_mid_01", channel="sound"))

    pause 0.6
    "events hancock blowjob hancock_blowjob_f2" with Dissolve(.1)
    pause 0.4
    repeat

image a_hancock_blowjob_fast:
    "events hancock blowjob hancock_blowjob_f1" with Dissolve(.1)
    pause 0.2
    "events hancock blowjob hancock_blowjob_f2" with Dissolve(.1)
    pause 0.2
    "events hancock blowjob hancock_blowjob_f3" with Dissolve(.2)
    block:
        choice:
            function (frame_sound("blowjob_02", channel="sound"))
        choice:
            function (frame_sound("blowjob_01", channel="sound"))
        choice:
            function (frame_sound("blowjob_mid_01", channel="sound"))
        choice:
            pass
        choice:
            pass

    pause 0.3
    "events hancock blowjob hancock_blowjob_f2" with Dissolve(.1)
    pause 0.2
    repeat