# Version event: 2
# Version game: 0.5

# EN -1900 SE CARGAN LOS ARCHIVOS EN 00images.rpy ENTONCES ESTO VA DESPUES
init offset = -1800

# CARGAR IMAGENES
init python:
    config.images_directory = None

    def load_images_files():
        images={}
        for fn in renpy.list_files():
            if fn.lower().endswith((".png",".jpg",".webp")):
                parts=fn.split("/") if "/" in fn else [fn]

                #ELIMINO PARTE DE IMAGES CHARACTERS Y LOCATIONS 
                if parts and parts[0] in ["images"]:
                    parts.pop(0)

                    while parts and parts[0] in ["characters","enemies","locations", "skills"]:
                        parts.pop(0)

                    if parts and ("layers" in parts or "cuts" in parts or "objects" in parts):
                        parts[-1] = parts[-1].rsplit(".",1)[0]
                        images[parts[-1]]=fn

                    #AGREGA ESPACIOS EN BLANCO ENTRE CADA BARRA Y ELIMINA EXTENSION
                    elif parts:
                        parts[-1]=parts[-1].rsplit(".",1)[0]
                        name=" ".join(parts)
                        images[name]=fn

                if parts and parts[0] in ["movie"]:
                    parts.pop(0)
                    if parts and ("layers" in parts or "cuts" in parts):
                        parts[-1] = parts[-1].rsplit(".",1)[0]
                        images[parts[-1]]=fn

        #USA RENPY.IMAG PARA CREAR LAS IMAGENES CON VARIABLES
        for name,fn in images.items():
            renpy.image(name,fn)
            image = renpy.displayable(name)
            image.xpos = 0
            image.ypos = 0

    load_images_files()


# CARGAR AUDIOS
init python:
    config.audio_directory=None

    def load_audios_files():
        for fn in renpy.list_files():
            if fn.lower().endswith((".wav",".mp2",".mp3",".ogg",".opus")):
                parts=fn.split("/") if "/" in fn else [fn]
                # audio sound nombre.extencion 
                if parts and parts[0] in ["audio"]:
                    parts.pop(0)
                    # sound nombre.extencion 
                    if parts:
                        audio_folder = parts.pop(0)
                        #-1 ultima parte
                        audio_name = parts[-1].rsplit(".",1)[0]
                        audio_key = f"{audio_folder} {audio_name}"
                        audio.__dict__[audio_key]=fn            

    load_audios_files()