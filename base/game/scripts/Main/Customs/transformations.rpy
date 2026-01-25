# Version event: 1
# Version game: 0.1

# MOVE
transform x_move(x_start=0.85, y_start=1.0, x_end=0.5, dur=0.3):
    xalign x_start
    yalign y_start

    linear dur xalign x_end
    pause 0.05


# SALTO
transform a_talk:
    easein 0.2 zoom 1.04
    pause 0.1
    easeout 0.1 zoom 1.0

# NEW VERSION
transform new_version():
    ease 0.8 alpha 0.2 zoom 1.0
    ease 1.0 alpha 1 zoom 1.10
    ease 0.4 alpha 1 
    repeat

# CHANGE NAME
transform a_change_name():
    alpha 0.0 xoffset 200
    easein 0.6 alpha 1.0 xoffset 0

# CHOICE ZOOM
transform choice_zoom():
    zoom 0.85
    on hover:
        linear 0.3 zoom 1.0
    on idle:
        linear 0.3 zoom 0.85

# CHOICE ZOOM
transform ship_battle_zoom():
    zoom 0.95
    on hover:
        linear 0.3 zoom 1.10
    on idle:
        linear 0.3 zoom 0.95

# ROTATE
transform rotate_img():
    rotate -180 

transform flip():
    zoom -1 

transform rotate_90():
    zoom -1
    rotate -90

transform ship_destroyed():
    xalign 0.5 yalign 0.5
    easeout 3.5 rotate_pad True rotate 30 yalign 0.3 xoffset 100

transform ship_on():
    xalign 0.5 yalign 0.5 rotate_pad True rotate 0 xoffset 0
    easeout 3 rotate_pad True rotate 4 yalign 0.46 xoffset 10
    easein 2 rotate_pad True rotate 2 yalign 0.48 xoffset 0
    easeout 3 rotate_pad True rotate -3 yalign 0.46 xoffset -10
    easein 2 rotate_pad True rotate 0 yalign 0.5 xoffset 0
    repeat

transform ship_seas_on():
    xalign 0.5 yalign 0.5 zoom 1.0
    easeout 1 yalign 0.5 yoffset -10 zoom 1.02
    easein 3 yalign 0.5 yoffset 0 zoom 1.0
    repeat

# fight
transform enemy_zoom():
    zoom 0.60
    
# ANIMACION SUBIDA CALCULA DISTANCIA - OPCIONES
transform choice_appear(i=0, length=0):
    yoffset (-((length/2)-1 - i)*(gui.choice_button_height+gui.choice_spacing) - (gui.choice_button_height+gui.choice_spacing)/2)


#init:
transform vibration:
    truecenter zoom 1.01
    linear 0.1 xoffset -1 yoffset 1 
    linear 0.2 xoffset 1 yoffset -1 
    linear 0.1 xoffset 1 yoffset 0
    linear 0.2 xoffset -1 yoffset 0
    linear 0.1 xoffset 0 yoffset 0
    repeat


transform zoom_down:
    zoom 1.0 xalign 0.5
    ease 0.3 zoom 1.15
    zoom 1.15

#earthquake
transform v_earthquake:
    truecenter zoom 1.02
    linear 0.1 yoffset 10
    linear 0.1 yoffset -10
    pause 0.05
    repeat

transform v_low_move:
    truecenter zoom 1.02
    linear 0.6 yoffset 15 xoffset 5
    linear 0.6 yoffset -15 xoffset -5
    repeat