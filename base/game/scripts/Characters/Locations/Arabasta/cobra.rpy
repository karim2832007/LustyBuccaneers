# Version event: 2
# Version game: 0.5

default cobra_name = "Cobra"

define cobra      = createCharacter('[cobra_name]', color="#530841", image="cobra")

default cobra_love = 0
default cobra_lust = 0

default cobra_crew = True

layeredimage cobra:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "cobra c1 cobra_c1"

        attribute c1_mr2:
            "cobra c1 cobra_c1_mr2"

        attribute c1_wounded:
            "cobra c1 cobra_c1_wounded"