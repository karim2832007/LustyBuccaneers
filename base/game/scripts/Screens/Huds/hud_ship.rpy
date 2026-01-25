# Version event: 1
# Version game: 0.23

screen hud_ship():
    zorder 10

    frame:
        background None
        xsize 150
        ysize 150
        xalign 0.5
        yalign 0.5

        add "GUI HUD hud_ship_back"

        # Máscara de la vida
        add AlphaMask(
            child="GUI HUD hud_ship_hp",  
            mask= Transform("GUI HUD hub_ship_mask", xalign=0.5, yalign=0.5 , yoffset= 130 - (ship_player_health / ships_hp_max[ship_player_lvl]) * 130) 
        )

        add "GUI HUD hub_ship_top"
