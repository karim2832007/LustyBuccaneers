# Version event: 4
# Version game: 0.12

# vatiables
default yamato_blowjob = 0

label event_yamato_services:
    menu:
        "Handjob":
            jump event_yamato_handjob

        "Blowjob":
            jump event_yamato_blowjob

        "Titjob":
            #. narrador "This event is available in version 0.12.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
            #. jump event_yamato_services 
            jump event_yamato_titjob

        "Back":
            jump event_yamato_lewd

label event_yamato_blowjob:
    if yamato_blowjob == 0:
        player "[yamato.n], now that we know each other more intimately, what do you say about taking the next step?!"
        show yamato c1 shame with dissolve        
        yamato "What do you mean by taking the next step? Are you thinking of a new training regimen?"
        player "Well, it's something new, I don't know if you have experience, but I'm going to teach you... it's with your mouth! Kneel down, I'll tell you what to do..."

        $ yamato_blowjob += 1

    else:
        player "[yamato.n], I was just looking for you. I need your help... It's time to continue with your training!"
        yamato "Excellent, Captain! I'm sure I'll do much better if we continue with our sessions..."


    call lewd_yamato_check pass (check_love = 20, check_lust = 20) from _lewd_yamato_check_blowjob

    show yamato neutral with dissolve
    window hide
    show yamato c1_naked with dissolve
    pause 0.4

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events yamato blowjob yamato_blowjob
    hide screen screen_black with Dissolve(0.8)
    $ renpy.music.set_volume(0.1, delay=1, channel='music')
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')
    play sound [ "blowjob_mid_01","<silence 0.2>","blowjob_02","blowjob_03","blowjob_01","<silence 0.2>","blowjob_01"] loop
    pause 1
    window auto

    yamato "(Wow, it's sooo big!!!)"
    player "(She is slowly bringing her nose closer to the tip of my glans, being able to even feel her breathing)"
    yamato "Mmm, that smell is so good... so strong, so masculine...."
    yamato "I love smelling it so close to my nose..."
    player "I'm glad to know you like it, now start sucking it, I'm sure you'll like it even more..."
    yamato "I'm new to this, Captain... I hope to learn and do it well..."

    player "Don't worry, you're doing fantastically..."
    player "Your lips feel sooo good, you were born to do this... With a little practice you will be an expert"
    yamato "It fills my mouth too much..."
    yamato "Mnnmnm it's so hard..."
    yamato "*Lick*...*Lick*...*Lick*..."
    yamato "*Kiss*...*Kiss*...*Kiss*..."

    window hide
    play sound [ "blowjob_mid_01","deepthroat_01"]
    show events yamato blowjob yamato_blowjob_cum with Dissolve(0.4)
    with flash
    pause 1.2
    window auto

    player "Ufff you're so good [yamato.n]... You do it so well..."
    yamato "I'm glad to know you enjoyed it, it makes the effort worthwhile..."
    yamato "I'm sure that little by little, with more training, I'll do better!"

    window hide
    show screen screen_black with Dissolve(0.6)
    show yamato neutral
    $ ui_interface = True
    hide events yamato blowjob yamato_blowjob
    hide screen screen_black with Dissolve(0.6)
    $ renpy.music.set_volume(1.0, delay=1, channel='music')
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')
    window auto

    player "There will be more opportunities, I'm sure of it!..."

    $ talk_random = renpy.random.choice([
        _("Now if you'll excuse me, I'll continue with my training..."),
        _("Now, if you'll excuse me, I'll get back to my training. I'll be here whenever you need me!"),
        _("Until next time, Captain! I'll continue with my training!"),
    ])

    yamato "[talk_random]"

    $ yamato_lust += 1
    narrador "[yamato.n] Lust +1"  

    jump event_yamato_lewd_end


                