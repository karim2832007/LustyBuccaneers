# Version event: 2
# Version game: 0.4

init -1 python:
    def calculate_text_size(text, max_width, font, base_size):
        from renpy.text.text import Text
        # Creamos un objeto de texto para medir su tamaño
        text_obj = Text(text, style="default", size=base_size, font=font)
        rendered_width, _ = text_obj.size()
        
        # Si el ancho excede el máximo permitido, reducimos el tamaño
        while rendered_width > max_width and base_size > 40:  # Establecemos un tamaño mínimo
            base_size -= 2
            text_obj = Text(text, style="default", size=base_size, font=font)
            rendered_width, _ = text_obj.size()

        return base_size


define n_girl = 0
define girl_img = ["nami c1 nami_c1", "robin c1 robin_c1", "yamato c1 yamato_c1", "perona c1 perona_c1", "hancock c1 hancock_c1", "vivi c1 vivi_c1", "uta c1 uta_c1"]
define girl_n = ["nami", "robin", "yamato", "perona", "hancock", "vivi","uta"]

init python:
    def f_previous_girl():
        while True:
            globals()['n_girl'] = (globals()['n_girl'] - 1) % len(girl_n)
            if globals().get(girl_n[globals()['n_girl']] + "_crew"):
                break

    def f_next_girl():
        while True:
            globals()['n_girl'] = (globals()['n_girl'] + 1) % len(girl_n)
            if globals().get(girl_n[globals()['n_girl']] + "_crew"):
                break

screen girls_stats():
    modal True
    zorder 15 #-15 # con 0 tapo todo

    tag menu

    add "BG locations"

    imagebutton:
        idle "black_40"
        hover "black_40"
        action [Hide("girls_stats")]

    button:
        focus_mask None
        action NullAction()
        area (625, 40, 670, 1000)


    add "GUI girls_stats stats_wanted_back":
        xalign 0.5
        yalign 0.5  
    
    add [girl_img[globals()['n_girl']]]:
        zoom 0.6
        xalign 0.5
        yalign 0.45

    add "GUI girls_stats stats_wanted":
        xalign 0.5
        yalign 0.5

    imagebutton:
        idle "GUI girls_stats stats_arrow"
        hover "GUI girls_stats stats_arrow_press"
        action [Function(f_previous_girl)]
        xpos 485
        yalign 0.5

    imagebutton at rotate_img:
        idle "GUI girls_stats stats_arrow"
        hover "GUI girls_stats stats_arrow_press"
        action [Function(f_next_girl)]
        xpos 1195
        yalign 0.5

    text "WANTED":
        font gui.wanted_text_font
        color "#6b5440"
        xalign 0.5
        #yalign 0.30
        yoffset 108
        size 130

    text "DEAD OR ALIVE":
        font gui.wanted_text_font
        color "#6b5440"
        xalign 0.5
        #yalign 0.30
        yalign 0.67
        size 62

    #$ name_length = len(globals().get(girl_n[globals()['n_girl']] + "_name"))
    $ girl_name = globals().get(girl_n[globals()['n_girl']] + "_name")
    $ base_size = 86
    $ max_width = 520 
    $ text_size = calculate_text_size(girl_name, max_width, gui.wanted_text_font, base_size)

    text girl_name:#[globals().get(girl_n[globals()['n_girl']] + "_name")]:
        font gui.wanted_text_font
        color "#6b5440"
        xalign 0.5
        #yalign 0.30
        yalign 0.76
        size text_size

    text "MARINE":
        font gui.wanted_text_font
        color "#6b5440"
        xalign 0.6
        #yalign 0.30
        yalign 0.93
        size 65

    
    vbox:
        xalign 0.42
        yalign 0.90
        spacing 20

        hbox:
            frame:
                xsize 150
                ysize 50
                background None

                text "LOVE:":
                    font gui.wanted_text_font
                    color "#6b5440"
                    text_align 0
                    yalign 0.5
                    size 48

            frame:
                xsize 65
                ysize 50
                background None

                text [str(globals().get(girl_n[globals()['n_girl']] + "_love"))]:
                    font gui.interface_text_font
                    color "#6b5440"
                    xalign 0.5
                    text_align 0.5
                    yalign 0.5
                    size 55

        hbox:
            frame:
                xsize 150
                ysize 50
                background None

                text "LUST:":
                    font gui.wanted_text_font
                    color "#6b5440"
                    text_align 0
                    yalign 0.5
                    size 48

            frame:
                xsize 65
                ysize 50
                background None

                text [str(globals().get(girl_n[globals()['n_girl']] + "_lust"))]:
                    font gui.interface_text_font
                    color "#6b5440"
                    xalign 0.5
                    text_align 0.5
                    yalign 0.5
                    size 55