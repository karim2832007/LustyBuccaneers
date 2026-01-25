# Version event: 1
# Version game: 0.18

default donflamingo_name = "Donflamingo"

define donflamingo       = createCharacter('[donflamingo_name]', color="#ff93c5", image="donflamingo")

layeredimage donflamingo:
    zoom 1
    yoffset +1

    group cloths:
        attribute c1 default:
            "donflamingo c1 donflamingo_c1"