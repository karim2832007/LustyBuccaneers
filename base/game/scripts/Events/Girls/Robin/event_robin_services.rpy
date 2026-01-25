# Version event: 3
# Version game: 0.3

# vatiables
default robin_blowjob = 0

label event_robin_services:
    menu:
        "Handjob":
            #. narrador "This event is available in version 0.3.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
            jump event_robin_handjob

        "Blowjob":
            #. narrador "This event is available in version 0.3.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
            jump event_robin_blowjob
    
        "Titjob":
            jump robin_titjob

        "Footjob":
            jump event_robin_footjob

        "Back":
            jump event_robin_lewd

label event_robin_blowjob:
    if robin_blowjob == 0:
        player "[robin.n], I was just looking for you... We've been so close lately, what do you say we take the next step?!"
        robin  "Whatever you say, Captain. I'm not sure what you're getting at..."
        player "Well, I've been feeling uncomfortable, and maybe you could help me relax!"
        player "It's here in my crotch... I think you know what I mean!"

        $ robin_blowjob += 1

    else:
        player "[robin.n], I think I'm feeling uncomfortable again!"
        player "I'll need a checkup. I'm sure you'll do well..."
        robin "Perhaps we should seek a doctor, Captain... But for now, I'm delighted to help you with your issue hehe!"


    call lewd_robin_check pass (check_love = 20, check_lust = 20) from _lewd_robin_check_blowjob
    
    show robin c1 shame with dissolve
    robin "Mmm... I think this time it's my turn to do the medical examination, Captain..."
    show robin neutral with dissolve
    robin "Get comfortable here and leave the rest to me... I'll take a look..."

    window hide
    show robin c1_naked with dissolve
    pause 0.4

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events robin blowjob robin_blowjob
    hide screen screen_black with Dissolve(0.8)
    $ renpy.music.set_volume(0.1, delay=1, channel='music')
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')
    play sound [ "blowjob_mid_01","<silence 0.2>","blowjob_02","blowjob_03","blowjob_01","<silence 0.2>","blowjob_01"] loop
    pause 1
    window auto

    robin "Is it this big just because of me??... Or is it due to inflammation..."
    player "Having you looking at my cock like that makes me very horny [robin.n]..."
    robin "It's soooo big... Maybe it's necessary for me to help it expel all the bad stuff..."
    robin "Good thing I learned this technique from a book. Just relax, Captain, let me handle the rest..."
    #pause 1.2
    robin "It fills my mouth too much..."
    robin "Mnnmnm it's so hard..."
    robin "*Lick*...*Lick*...*Lick*..."
    robin "*Kiss*...*Kiss*...*Kiss*..."

    window hide
    play sound [ "blowjob_mid_01","deepthroat_01"]
    show events robin blowjob robin_blowjob_cum with Dissolve(0.4)
    with flash
    pause 1.2
    window auto

    player "Ufff you are so good [robin.n]... You do it so well, you are an expert..."
    robin "You got it all out.... So delicious..."
    robin "I'm glad to know you enjoyed it, it makes the effort worthwhile..."

    window hide
    show screen screen_black with Dissolve(0.6)
    show robin neutral
    $ ui_interface = True
    hide events robin blowjob robin_blowjob
    hide screen screen_black with Dissolve(0.6)
    $ renpy.music.set_volume(1.0, delay=1, channel='music')
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    window auto

    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, i'll continue with my duties..."),
        _("Now, if you'll excuse me, I'll get back to my research. I'll be here whenever you need me!"),
        _("Until next time, Captain! I'll continue with my research!"),
    ])

    robin "[talk_random]"

    $ robin_lust += 1
    narrador "[robin.n] Lust +1"  

    jump event_robin_lewd_end


                