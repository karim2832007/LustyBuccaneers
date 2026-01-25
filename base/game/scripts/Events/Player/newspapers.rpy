# Version event: 2
# Version game: 0.32

label newspapers:
    $ ui_berries = True

    menu:
        #(disabled=(game.clock.getDay < 10)):
        "NewsCoo Special Edition 1º{space=140}-100 Berries" if game.clock.getDay >= 10 and not obj_newcoo_1: 
            if berries >= 100:
                $ berries -= 100
                narrador "-100 [Berries.n] | + NewsCoo Special Edition 1º"
                $ ui_berries = False
                jump newcoo_1

            else:
                player "I have [berries] [Berries.n], but I need 100."

        "NewsCoo Special Edition 2º{space=140}-100 Berries" if game.clock.getDay >= 15 and not obj_newcoo_2: 
            if berries >= 100:
                $ berries -= 100
                narrador "-100 [Berries.n] | + NewsCoo Special Edition 2º"
                $ ui_berries = False
                jump newcoo_2

            else:
                player "I have [berries] [Berries.n], but I need 100."

        "Back":
            jump m_shells_town

    jump newspapers