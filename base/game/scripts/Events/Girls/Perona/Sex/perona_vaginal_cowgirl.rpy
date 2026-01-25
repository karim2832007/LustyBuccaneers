# Version event: 3
# Version game: 0.10

default perona_cowgirl = 0

label perona_vaginal_cowgirl:

    if perona_cowgirl == 0:

        player "[perona.n] I can't stop thinking about you... We have to continue getting to know each other, in depth!!!"
        show perona c1 shame with dissolve
        perona "Captain!! You know I would like it, but..."
        player "Don't worry, I'll tell you what to do, you can trust me..."
        show perona c1 shame with dissolve
        perona "Where do we start?"

    else:
        perona "It's good that you're here Captain!"
        show perona c1 shame with dissolve
        perona "I want to feel one with you again!"


    call lewd_perona_check pass (check_love = 30, check_lust = 30) from _lewd_perona_check_cowgirl

    $ perona_cowgirl += 1

    pause 1.0
    window hide
    show perona neutral c1_naked with dissolve

    pause 0.3

    player "Come on top of me!!, I will guide you this time..."
    perona "Of course, Captain! Please be kind..."


    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events perona vaginal cowgirl perona_cowgirl_1 at vibration 
    play gems "nami_gem_1"
    hide screen screen_black with Dissolve(0.8)

    pause 3.0
    window hide
    pause 0.8
    window auto

    player "Wow... Fuck!!"
    player "(Her pussy stretches with every inch I slide my cock into her...)"
    player "You are so beautiful from this angle!!"
    play gems "nami_gem_1"    
    perona "Mmmmfff..."
    player "(Fuck!!... My cock's getting sucked even deeper inside her... Maybe...)"
    player "You are so damn sexy, I love sharing this with you!!"
    perona "Ooohh, oooohh God... Soooo goood..."
    player "(Heheheh they say that winning a girls heart also means winning her pussy!!)"
    player "(Every time I say something sweet to her, her pussy squeezes me like it's the last day)"
    player "(I'am all the way inside her... this warm sensation is just incredible!)"
    player "Wow... Fuck I love it!!"
    play gems "gem_02"
    perona "This feels so hot taht it burns... but ir feels good"
    perona "Ah, ooh... The smeel and the 'taste' of your cock in my pussy, is speading in my head"
    pause 0.5
    perona "Thiiis cooock... Thisss cockk so good.... MY PUSSY WANT'S MORE OF THIS COOOOCK!!"

    window hide
    window auto 

    play gems "nami_gem_2"
    show events perona vaginal cowgirl perona_cowgirl_2 at vibration with vpunch
    
    pause 3.0
    perona "Ohh yess..."
    perona "Sooo fucccking goood!!!!"
    play gems "gem_02"
    perona "(Soooo fattt sooo h-huuuuge, it's still only halfway in... But it's already touching my wooomb)"  
    player "(She is getting out of control!!)"        


    window hide
    window auto

    # Disable vibration
    show events perona vaginal cowgirl perona_cowgirl_2 at truecenter

    play sound "nami_cowgirl_1" fadein 0.5 loop

    show events perona vaginal cowgirl perona_cowgirl_2:
        xalign 0.5 yalign 0.0 zoom 1.02
        linear 0.25 zoom 1.09 yalign 0.1
        ease 0.2 zoom 1.02 yalign 0.0
        repeat

    pause 3.0

    perona "Soo hottt,soooo hardd, sooo faaat... Give me mooore..."
    perona "Fuuuck yeeesss... I will do it faster!, I will doooo it fa- faaaster!"   
    perona "Captain's cock is completely filling my thoughts..."
    perona "My belly is geeetting stuffed... I can't... I can't breatthee!!!"  
    perona "I-I want to cuuum agaain... I waaant to cum Caaaptaaain!!!"
    player "(Fuck she's crazy, it's like another person!!)"
    perona "Inside please!!! I waaant you to cuuuum insiiide me captain!"
    #play gems "gem_02" #mnmnm
    perona "Yeeeeesss!!!"    
    perona "It's feels, really really good... I'am goin to cum!!!!"
    perona "Inside please!!! I waaant you to cuuuum insiiide me captain!"
    perona "Giiiiive me your thiiiick load of cum!!! Fill my pussy pleaseeee"   

    window hide
    pause 0.5
    window auto

    show events perona vaginal cowgirl perona_cowgirl_2_cum at vibration with vpunch
    play sound "cum_01"
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    play gems ["<silence 0.1>","nami_gem_5","<silence 0.3>","nami_gem_6","<silence 0.3>","nami_gem_3","<silence 0.2>","nami_gem_end_1"]
    with flash
    pause 0.2
    with flash
    pause 2.0
    
    perona "I'm cummingggg... yeeessssss"
    perona "Cuuuummingggg..."
    perona "I-iiinsideeeee woooomb!!!"
    player "Fuck... You are totally another person in this state..."
    perona "Diiiickk amazingg!!! Pussy sooooo good..."
    perona "Yeeeeessss!!!"
    player "Let me have a proper look at your face"
    player "You 're making such a lewd face..."
    player "You always make amazing cumming faces!!"

    window hide
    window auto

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events perona doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    player "Wow you were incredible... It was very good!"
    show perona happy with dissolve

    $ talk_random = renpy.random.choice([
        _("Sorry Captain, I lost control... Thanks anyway, until next time!"),
        _("It was sooo good... I hope to repeat it soon Captain!"),
    ])

    perona "[talk_random]"
    
    $ perona_lust += 2
    $ perona_love += 2
    narrador "[perona.n] Lust +2 and Love +2"  

    window hide
    show perona c1 with dissolve
    hide perona with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location
