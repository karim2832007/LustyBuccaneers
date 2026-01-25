# Version event: 1
# Version game: 0.41

label rebecca_join_the_crew:
    $ ui_interface = False
    rebecca ""

    menu:
        "Yes":
            player ""

            window hide
            hide rebecca with dissolve
            window auto
            
            $ rebecca_crew = True
            $ ThrillerBark.h = 11

            pause 0.5
            $ game.clock.next()
            #aca pondría ir directo al barco como opción tmb

        "I need to think about it":
            player "I need to think about it"
            rebecca "That's okay. If you change your mind, I'll be here!"

    $ _window_hide()
    hide rebecca with moveoutright
    pause 0.5
    
    $ game.clock.next()
    $ ui_interface = True
    jump expression game.location
