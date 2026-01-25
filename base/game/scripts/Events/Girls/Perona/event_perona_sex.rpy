# Version event: 2
# Version game: 0.7

default perona_doggystyle = 0

label event_perona_sex:
    menu:
        "Vaginal":
            menu event_perona_sex_vaginal:
                "Missionary":
                    narrador "This event is available in version 0.[version_id_next].\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                    jump event_perona_sex_vaginal
                    #jump event_perona_missionary_vaginal

                "Doggystyle":
                    jump event_perona_doggystyle

                "Cowgirl":
                    jump perona_vaginal_cowgirl

                "Back":
                    jump event_perona_sex

        "Back":
            jump event_perona_lewd


label event_perona_doggystyle:

    if perona_doggystyle == 0:
        player "[perona.n], lately I can't get you out of my mind!"
        player "We've had such a close relationship that I think we're ready to take the next step..."
        show perona c1 shame with dissolve
        perona "What are you implying, Captain?!?... It's true that I've been feeling very close to you lately..."
        player "You know!... Getting to know each other deeply, seeing you as you truly are, and enjoying ourselves together..."
        player "Let me teach you new things, I'm sure we'll enjoy it together!... What do you say?"

    else:
        perona "It's good that you're here Captain!"
        show perona c1 shame with dissolve
        perona "I want to feel one with you again!"


    call lewd_perona_check pass (check_love = 25, check_lust = 25) from _lewd_perona_check_doggystyle


    $ perona_doggystyle += 1

    window hide
    show perona neutral c1_naked with dissolve

    pause 0.3

    player "(She is soo sexy!!)"
    perona "Please be gentle Captain..."

    
    play music "music_sexy" fadein 2.0
    $ renpy.music.set_volume(0.1, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events perona doggystyle perona_doggystyle_0
    hide screen screen_black with Dissolve(0.8)


    pause 3.0

    player "Wow, you are so attractive [perona.n]... Rest assured that I will take care of you." 
    player "You don't need to worry about anything, just relax."
    perona "(I cant wait to fell his dick slip into my pussy...)"
    perona "(I want him to go as far as he wants...)"
    perona "(I want him fill me up...)"
    perona "(Ohh my god...)"
    perona "(I feel his cock so close, yet so far away....)"
    perona "(I'm sooo excited...)"
    player "[perona.n]??"
    perona "Oh!!! S-sorry, I was lost in my thoughts... I trust you..."
    perona "You can start now..."

    show screen screen_black with Dissolve(0.8)
    $ ui_interface = False
    show events perona doggystyle perona_doggystyle_1
    hide screen screen_black with Dissolve(0.8)

    pause 3.0
    play gems "gem_01"
    perona "Oh fuck that so Deep!"
    player "Wow... Your pussy's so tight..."
    perona "(I can't think clearly...)"
    perona "(My mind goes hazy... It feel so good...)"
    perona "(I love that feeling, it relaxes me...)"
    play gems "gem_02"
    perona "Mnmnmn... Oh my goodd..."
    player "You're soo wet... I had no idea you were such a slutty girl"
    perona "Y-yesss... Y-esss.."
    player "Hahaha, you can't even speak correctly!"
    perona "Its huuurt a bi-ttt, buuut feelssss soooo Good!"
    play gems "gem_01"
    perona "Oooooh-hh fuuuuck!"
    perona "(I finally feel what its really like to have Captain's cock inside me for the first time...)"
    perona "Goddddd this is amaaazing!"
    player "Fuccck... Your pussy squeezes me so much..."
    player "I can't take it anymore!... Take it all!!"

    #CUM
    show events perona doggystyle perona_doggystyle_cum 
    hide a_perona_doggystyle_speed
    play sound "cum_01"
    play sound ["<silence 0.1>","cum_02","<silence 0.2>","cum_01"]
    with flash
    pause 4.0
    play gems "gem_01"
    perona "Ooohh..."
    perona "(I can't even feel my legs.)"
    perona "(I love thissss!!!!)"

    stop music fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=1, channel='ambient')

    show screen screen_black with Dissolve(0.6)
    $ ui_interface = True
    hide events perona doggystyle
    hide screen screen_black with Dissolve(0.6)
    $ music_time_day()

    player "Wow you were incredible..."  
    perona "It's been incredible Captain, I'm leaving for now, I hope to be able to do it again later!"

    $ perona_lust += 2
    $ perona_love += 2

    narrador "[perona.n] Lust +2 and Love +2"  

    window hide
    show perona c1 with dissolve
    hide perona with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location
