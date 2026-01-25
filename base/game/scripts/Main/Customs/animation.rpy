# Version event: 1
# Version game: 0.1

# EN -1900 SE CARGAN LOS ARCHIVOS EN 00images.rpy ENTONCES ESTO VA DESPUES
init offset = -100

# CARGAR IMAGENES
init python:
    def config_frame(i_speed, i_frame, max_frame, i_step = 1):
        global speed
        global animation_frame
        global animation_frame_max
        global animation_frame_min
        global step

        speed = i_speed
        animation_frame = i_frame
        animation_frame_max = max_frame
        animation_frame_min = i_frame
        step = i_step

    def next_frame(t, st, at):
        global animation_frame
        global animation_frame_max
        global animation_frame_min
        global step

        if animation_frame == animation_frame_max:
            step = -1
        elif animation_frame == animation_frame_min:
            step = 1
            
        animation_frame += step