# Version event: 2
# Version game: 0.38

label nami_bathroom:
    $ _window_hide()
    show screen screen_black with Dissolve(0.6)

    $ ui_interface = True
    $ game.location = "ship_bathroom"
    scene BG locations:
        blur 3

    play ambient "shower" fadein 1.0
    
    hide screen screen_black with Dissolve(0.3)

    narrador "As I step inside, I can hear the water running from the shower."
    player "(Looks like [nami.n]'s taking a bath... I knew I shouldn't come in, but...)"
    player "(The temptation is too strong...)"
    pause 0.5
    player "(It would be incredible if I could spy a little...)"
    player "(But if she catches me... I'll definitely be dead!!!)"
    player "(What should I do... the risk is huge... But the reward... it's unimaginable!!!!)"


    menu m_nami_bathroom:
        narrador "[nami.n] is taking a bath. What do you want to do?"
        "Peek inside":
            jump nami_bathing

        "Take [nami.n]'s panties" if Haki.h == 5 and not haki_nami_panties:
            jump haki_h5_nami

        "Back":
            jump ship_mid
