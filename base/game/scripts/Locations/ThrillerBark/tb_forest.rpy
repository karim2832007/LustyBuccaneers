# Version event: 3
# Version game: 0.8

default tb_forest = 0
default tb_forest_map = False
default tb_forest_bg = 1

label tb_forest():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ tb_forest_bg = 1
    $ game.location = "tb_forest"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_thrillerbark()
    jump m_tb_forest

label m_tb_forest():
    # IF $ tb_forest = 4

    if not tb_forest_map:
        if tb_forest == 0:        

            show robin at center with dissolve

            robin "The forest here is too dense... There are no marked paths, and there's very little light..."
            robin "There doesn't seem to be a clear path to follow..."

        
            show robin:
                linear 0.4 xalign 0.85

            pause 0.4

            show nami with dissolve:
                yalign 1.0
                xalign 0.5        
        
            nami "If we keep moving forward without a fixed direction, we'll probably end up getting lost here..."
        
            show nami:
                linear 0.4 xalign 0.15

            pause 0.4

            show yamato at center with dissolve       
            
            yamato "Let's be careful, Captain!"
            yamato "If we venture further, it's best not to separate. Who knows what we might encounter here..."

            window hide
            hide nami
            hide robin
            hide yamato
            with dissolve
            window auto

            $ tb_forest = 1

        if perona_crew and tb_forest < 4:

            show perona at center with dissolve
            perona "Captain, I'm sure with your skills you could navigate and cross here without any problems..."
            perona "But I think we could save time. This forest is very dense, and it's easy to get lost..."
            player "What do you suggest then..."
            perona "I've been here a while and got lost in this forest before..."
            perona "I remember there's a room in the mansion with a detailed map to cross it..."
            perona "Last time, I recall it was in the crew doctor's room..."
            perona "We could check that room for the map..."
            player "That could be interesting, I'll consider it..."

            window hide
            hide perona
            with dissolve
            window auto

            $ tb_forest = 4

    menu:
        "Continue":
            #$ tb_forest = tb_forest_next
            pass
        
        "Back":
            jump thriller_bark_mid
    

    $ ui_interface = False

    if tb_forest_map:

        robin "Alright... Let's look at the forest map before we proceed."
        window hide
        show events forest tb_forest_map with Dissolve(1.0)
        pause
        hide events forest tb_forest_map with Dissolve(1.0)
        window auto

    call screen forest_arrows() with Dissolve(1.0)
    # 1 : Left /// 2 : Top /// 3 : Right
    if _return == 2:
        call tb_forest_call pass (bg = 2) from _call_tb_forest_02_call
        call screen forest_arrows() with Dissolve(1.0)

        if _return == 1:
            call tb_forest_call pass (bg = 3) from _call_tb_forest_03_call
            call screen forest_arrows() with Dissolve(1.0)

            if _return == 3:
                call tb_forest_call pass (bg = 4) from _call_tb_forest_04_call
                call screen forest_arrows() with Dissolve(1.0)

                if _return == 3:
                    call tb_forest_call pass (bg = 5) from _call_tb_forest_05_call
                    call screen forest_arrows() with Dissolve(1.0)

                    if _return == 1:
                        $ tb_forest = 4
                        $ ui_interface = True
                        jump tb_camp

    $ ui_interface = True
    jump tb_forest_end

label tb_forest_end():
    window hide
    show screen screen_black with Dissolve(0.6)

    $ tb_forest_bg = 1
    $ game.location = "tb_forest"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto


    if tb_forest == 1:
        show nami at center with dissolve

        nami "It seems like we're going around in circles..."

        show nami:
            linear 0.4 xalign 0.85

        pause 0.4

        show robin with dissolve:
            yalign 1.0
            xalign 0.5  
    
        robin "That's right, we've been off course for a few minutes..."
        robin "I think we're back where we started..."
        robin "We could try again and investigate a bit more, or come back another time..."
        robin "What do you say, Captain?"

        window hide
        hide nami
        hide robin
        with dissolve
        window auto

        $ tb_forest = 2

    elif tb_forest == 2:

        show yamato at center with dissolve

        yamato "Damn it... We're lost again..."
        yamato "Damn forest..."

        show yamato:
            linear 0.4 xalign 0.85

        pause 0.4

        show robin with dissolve:
            yalign 1.0
            xalign 0.5        

        robin "It's very easy to get lost here..."
        robin "Maybe we should take advantage of being back at the beginning and head back..."
        robin "The smartest thing might be to check the castle for clues on how to cross this forest..."
        robin "We might get some directions..."

        window hide
        hide yamato
        hide robin
        with dissolve
        window auto

        $ tb_forest = 3

    jump tb_forest

screen forest_arrows():
    modal True
    zorder 15 #-15 # con 0 tapo todo

    tag menu

    imagebutton:# at rotate_img:
        idle "GUI forest forest_arrow"
        hover "GUI forest forest_arrow"
        #action [Function(f_next_girl)]
        action [Return(1)]
        xoffset 100
        yalign 0.5

    imagebutton at rotate_90:
        idle "GUI forest forest_arrow"
        hover "GUI forest forest_arrow"
        action [Return(2)]
        xalign 0.5
        yalign 0.0
        #yoffset 100


    imagebutton at flip:
        idle "GUI forest forest_arrow"
        hover "GUI forest forest_arrow"
        #action [Function(f_next_girl)]
        action [Return(3)]
        xalign 1.0
        xoffset -100
        yalign 0.5


label tb_forest_call(bg = 1):
    window hide
    show screen screen_black with Dissolve(0.6)

    $ tb_forest_bg = bg
    $ game.location = "tb_forest"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    return
