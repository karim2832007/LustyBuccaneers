# Version event: 4
# Version game: 0.13

label event_robin_sex:
    menu:
        "Vaginal":
            menu:
                "Doggystyle":
                    jump event_robin_doggystyle_vaginal

                "Cowgirl":
                    jump event_robin_cowgirl

                "Back":
                    jump event_robin_sex

        "Back":
            jump event_robin_lewd


label event_robin_doggystyle:


    if robin_doggystyle == 0:

        player "[robin.n] how are you? I wanted to steal a bit of your time, not sure if you're busy with your research..."
        robin "I was just finishing up, Captain. I can take a small break for some recreation."
        player "Excellent, that's exactly what I was thinking about... Recreation"
        player "Let's study anatomy again, in a fun way... but this time I want an advanced class..."
        show robin c1 shame with dissolve
        robin "I think I know what kind of study you want to pursue..."
        player "Hahah you know me so well [robin.n]... What do you say? I'm a quick learner..."


    else:
        robin "Do you want to repeat, Captain?"
        robin "Surely you took note of the previous opportunity..."

    call lewd_robin_check pass (check_love = 25, check_lust = 25) from _lewd_robin_check_doggystyle


    $ robin_doggystyle += 1



    window hide
    show robin neutral c1_naked with dissolve

    pause 0.3

    player "Soo fucking sexy... You are a naughty teacher..."
    robin "Let's go with the first lesson..."
    robin "Come here..."
    robin "Fill me with your huge dick, Captain..."   

    
    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events robin doggystyle robin_doggystyle_0
    hide screen screen_black with Dissolve(0.8)


    pause 3.0

    player "What an ass..."
    robin "Please do it!! Hurry up…!"
    robin "I'm ready... sooo ready..."
    robin "Please... Give it to me!"
    robin "Just to thinking about it, is making me sooo wet..."
    player "I like it when you get like this... I won't make you wait any longer..."

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events robin doggystyle robin_doggystyle_1
    hide screen screen_black with Dissolve(0.8)

    pause 3.0

    play gems "gem_01"
    robin "Ohh fuck that is Deep!!!"
    robin "Keep fucking me just like that!!"
    robin "(His dick is sooo Huuuge!!)"
    robin "It's soo big!!!"
    robin "It's driving me insane!"
    play gems "gem_02"
    robin "Mnmnmnm... Dont you dare stop!"
    robin "Fuck me just like that"
    robin "Fuck me until you cum all inside me!"
    play gems "gem_01"
    robin "Oh my god th-this is... So insane..."
    player "Sooo hot...I can't take it anymore!"
    robin "Do it cum in me!!!"
    robin "Let me feel you finish inside me!!!"
    robin "Let me feel that cum I love... Fill my naughty cheating teacher pussy!"


    #CUM
    show events robin doggystyle robin_doggystyle_cum 
    play sound "cum_01"
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 4.0
    play gems "gem_01"
    robin "Ooohh..."
    robin "That heat!"
    robin "That sense of fullness"

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events robin doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    player "Wow you were incredible [robin.n]..."
    robin "And there is still a lot to teach you... But that will be the next time...."

    window hide
    show robin c1 with dissolve
    hide robin with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location
