# Version event: 3
# Version game: 0.31

label event_yamato_sex:
    menu:
        "Vaginal":
            menu:
                "Doggystyle":
                    jump event_yamato_doggystyle_vaginal

                "Cowgirl":
                    jump yamato_vaginal_cowgirl

                "Back":
                    jump event_yamato_sex

        "Back":
            jump event_yamato_lewd


label event_yamato_doggystyle:


    if yamato_doggystyle == 0:

        player "[yamato.n], after so many moments lived, I think it's time to train seriously..."
        yamato "What do you mean, Captain?!? I always train seriously..."
        player "Not like what I'm about to show you now..."
        player "This is a special training... First, I need you to get naked for me... What do you say?"


    else:
        yamato "Captain!! I've been waiting for you..."
        yamato "Since the last time we trained, I can't stop thinking about you... I need a new session right now!"

    call lewd_yamato_check pass (check_love = 25, check_lust = 25) from _lewd_yamato_check_doggystyle


    $ yamato_doggystyle += 1

    window hide
    show yamato neutral c1_naked with dissolve

    pause 0.3

    yamato "I already knew where you were going with this... Do you like what you see?"
    yamato "Let's see if you're up to the challenge... Let's see how fit you are..."

    
    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events yamato a_doggystyle yamato_doggystyle_f1
    hide screen screen_black with Dissolve(0.8)

    pause 1.0
    
    show events yamato a_doggystyle yamato_doggystyle_f2 with Dissolve(0.4)
    pause 1.0

    yamato "Niiice cock Captain..."

    pause 0.5
    show events yamato a_doggystyle yamato_doggystyle_f3 with Dissolve(0.6)
    play sound "doggystyle_01"
    pause 0.1
    play gems "gem_01"
    pause 1.0

    show events yamato a_doggystyle yamato_doggystyle_f2 with Dissolve(0.2)
    pause 0.2

    #ANIMACION
    show a_yamato_doggystyle with Dissolve(0.2)

    # POSIBLE TEXTO CON TIEMPO LARGO PARA MOSTRAR ANIMACION
    yamato "I wish we had done this so much sooner!"
    yamato "I'm going to show you some of my moves Captain..."
    yamato "Just like you wanted, right?"
    yamato "Oh god! It's sooo big!"
    yamato "I love the way it fills me so much!"
    yamato "Just enyoing every inch of you..."
    yamato "Nmnmn... you like it when i talk dirty?"
    player "Fuck, I love it!!!!!"

    pause 2.0
    yamato "I love when my hot fucking Captain stretches my trained pussy with his big fat cooock!!"
    yamato "That feels sooo good!"
    yamato "I love how hot it is..."
    pause 3.0
    yamato "Nnm... nmnm... Ahhh.."
    pause 4.0

    #SPEED
    show a_yamato_doggystyle_speed with Dissolve(0.2)
    hide a_yamato_doggystyle

    pause 3.0
    yamato "(He's doing it faster... omfgood!!)"
    yamato "Come on and fuck me with that big, manly cock of yours!!"
    pause 8.0
    yamato "(Omg... Omgg!!!!)"
    yamato "I love the  feeling i get when your huge dick fills me up just right!!"
    pause 1.0
    player "Fuuuuck... I can't take it anymore!!!"
    yamato "Yesss!!... Cum for mommy baby!!!, make me cum my brains out for you!"
    pause 1.0

    show events yamato a_doggystyle yamato_doggystyle_cum 
    hide a_yamato_doggystyle_speed
    play sound "cum_01"
    with Dissolve(0.4)
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 2.0

    yamato "Ooohh... Shitt... That was really good!!"

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events yamato doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    player "Wow so intense [yamato.n]..."
    yamato "I had a great time Captain, but you need a little more cardio hehe... We will improve it the next time!"

    window hide
    show yamato c1 with dissolve
    hide yamato with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location


image a_yamato_doggystyle:
    "events yamato a_doggystyle yamato_doggystyle_f1" with Dissolve(.1)
    pause 0.4
    "events yamato a_doggystyle yamato_doggystyle_f2" with Dissolve(.1)
    pause 0.4
    "events yamato a_doggystyle yamato_doggystyle_f3" with Dissolve(.2)
    function (frame_sound("doggystyle_01"))
    block:
        choice:
            function (frame_sound("gem_01", channel="gems"))
        choice:
            function (frame_sound("gem_02", channel="gems"))
        choice:
            pass

    pause 0.6
    "events yamato a_doggystyle yamato_doggystyle_f2" with Dissolve(.1)
    pause 0.4
    repeat

image a_yamato_doggystyle_speed:
    "events yamato a_doggystyle yamato_doggystyle_f1" with Dissolve(.1)
    pause 0.2
    "events yamato a_doggystyle yamato_doggystyle_f2" with Dissolve(.1)
    pause 0.2
    "events yamato a_doggystyle yamato_doggystyle_f3" with Dissolve(.2)
    function (frame_sound("doggystyle_01"))
    block:
        choice:
            function (frame_sound("gem_01", channel="gems"))
        choice:
            function (frame_sound("gem_02", channel="gems"))
        choice:
            pass
        choice:
            pass

    pause 0.3
    "events yamato a_doggystyle yamato_doggystyle_f2" with Dissolve(.1)
    pause 0.2
    repeat