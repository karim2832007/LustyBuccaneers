# Version event: 4
# Version game: 0.5

label thriller_bark_mansion():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ game.location = "thriller_bark_mansion"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_thriller_bark_mansion

label m_thriller_bark_mansion():
    if ThrillerBark.h == 4:
        window hide
        pause 1.0
        window auto

        show robin at center with dissolve       
        robin "We finally arrived at the mansion! It's quite old and architecturally elegant..."
        hide robin with dissolve

        window hide
        pause 1.0
        window auto
        
        show yamato at center with dissolve

        yamato "Let's be cautious. After everything we've been through, we don't know what or who could be inside..."

        show yamato:
            linear 0.4 xalign 0.85

        pause 0.4

        show nami with dissolve:
            yalign 1.0
            xalign 0.15       
        nami "Maybe we'll find some treasure!!!"
        yamato "Heheheh... You get so brave when there's something valuable involved!"
        nami "There's nothing to fear!... As long as I don't get separated from you all!"

        $ ThrillerBark.h = 5

    menu:
        "Enter the castle":
            jump tb_mansion_01

        "Back":
            jump thriller_bark_mid
