# Version event: 3
# Version game: 0.13

label event_alvida_sex:
    menu:
        "Vaginal":
            menu:
                "Doggystyle":
                    jump event_alvida_doggystyle

                "Cowgirl":
                    jump event_alvida_cowgirl

                "Back":
                    jump event_alvida_sex

        "Back":
            jump event_alvida_lewd


label event_alvida_doggystyle:
    player "I will teach you to respect me!"
    player "Take off your clothes and get on all fours on the bed!"
    alvida "What? You can't be serious..."
    alvida "You're just a small-time pirate! Who do you think you are!?!"
    player "I'm not giving you an option, [alvida.n]. Do as I say..."
    player "You're on my ship now... You have no power here!"
    alvida "I can't believe this is happening..."
    player "Now, move. I don't have all day..."
    player "I warn you... you don't want to see me angry."
    alvida "Fine... I'll do as you say... But don't think I'll forget this!!"
    player "You're right, you'll never forget... my cock!"

    window hide
    show alvida c1_naked with dissolve

    pause 0.3

    player "That's it, just the way I like it. Good girl."
    alvida "Let's end this!"    
    player "I like what I see...Now you're the one who's eager."
    alvida "..."
    alvida "I can't believe it...."
    alvida "Big talk, but I bet you won't last a second..."
    player "Hahaha... you'll see!"
    player "Now to bed..."

    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events alvida doggystyle alvida_doggystyle_f1
    hide screen screen_black with Dissolve(0.8)
    
    pause 3.0

    player "Wow, what a beautiful view."
    player "You don't look so strong and threatening now..."
    alvida "Shut up and get this over with!!!"
    player "You still don't understand who's in charge here, but don't worry... you will!"

    pause 0.5
    show events alvida doggystyle alvida_doggystyle_f2 with Dissolve(0.4)
    pause 1.0

    alvida "(What the hellll!?!)"
    alvida "(This simple pirate has a huge one...)"
    player "What's with that face? Do you like what you see?..."
    pause 0.5
    show events alvida doggystyle alvida_doggystyle_f3 with Dissolve(0.6)
    pause 1.0
    alvida "Nnm..."
    player "Take it easy, we haven't even started yet..."
    pause 0.5
    player "Are you ready?"
    alvida "(If he introduces something so big... I won't be able to handle it!)"
    alvida "Wait, can we talk about thhh.."

    pause 0.5
    show events alvida doggystyle alvida_doggystyle_f4 with Dissolve(0.4)
    play gems "gem_02"
    pause 0.2
    alvida "iiisssss.."   
    alvida "Nnm... nmnm..."
    alvida "Ommgg... nmnm..."

    show events alvida doggystyle alvida_doggystyle_f5 with Dissolve(0.2)
    play sound "blowjob_mid_01"
    show events alvida doggystyle alvida_doggystyle_f6 with Dissolve(0.1)
    play sound "doggystyle_01"
    pause 0.1
    play gems "gem_01"

    pause 0.3
    alvida "Ahhh.."
    alvida "It's huge!"

    #ANIMACION
    show a_alvida_doggystyle with Dissolve(0.2)

    pause 3.0
    alvida "That feels good!"
    pause 2.0
    player "Do you like it that much? I didn't think you'd surrender to pleasure so quickly..."
    pause 2.0
    alvida "(At this rate, I won't be able to hold on for much longer....)"
    pause 7.0
    alvida "Nnm... nmnm... Ahhh.."
    pause 7.0
    alvida "(I love it!!!!)"
    pause 5.0

    #SPEED
    show a_alvida_doggystyle_speed with Dissolve(0.2)
    hide a_alvida_doggystyle

    pause 3.0
    alvida "(He's doing it faster... I can't take it anymore!!)"
    pause 8.0
    alvida "(Omg....Omgg!!!!)"
    pause 1.0
    alvida "(Yesss!!... Cum for mommy baby!!!)"
    pause 1.0

    show events alvida doggystyle alvida_doggystyle_cum 
    hide a_alvida_doggystyle_speed
    play sound "cum_01"
    with Dissolve(0.4)
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 4.0
    alvida "Ooohh... Shitt..."

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events alvida doggystyle
    hide screen screen_black with Dissolve(0.6)
    player "Hahaha! It seems like you enjoyed it in the end..."
    alvida "..."
    player "That's all, [alvida.n]. You can go now..."
    alvida "This won't end here... we'll meet again..."

    hide alvida with moveoutright
    player "I knew she wouldn't forget... I'll be waiting for the next one!"
    
    stop music fadeout 2.0
    pause 0.5
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    $ music_time_day()
    
    $ game.clock.next()
    jump expression game.location


image a_alvida_doggystyle:
    "events alvida doggystyle alvida_doggystyle_f4" with Dissolve(.1)
    pause 0.4
    "events alvida doggystyle alvida_doggystyle_f5" with Dissolve(.1)
    pause 0.4
    "events alvida doggystyle alvida_doggystyle_f6" with Dissolve(.2)
    function (frame_sound("doggystyle_01"))
    block:
        choice:
            function (frame_sound("gem_01", channel="gems"))
        choice:
            function (frame_sound("gem_02", channel="gems"))
        choice:
            pass

    pause 0.6
    "events alvida doggystyle alvida_doggystyle_f5" with Dissolve(.1)
    pause 0.4
    repeat

image a_alvida_doggystyle_speed:
    "events alvida doggystyle alvida_doggystyle_f4" with Dissolve(.1)
    pause 0.2
    "events alvida doggystyle alvida_doggystyle_f5" with Dissolve(.1)
    pause 0.2
    "events alvida doggystyle alvida_doggystyle_f6" with Dissolve(.2)
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
    "events alvida doggystyle alvida_doggystyle_f5" with Dissolve(.1)
    pause 0.2
    repeat