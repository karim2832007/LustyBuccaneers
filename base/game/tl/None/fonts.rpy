init -900 python:
    game_fonts[None] = "fonts/Raleway-Bold.ttf"

translate None python:
    gui.text_font = game_fonts[None]
    gui.name_text_font = game_fonts[None]
    gui.interface_text_font = "fonts/AveriaSerifLibre-Bold.ttf"
    gui.wanted_text_font = "fonts/Neothic.ttf"
    gui.text_font_korean = "fonts/NanumSquareNeo-dEb.ttf"
    renpy.restart_interaction()
