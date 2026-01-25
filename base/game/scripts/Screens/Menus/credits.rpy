# Version event: 1
# Version game: 0.1

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

transform trn_tooltip:
    on show:
        xoffset 0
        easein 0.2 xoffset 100
    on hide:
        easeout 0.2 xoffset 0 alpha 0.0

screen tooltip_display(img, x, y):
    $ mouse_x, mouse_y = renpy.get_mouse_pos()
    #$ mouse_y = mouse_y/2
    add "black_50"
    add img xpos mouse_x ypos mouse_y yoffset -200 zoom 1.2 at trn_tooltip

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "{size=*1.5}Lusty Buccaneers - v[config.version!t]\n{/size}"

            vbox:
                style_prefix "overview"
                text "Lusty Buccaneers " + _("is an NSFW Visual Novel game in development! Embark on an exciting journey filled with challenges, enemies, mysteries, battles, and sexy women whom you can recruit into your crew! Experience an adventure set in a world inspired by") + " One Piece" + _(", but with many other surprises!\n")
                text ""
                text _("Not associated with Shonen Jump or Oda, this game is an unofficial fan creation.\n\n\n")
            

            text _("Created by") + " {a=https://www.patreon.com/LustyBuccaneers}Nika{/a}\n\n"

            #Huge thanks to my Patrons
            #"#ae6cc9"
            label "Patrons Wanted:"
            #text _("{color=#ae6cc9}Huge Thanks to my Patrons:{/color}")
            vbox:
                style_prefix "patreonsw"
                spacing 10
                textbutton  "윤호 이":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 001", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Valca":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 002", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Vali":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 003", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Cristobal":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 004", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "TheMediocreCrow":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 005", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Vinsmoke":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 006", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Butko":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 007", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Moioli":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 008", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Js Bohle":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 009", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

                textbutton  "Heitor R.":
                    action NullAction()
                    hovered Show("tooltip_display", img="GUI board wanted patrons 010", x=0.5, y=0.5)
                    unhovered Hide("tooltip_display")

            text "\n"

            label _("Huge Thanks to my Patrons:")
            #text _("{color=#ae6cc9}Huge Thanks to my Patrons:{/color}")
            vbox:
                style_prefix "patreons"
                text "Mike"
                text "Miles"
                text "Daniele"
                text "Krookaking"
                text "Hayden"
                text "sdas"
                text "James"
                text "Sbsbs"
                text "Schlu"
                text "Patrick"
                text "John"
                text "IMJAYGK"
                text "수민 김"
                text "Caleb"
                text "CocOli"
                text "Dima"
                text "Hanzo84"
                text "Giovany"
                text "Christopher"
                text "Dima"
                text "skeith9"
                text "Neon"
                text "Dany"
                text "Authentic"
                text "Adon"
                text "Dark Demon gamer"
                text "Epsilon Shiro"
                text "Bassin"
                text "Mugiwara D. Ryu"
                text "mx burn"
                text "Derpydino"
                text "Sweet Hell"
                text "Azding Ytb"
                text "Eliot Esquire"
                text "Yves-Melvin Richter" 
                text "Dai shi"#大 死
                text "xing A" 
                text "brandon houk"
                text "growbumon"
                text "mansa"
                text "Janjarre"
                text "Richard"
                text "Sam Serius"
                text "Giovanni"
                text "Navdeep Singh"
                text "Maximo Contreras"
                text "yiqiang li"
                text "Ng Elson"
                text "Seth Francis"
                text "justin Santos"
                text "Tye Abrahams"
                text "Heitor Rodrigues"
                text "Alexander Alexandrov" #Александр Александров
                text "Jesus Campos"
                text "kimmo256"
                text "Josepx3"
                text "fedi jouirou"
                text "Adonis Berrios"
                text "Justin G. Santos"
                text "Janjarre Vanpoppel"
                text "Times of Abraham"
                text "By Elson"
                text "Holy Day Liu"



            text "\n\n"
                
            label "And a huge thanks to all my other Patrons and Followers on Patreon!"
            label "This game is possible thanks to all of you!"
            
            text "\n\n"

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{color=#575654}Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]{/color}")


            

            

style about_label is gui_label
style about_label_text is gui_label_text
style about_text:
    font gui.text_font
    color "#ffd95d"
    #properties gui.text_properties("interface")


style patreons_text:
    size 26
    font gui.text_font_korean
    color "#ffd95d"

style patreonsw_button_text:
    size 30
    font gui.text_font_korean
    color "#ffd95d"
    
style overview_text:
    size 24
    font gui.text_font
    color "#ffaf46"

#font gui.interface_text_font
#font gui.wanted_text_font
#font gui.text_font


screen tooltip_image(xoffset=0, yoffset=0):
    add "GUI board wanted patrons 001" xpos xoffset ypos yoffset