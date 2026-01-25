# Version event: 1
# Version game: 0.35

default riku_name = "Gladiator" # Ricky # Riku

define riku      = createCharacter('[riku_name]', color="#1c1b68", image="riku")

layeredimage riku:
    zoom 1
    yoffset +1

    group cloths:
        attribute c2 default:
            "riku riku_c2"

        attribute c2_wounded:
            "riku riku_c2_wounded"