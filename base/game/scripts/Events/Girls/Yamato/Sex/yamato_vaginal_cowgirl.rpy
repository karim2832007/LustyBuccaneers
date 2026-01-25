# Version event: 4
# Version game: 0.10

default yamato_cowgirl = 0

label yamato_vaginal_cowgirl:

    if yamato_cowgirl == 0:

        player "[yamato.n] What do you say if we have another one of those... Intimate training sessions..."
        player "One versus one again, without anyone bothering us..."
        show yamato c1 shame with dissolve        
        yamato "I love those kinds of training... But I don't know if we can..."
        player "Don't worry, no one will notice..."

    else:
        yamato "Do you want to train again, Captain?"
        show yamato c1 shame with dissolve 
        yamato "Surely he has much more to show me!!"


    call lewd_yamato_check pass (check_love = 30, check_lust = 30) from _lewd_yamato_check_cowgirl

    $ yamato_cowgirl += 1

    pause 1.0
    window hide
    show yamato neutral c1_naked with dissolve

    pause 0.3

    player "Come on top of me!!, This time we will do some Cowgirl training!!"
    yamato "Of course, Captain! I feel like this lesson will be very interesting..."


    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events yamato vaginal cowgirl yamato_cowgirl_1 at vibration 
    play gems "nami_gem_1"
    hide screen screen_black with Dissolve(0.8)

    pause 3.0
    window hide
    pause 0.8
    window auto
    yamato "Yeeees!!! that's so Good!!!"
    yamato "Sooo fuuuucking gooooood!!!!"
    yamato "What a Good dick!!!"
    player "What a filthy warrior you are..."
    player "Saying that kind of shit so close to the rest of the girls..."
    yamato "Yeeeesssss... A women like me deserve to be punished Captain!!!"
    player "Its that so?"
    yamato "Yees we need discipline"

    play gems "gem_02"

    yamato "Mmmmfff"
    pause 1.0
    yamato "I CAN'T CONTROL MY BODY!!!"

    window hide
    window auto 

    play gems "nami_gem_2"
    show events yamato vaginal cowgirl yamato_cowgirl_2 at vibration with vpunch
    
    pause 3.0
    yamato "Ohh, fuck yes..."
    yamato "Gooood that's Good!!!"
    play gems "gem_02"
    yamato "My pussy is twitchin every time i get fuckee"
    yamato "(Each time he hits me I can feel the hard cock, still stuck deep within me, twitch...)"
    yamato "Yeeeeessss I love your cock!!"
    yamato "How could I have ever hated this... It feels sooo good... More dick!"
    yamato "WHY... DOES IT FEELS SO MUCH BETTER!!!"
    player "Fuuck you are an animal!!!"        
    yamato "Fuck meee... Keep fucking me!!! Fuck me like an animal!!!"

    window hide
    window auto

    # Disable vibration
    show events yamato vaginal cowgirl yamato_cowgirl_2 at truecenter

    play sound "nami_cowgirl_1" fadein 0.5 loop

    show events yamato vaginal cowgirl yamato_cowgirl_2:
        xalign 0.5 yalign 0.0 zoom 1.02
        linear 0.25 zoom 1.09 yalign 0.1
        ease 0.2 zoom 1.02 yalign 0.0
        repeat

    pause 3.0

    yamato "AHH... Omggg I LOVE THIS DICK! PLEASE MORE MORE DICK!!!"
    yamato "MORE I WANT MORE... BANG ME HARDER, GIVE ME YOUR DICK!!!"

    yamato "THIS COCK IS SO... ITS SO GOOD IM LOSIGN MY MIND"
    yamato "Yeeee--ssss... I will do it faster!, gooo fa- faaaster Captain!"    
    yamato "Inside please!!! I waaant you to cuuuum insiiide me captain!"
    yamato "Give me you cummmmmm"
    #play gems "gem_02" #mnmnm
    yamato "Fill meeeee"    
    yamato "filll my pussy completely!!"
    player "Take it all beachh!!"    
    yamato "CUM INSIDE MEEEEEEE IÁM OHHO OHHHH CUMMINGGG....!"

    window hide
    pause 0.5
    window auto

    show events yamato vaginal cowgirl yamato_cowgirl_2_cum at vibration with vpunch
    play sound "cum_01"
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    play gems ["<silence 0.1>","nami_gem_5","<silence 0.3>","nami_gem_6","<silence 0.3>","nami_gem_3","<silence 0.2>","nami_gem_end_1"]
    with flash
    pause 0.2
    with flash
    pause 2.0
    
    yamato "I'm cummingggg... yeeessssss"
    yamato "Inside my womb!!!"
    yamato "H-his seeeed deeep into meee..."
    yamato "Ffflooding my wommmb"
    yamato "Sooo Amazing"
    yamato "My womb is overflowing... I'm filled with seeemenn"
    yamato "Aah he... he he eek..."
    player "You're a bitch when you're in this state..."
    player "Ufff...That was very good... great session!!!!"

    window hide
    window auto

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events yamato doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    player "Wow you were incredible... It was very good"
    show yamato happy with dissolve

    $ talk_random = renpy.random.choice([
        _("Very, very good indeed!, next time let's practice another session!"),
        _("That was really really good! Until next time Captain!"),
    ])

    yamato "[talk_random]"

    $ yamato_lust += 2
    $ yamato_love += 2
    narrador "[yamato.n] Lust +2 and Love +2"  

    window hide
    show yamato c1 with dissolve
    hide yamato with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location
