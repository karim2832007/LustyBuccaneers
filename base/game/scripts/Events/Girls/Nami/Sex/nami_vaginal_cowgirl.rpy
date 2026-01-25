# Version event: 1
# Version game: 0.14

default nami_cowgirl = 0

label nami_vaginal_cowgirl:
    if nami_cowgirl == 0:
        player "[nami.n] how are you? I'm here for you again..."
        nami "Captain! I'm fine, luckily! How can I help you?"
        player "I want to relax a bit again..."
        player "You're so good at it... You know exactly what I like, and what I want..."
        show nami c1 shame with dissolve
        nami "Hehe! At it again, Captain..."
        nami "You know I'd love to do it... But nothing in this world is for free... Especially when one knows their worth!"
        player "And you really worth it! That's not a problem!"

    else:
        nami "Do you want to repeat Captain?"
        nami "I'm delighted... But you know how this works..."


    menu:
        "40 berries" if berries >= 40:
            call nami_check pass (check_love = 25, check_lust = 25, check_berries = 40) from _nami_check_cowgirl_40
            show nami happy with dissolve

        "Bargain, 20 berries" if berries >= 20:
            call nami_check pass (check_love = 27, check_lust = 27, check_berries = 20) from _nami_check_cowgirl_20
            show nami happy with dissolve

        "No payment":
            call nami_check pass (check_love = 30, check_lust = 30, check_berries = 0) from _nami_check_cowgirl_0
            show nami neutral with dissolve
           

    $ nami_cowgirl += 1

    pause 1.0
    window hide
    show nami neutral c1_naked with dissolve

    pause 0.3

    player "Always ready! And without a doubt... You're so sexy!"
    player "Come on top of me this time! Let me guide you!"
    nami "Of course, Captain! I hope we both enjoy it!"


    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events nami vaginal cowgirl nami_cowgirl_1 at vibration
    play gems "nami_gem_1"
    hide screen screen_black with Dissolve(0.8)

    pause 3.0
    window hide
    pause 0.8
    window auto

    player "Wow... Fuck!!"
    nami "(Yeeeesssss... It's going in... Sooo deep!)"
    nami "Ahhh, mmf... Ahhh..."
    nami "It's feels, really really good Captain!!"
    nami "All the wat to the back!"

    play gems "gem_02"

    nami "Mmmmfff"
    nami "Fuuuuck!!"
    pause 1.0
    nami "I can't take it anymore, let's fuuuck!"
    window hide
    window auto 


    play gems "nami_gem_2"
    show events nami vaginal cowgirl nami_cowgirl_2 at vibration with vpunch
    
    pause 3.0
    nami "Ohh yess..."
    nami "It's in, so... sooo deep!!"
    play gems "gem_02"
    nami "Right theeere!!!"
    player "(My cock is getting sucked even deeper inside her!!!)"

    window hide
    pause 1.0
    play gems "gem_02" #mnmnm
    window auto

    # Disable vibration
    show events nami vaginal cowgirl nami_cowgirl_2 at truecenter

    play sound "nami_cowgirl_1" fadein 0.5 loop

    show events nami vaginal cowgirl nami_cowgirl_2:
        xalign 0.5 yalign 0.0 zoom 1.02
        linear 0.25 zoom 1.09 yalign 0.1
        ease 0.2 zoom 1.02 yalign 0.0
        repeat

    pause 3.0

    nami "I've never felt anything like this before... It's reaching all the way to my womb..."
    player "(She is leaking like crazy!!!... Fuuuck!!)"
    nami "Riiight theeere!!!"
    nami "M....my hips wont stooop moving!"
    #play gems "gem_02" #mnmnm
    nami "(My insides!!!... My iiiinsides!!!, Heee's crushing my insidessss!)"
    player "Wow!!! you are riding me like a crazy bitch [nami.n]!!"
    nami "I... I'm... Floating... (Whenever his... big cock, hits me deeeeep... I float...)"
    nami "Fuuuuck, yeeeeessss!!"
    nami "It's coming..... gummiingg gyuummiinngg"
    nami "i'm cummingggg"
    player "Let's cum to-gether!!"

    window hide
    window auto

    show events nami vaginal cowgirl nami_cowgirl_2_cum at vibration with vpunch
    play sound "cum_01"
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    play gems ["<silence 0.1>","nami_gem_5","<silence 0.3>","nami_gem_6","<silence 0.3>","nami_gem_3","<silence 0.2>","nami_gem_end_1"]
    with flash
    pause 0.2
    with flash
    pause 2.0
        
    nami "nfaah!!, Aah, aahh"
    nami "Ohh, ohh i'm cummingggg... Oh oh..."
    player "Fuck... Your pussy's throbbing like crazy, i guess it was a big orgasm wasn't it?"
    nami "Aah he... he eek... It's leaking out!"
    nami "Ahhh, mmf... mnghoo hogh nguhh, eek aah..."
    nami "Captain's cooooock... Is so amazing.... eeh eek.."
    player "Hahaha wtf... Your brain is melted or what?!?"
    player "If you keep cuming like this, I'm going to have to charge you."


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

    player "Wow you were incredible... It was very good"
    show nami happy with dissolve
    
    $ talk_random = renpy.random.choice([
        _("Very, very good indeed!, next time, I might not charge you hehe!"),
        _("That was really really good! Until next time Captain!."),
    ])

    nami "[talk_random]"

    $ nami_lust += 2
    $ nami_love += 2
    narrador "[nami.n] Lust +2 and Love +2" 


    window hide
    show nami c1_underwear with dissolve
    pause 0.2
    show nami c1 with dissolve

    jump nami_bye

