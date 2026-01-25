# Version event: 1
# Version game: 0.33

default sai_name = "Sai"

define sai       = createCharacter('[sai_name]', color="#ffc079", image="sai")

layeredimage sai:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "sai c1 sai_c1"