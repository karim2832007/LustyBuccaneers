# Version event: 1
# Version game: 0.1

image black_100 = Solid("#000000ff")
image black_90  = Solid("#000000E6")
image black_80  = Solid("#000000CC")
image black_70  = Solid("#000000B3")
image black_60  = Solid("#00000099")
image black_50  = Solid("#0000007F")
image black_40  = Solid("#00000066")
image black_30  = Solid("#0000004C")
image black_20  = Solid("#00000033")
image black_10  = Solid("#00000019")
image alpha     = Solid("#00000000")

screen screen_black():
    zorder 20
    add "black_100"

screen screen_basic_black():
    zorder 10
    add "black_100"

label screen_basic_black_hide():
    hide screen screen_basic_black
    return

screen screen_alpha_choice():
    zorder -20
    add "black_40"

screen screen_alpha_choice_lock():
    modal True
    zorder -20
    add "black_40"


define flash = Fade(0.2, 0.0, 0.5, color="#fff")
define flashaki = Fade(0.4, 0.2, 0.8, color="#ffffffe7")
define flashHancock = Fade(0.2, 0.0, 0.3, color="#ff3493ff")
define t_black = Fade(0.3, 0.2, 0.6, color="#000000")

define t_black_screen = Fade(0.6, 0.0, 0.3, color="#000000")
 
#"#f79fc4" #"#9e204a"

# COLOR STATS
define Charisma  = renpy.substitute("{color=#00e99f}{b}Charisma{/b}{/color}")
define Strength  = renpy.substitute("{color=#be71ec}{b}Strength{/b}{/color}")
define Intelligence  = renpy.substitute("{color=#46aeeb}{b}Intelligence{/b}{/color}")
define Cooking  = renpy.substitute("{color=#ff8e6f}{b}Cooking{/b}{/color}")

# COLOR LOCATION
define ThrillerBark.n  = renpy.substitute("{outlinecolor=#6e0e7a}{color=#ae6cc9}Thriller Bark{/color}{/outlinecolor}{space=2}")
define DrumIsland.n  = renpy.substitute("{outlinecolor=#28adce}{color=#97dbf7}Drum Island{/color}{/outlinecolor}{space=2}")
define AmazonLily.n  = renpy.substitute("{outlinecolor=#407a0a}{color=#bdf797}Amazon Lily{/color}{/outlinecolor}{space=2}")
define CactusIsland.n  = renpy.substitute("{outlinecolor=#7acc2c}{color=#8ff848}Cactus Island{/color}{/outlinecolor}{space=2}")

define Arabasta.n  = renpy.substitute("{outlinecolor=#f8c75c}{color=#9e8120}Arabasta{/color}{/outlinecolor}{space=2}")

#Dressrosa
define Dressrosa.n  = renpy.substitute("{outlinecolor=#f79fc4}{color=#9e204a}Dressrosa{/color}{/outlinecolor}{space=2}")

# ITEMS
define Berries.n  = renpy.substitute("{outlinecolor=#ffcc6c}{color=#ff951b}Berries{/color}{/outlinecolor}{space=2}")
define SakuraFlower.n = renpy.substitute("{outlinecolor=#be30a0}{color=#ff9de2}Sakura Flower{/color}{/outlinecolor}{space=2}")

# DEVIL FRUIT
define MeroMeroFruit.n = renpy.substitute("{outlinecolor=#fa3fcb}{color=#ff79a1}Mero Mero no Mi{/color}{/outlinecolor}{space=2}")
define HanaHanaFruit.n = renpy.substitute("{outlinecolor=#a85d74}{color=#ffc0cb}Hana Hana no Mi{/color}{/outlinecolor}{space=2}")
