# Version event: 5
# Version game: 0.14

# vatiables
default perona_blowjob = 0

label event_perona_services:
    menu:
        "Blowjob":
            jump event_perona_blowjob

        "Titjob":
            #narrador "This event is available in version 0.14.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
            #jump event_perona_services
            jump event_perona_titjob

        "Back":
            jump event_perona_lewd

label event_perona_blowjob:
    if perona_blowjob == 0:
        player "How are you, [perona.n]?... Lately, I feel like you've lost all the shyness and embarrassment you had with me... I feel like you really trust me now."
        show perona c1 shame with dissolve        
        perona "It's all thanks to you, [player.n]..."
        player "I think I already know who you really are, but we could become even closer..."
        player "Kneel down [perona.n], I'll tell you what to do... You'll help me relax, maybe you'll even like it..."

        $ perona_blowjob += 1

    else:
        player "How are you [perona.n]?? ... what do you think if we have a new session like the last time..."
        player "You really freed yourself and showed me who you are..."
        show perona c1 shame with dissolve  
        perona "That sounds pretty good, i feel like this time i'll be able to do even better..."
        player "I have no doubt about that, now get on your knees [perona.n], be a good girl..."


    call lewd_perona_check pass (check_love = 20, check_lust = 20) from _lewd_perona_check_blowjob

    perona "I think i know exactly what i have to do captain... I hope to do it well, i don't have much experience..."
    perona "I'll make you feel good... Just relax and leave the rest to me..."

    show perona neutral with dissolve
    window hide
    show perona c1_naked with dissolve
    pause 0.4

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events perona blowjob perona_blowjob
    hide screen screen_black with Dissolve(0.8)
    $ renpy.music.set_volume(0.1, delay=1, channel='music')
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')
    play sound [ "blowjob_mid_01","<silence 0.2>","blowjob_02","blowjob_03","blowjob_01","<silence 0.2>","blowjob_01"] loop
    pause 1
    window auto

    perona "[player.n] is so big..."
    perona "It's so hard... it smells so good too... it's very manly..."
    player "Since you have been with us, I always suffer from constant boners..."
    player "You have to take charge, nothing is stopping you [perona.n]..."
    pause 1.2
    perona "Mnnmnm it's so hard..."
    perona "*Lick*...*Lick*...*Lick*..."
    perona "*Kiss*...*Kiss*...*Kiss*..."
    pause 1.2    
    perona "(I feel so relieved... when I'm sucking the captain's cock)"
    perona "(The captain's precum is a little bitter but it is sweet at the same time...)"
    perona "(It's delicious... I love everything about this cock...)"
    player "The way you use your tongue is wonderful... I feel like you like it more and more..."
    player "Little by little you do it better and better [perona.n]..."
    perona "Thank you very much Captain!"



    window hide
    play sound [ "blowjob_mid_01","deepthroat_01"]
    show events perona blowjob perona_blowjob_cum with Dissolve(0.4)
    with flash
    pause 1.2
    window auto
    #aca a futuro se puede agregar semen encima del pelo de perona por ej
    perona " Everything's all sticky with jizzz, in my mouth, on my face and even in my hair"
    perona " It was so thick… I drank it all"
    player "Wow [perona.n], you did a great job..."
    player "It all seems so natural to you..."
    player "We'll enjoy this many more times, I'm sure..."

    window hide
    show screen screen_black with Dissolve(0.6)
    show perona neutral
    $ ui_interface = True
    hide events perona blowjob perona_blowjob
    hide screen screen_black with Dissolve(0.6)
    $ renpy.music.set_volume(1.0, delay=1, channel='music')
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    window auto

    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, i'll continue with my duties..."),
        _("Now, if you'll excuse me, I'll get back to my work. I'll be here whenever you need me!"),
        _("Until next time, Captain! I'll continue with my work!"),
    ])

    perona "[talk_random]"

    $ perona_lust += 1
    narrador "[perona.n] Lust +1"  

    jump event_perona_lewd_end


                