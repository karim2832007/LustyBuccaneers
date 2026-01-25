# Version event: 3
# Version game: 0.18

# NARRATOR
define narrador = createCharacter('', what_xalign=0.5, what_text_align=0.5, color="#FFFFFF", image="img_none")

define unknown  = createCharacter('???', color="#acaaab", image="img_none")

define guard = createCharacter('Guard', color="#577cf3", image="guard")


# GET CHARACTER
init python:
    def gCharacter(name):
        if name == alvida_name:
            return alvida

        return name
