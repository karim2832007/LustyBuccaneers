# Version event: 1
# Version game: 0.23

screen hud_player():
    zorder 10

    frame:
        background None
        xsize 150
        ysize 150
        xalign 0.5
        yalign 0.5

        add "GUI HUD hud_player_back"

        # Máscara de la vida
        add AlphaMask(
            child="GUI hud_player_hp",  
            mask= Transform("GUI HUD hud_player_hp", rotate=(-180 * (1 - player_hp / RPGPlayer.true_hp_max())), xalign=0.5, yalign=0.5 ) 
        )

        add AlphaMask(
            child="GUI HUD hud_player_mana",  
            mask= Transform("GUI HUD hud_player_mana", rotate=(180 * (1 - player_mana / RPGPlayer.true_mana_max())), xalign=0.5, yalign=0.5 )
        )

        add "GUI HUD hub_player_top"


image GUI hud_player_hp = ConditionSwitch(
    "player_hp <= RPGPlayer.true_hp_max()*0.25", "GUI HUD hud_player_hp_red",
    "player_hp <= RPGPlayer.true_hp_max()*0.5", "GUI HUD hub_player_hp_yellow",
    True,"GUI HUD hud_player_hp",
)