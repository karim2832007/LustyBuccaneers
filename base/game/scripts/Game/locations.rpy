# Version event: 2
# Version game: 0.25

init -1 python:
    def ImgNight(ruta_base):
        image_name = f"{ruta_base} IN"

        renpy.image(
            image_name,
            ConditionSwitch(
                "game.clock.night", f"{ruta_base}_night",
                "True", f"{ruta_base}"
            )
        )
        
        return image_name


image BG locations = ConditionSwitch(
    # SHIP
    "game.location == 'ship_captains_cabin'", "BG ship ship_captains_cabin",
    "game.location == 'ship_mid'", "BG ship mid",
    "game.location == 'ship_workshop'", "BG ship ship_workshop",
    "game.location == 'ship_girls_room_door'", "BG ship ship_girls_room_door",
    "game.location == 'ship_girls_room'", "BG ship ship_girls_room",
    "game.location == 'ship_kitchen'", "BG ship ship_kitchen",
    "game.location == 'ship_door'", "BG ship ship_door",
    "game.location == 'ship_training_room'", "BG ship training room",
    "game.location == 'ship_library_room'", "BG ship library room", #ship_library_room
    "game.location == 'ship_fishing'", "minigames fishing ship_fishing",
    "game.location == 'ship_bathroom'", "BG ship ship_bathroom",
    "game.location == 'ship_bathroom_tub'", "BG ship ship_bathroom_tub",

    # SEA
    "game.location == 'ship_battle'", "minigames ship_battle background_battle_ship",
    "game.location == 'ship_battle_fight'", "minigames fight background_ship_fight",
    # EAST BLUE
    "game.location == 'shells_town'", "BG eastblue shellstown",
    "game.location == 'shells_town_bar'", "BG eastblue shells_town_bar",
    "game.location == 'shells_town_outside'", ImgNight("BG eastblue shells_town_outside"),

    # THRILLER BARK
    "game.location == 'thriller_bark'", "BG thrillerbark thriller_bark",
    "game.location == 'thriller_bark_entrance'", "BG thrillerbark thriller_bark_entrance",
    "game.location == 'thriller_bark_mid'", "BG thrillerbark thriller_bark_mid",
    "game.location == 'thriller_bark_cemetery'", "BG thrillerbark thriller_bark_cemetery",
    "game.location == 'thriller_bark_grate'", "BG thrillerbark thriller_bark_grate",
    "game.location == 'thriller_bark_mansion'", "BG thrillerbark mansion",
    "game.location == 'tb_mansion_01'", "BG thrillerbark mansion_01",
    "game.location == 'tb_mansion_02'", "BG thrillerbark mansion_02",
    "game.location == 'tb_mansion_03'", "BG thrillerbark mansion_03",
    "game.location == 'tb_forest'", "BG thrillerbark tb_forest",
    "game.location == 'perona_room'", "BG thrillerbark perona_room",
    "game.location == 'thriller_bark_dr_room'", "BG thrillerbark thriller_bark_dr_room",
    "game.location == 'thriller_bark_camp'", "BG thrillerbark thriller_bark_camp",

    # Drum Island
    "game.location == 'drum_island'", "BG drum_island",
    "game.location == 'drum_island_village'", "BG drum_island_village",
    "game.location == 'drum_island_forest'", "BG drum_island_forest",
    "game.location == 'drum_island_castle'", "BG drum_island_castle",
    "game.location == 'di_castle_mid'", "BG di_castle_mid",
    "game.location == 'di_castle_room'", "BG di_castle_room",
    "game.location == 'drum_island_sakura'", "BG drum_island_sakura",

    # AMAZON LILY
    "game.location == 'amazon_lily'", "BG amazonlily amazon_lily",
    "game.location == 'amazon_lily_city'", "BG amazonlily amazon_lily_city",
    "game.location == 'amazon_lily_palace'", "BG amazonlily amazon_lily_palace",
    "game.location == 'amazon_lily_prision'", "BG amazonlily amazon_lily_prision",
    "game.location == 'al_palace_room'", "BG amazonlily al_palace_room",
    "game.location == 'amazon_lily_ring'", "BG amazonlily amazon_lily_ring",
    "game.location == 'amazon_lily_ring_top'", "BG amazonlily amazon_lily_ring_top",

    # Cactus Island
    "game.location == 'cactus_island'", "BG cactus_island",
    "game.location == 'ci_whisky_peak'", "BG ci_whisky_peak",
    "game.location == 'ci_alley'", "BG cactusisland ci_alley",
    "game.location == 'ci_den'", "BG cactusisland ci_den",
    "game.location == 'ci_captured'", "BG cactusisland ci_captured",
    "game.location == 'ci_river'", "BG cactusisland ci_river",

    # Arabasta
    "game.location == 'arabasta'", "BG arabasta",

    # Arabasta - Nanohana
    "game.location == 'ar_nanohana'", "BG ar_nanohana",
    "game.location == 'ar_nanohana_coast'", "BG ar_nanohana_coast",
    "game.location == 'ar_nanohana_coast_fishing'", "minigames fishing ar_nanohana_fishing",
    "game.location == 'ar_nanohana_h'", "BG arabasta ar_nanohana_h",

    # Arabasta - Erumalu
    "game.location == 'ar_erumalu'", "BG arabasta ar_erumalu",
    "game.location == 'ar_erumalu_coast'", "BG arabasta ar_erumalu_coast",

    # Arabasta - Yuba
    "game.location == 'ar_yuba_entrance'", "BG ar_yuba_entrance",
    "game.location == 'ar_yuba_oasis'", "BG ar_yuba_oasis",
    "game.location == 'ar_desert'", "BG arabasta ar_desert",

    "game.location == 'ar_y_toto_house'", "BG arabasta yuba ar_y_toto_house",
    "game.location == 'ar_y_bar'", "BG ar_yuba_bar",
    "game.location == 'ar_y_dance'", "BG arabasta yuba ar_y_dance",

    # Arabasta - Rainbase
    "game.location == 'ar_rainbase'", "BG ar_rainbase",
    "game.location == 'ar_rainbase_casino'", "BG arabasta rainbase ar_rainbase_casino",
    "game.location == 'ar_rainbase_casino_exit'", "BG arabasta rainbase ar_rainbase_casino_exit",
    "game.location == 'ar_rainbase_casino_in'", "BG arabasta rainbase ar_rainbase_casino_in",
    "game.location == 'ar_rainbase_jail'", "BG arabasta rainbase ar_rainbase_jail",
    "game.location == 'ar_rainbase_jail_pell'", "BG arabasta rainbase ar_rainbase_jail_pell",
    "game.location == 'ar_rainbase_room'", "BG arabasta rainbase ar_rainbase_room",
    "game.location == 'ar_rainbase_stairs'", "BG arabasta rainbase ar_rainbase_stairs",
    "game.location == 'ar_rainbase_vip'", "BG arabasta rainbase ar_rainbase_vip",
    "game.location == 'ar_rainbase_vip_in'", "BG arabasta rainbase ar_rainbase_vip_in",

    # Arabasta - Katorea
    "game.location == 'ar_katorea'", "BG arabasta ar_katorea",

    # Arabasta - Alubarna
    "game.location == 'ar_alubarna'", "BG arabasta alubarna ar_alubarna",
    "game.location == 'ar_alubarna_war'", "BG arabasta alubarna ar_alubarna_war",
    "game.location == 'ar_alubarna_palace'", "BG arabasta alubarna ar_alubarna_palace",
    "game.location == 'ar_alubarna_palace_room'", "BG arabasta alubarna ar_alubarna_palace_room",
    "game.location == 'ar_alubarna_shortcut'", "BG arabasta alubarna ar_alubarna_shortcut",

    # Elegia
    "game.location == 'elegia'", ImgNight("BG elegia elegia"),
    "game.location == 'elegia_dock'", ImgNight("BG elegia elegia_dock"),
    "game.location == 'elegia_city'", ImgNight("BG elegia elegia_city"),
    "game.location == 'elegia_road'", ImgNight("BG elegia elegia_road"),
    "game.location == 'elegia_road_fight'", "BG elegia elegia_road_fight",
    "game.location == 'elegia_castle'", "BG elegia elegia_castle",
    "game.location == 'el_castle_corridor'", "BG elegia el_castle_corridor",
    "game.location == 'el_castle_auditorium'", "BG elegia el_castle_auditorium",
    "game.location == 'el_castle_room'", "BG elegia el_castle_room",
    "game.location == 'elegia_forest'", "BG elegia elegia_forest",
    "game.location == 'elegia_church'", "BG elegia elegia_church",
    "game.location == 'elegia_church_inside'", "BG elegia elegia_church_inside",

    # e_church_tunnels
    "game.location == 'el_church_tunnels'", "BG elegia el_church_tunnels",
    "game.location == 'el_church_tunnels2'", "BG elegia el_church_tunnels2",
    "game.location == 'el_church_tunnels3'", "BG elegia el_church_tunnels3",
    "game.location == 'el_c_tunnels_room'", "BG elegia el_c_tunnels_room",

    # dressrosa
    "game.location == 'dressrosa'", ImgNight("BG dressrosa dressrosa"),

    # ACACIA
    "game.location == 'dr_acacia_1'", ImgNight("BG dressrosa acacia dr_acacia_1"),
    "game.location == 'dr_ac_colosseum'", ImgNight("BG dressrosa acacia dr_ac_colosseum"),
    "game.location == 'dr_ac_co_reception'", "BG dressrosa acacia dr_ac_co_reception",
    "game.location == 'dr_ac_co_fighters_preparations'", "BG dressrosa acacia dr_ac_co_fighters_preparations",
    "game.location == 'dr_ac_co_statue'", "BG dressrosa acacia dr_ac_co_statue",
    "game.location == 'dr_ac_co_store_room'", ImgNight("BG dressrosa acacia dr_ac_co_store_room"),
    "game.location == 'dr_ac_co_corridor_fight'", "BG dressrosa acacia dr_ac_co_corridor_fight",

    #dr_ac_co_arena
    "game.location == 'dr_ac_co_arena'", "BG dressrosa acacia dr_ac_co_arena",



    # MORE
    "game.location == 'none'", "none",
    "game.location == 'main_menu'", "black_100",
    "True", "black_100",#Fixed(Solid("#f0f"), Text("locations", align=(0.5, 0.5))),
)


image BG ship mid = ConditionSwitch(
    "game.clock.night", "BG ship ship_mid_night",
    True,"BG ship ship_mid",
)

image BG eastblue shellstown= ConditionSwitch(
    "game.clock.night", "BG eastblue shells_town_night",
    True,"BG eastblue shells_town",
)

image BG ship training room = ConditionSwitch(
    "game.clock.night", "BG ship ship_training_room_night",
    True,"BG ship ship_training_room",
)

image BG ship library room = ConditionSwitch(
    "game.clock.night", "BG ship ship_library_room_night",
    True,"BG ship ship_library_room",
)

image BG thrillerbark mansion = ConditionSwitch(
    "game.clock.night", "BG thrillerbark thriller_bark_mansion_night",
    True,"BG thrillerbark thriller_bark_mansion",
)

image BG thrillerbark perona_room = ConditionSwitch(
    "perona_crew", "BG thrillerbark perona_room_off",
    True,"BG thrillerbark perona_room_on",
)

image BG thrillerbark tb_forest = ConditionSwitch(
    "tb_forest_bg == 2", "BG thrillerbark tb_forest_2",
    "tb_forest_bg == 3", "BG thrillerbark tb_forest_3",
    "tb_forest_bg == 4", "BG thrillerbark tb_forest_4",
    "tb_forest_bg == 5", "BG thrillerbark tb_forest_5",
    True,"BG thrillerbark tb_forest_1",
)

# Drum Island
image BG drum_island = ConditionSwitch(
    "game.clock.night", "BG drumisland drum_island_night",
    True,"BG drumisland drum_island",
)

image BG drum_island_village = ConditionSwitch(
    "game.clock.night", "BG drumisland drum_island_village_night",
    True,"BG drumisland drum_island_village",
)

image BG drum_island_forest = ConditionSwitch(
    "game.clock.night", "BG drumisland drum_island_forest_night",
    True,"BG drumisland drum_island_forest",
)

image BG drum_island_castle = ConditionSwitch(
    "game.clock.night", "BG drumisland drum_island_castle_night",
    True,"BG drumisland drum_island_castle",
)

image BG di_castle_mid = ConditionSwitch(
    "game.clock.night", "BG drumisland di_castle_mid_night",
    True,"BG drumisland di_castle_mid",
)

image BG di_castle_room = ConditionSwitch(
    "game.clock.night", "BG drumisland di_castle_room_night",
    True,"BG drumisland di_castle_room",
)

image BG drum_island_sakura = ConditionSwitch(
    "game.clock.night", "BG drumisland drum_island_sakura_night",
    True,"BG drumisland drum_island_sakura",
)

# Cactus Island
image BG cactus_island = ConditionSwitch(
    "game.clock.night", "BG cactusisland cactus_island_night",
    True,"BG cactusisland cactus_island",
)

image BG ci_whisky_peak = ConditionSwitch(
    "game.clock.night", "BG cactusisland ci_whisky_peak_night",
    True,"BG cactusisland ci_whisky_peak",
)

# Arabasta
image BG arabasta = ConditionSwitch(
    "game.clock.night", "BG arabasta arabasta_night",
    True,"BG arabasta arabasta",
)

image BG ar_nanohana = ConditionSwitch(
    "game.clock.night", "BG arabasta ar_nanohana_night",
    True,"BG arabasta ar_nanohana",
)

image BG ar_nanohana_coast = ConditionSwitch(
    "game.clock.night", "BG arabasta ar_nanohana_coast_night",
    True,"BG arabasta ar_nanohana_coast",
)

image BG ar_nanohana_coast = ConditionSwitch(
    "game.clock.night", "BG arabasta ar_nanohana_coast_night",
    True,"BG arabasta ar_nanohana_coast",
)

image BG ar_yuba_entrance = ConditionSwitch(
    "game.clock.night", "BG arabasta ar_yuba_entrance_night",
    True,"BG arabasta ar_yuba_entrance",
)

image BG ar_yuba_oasis = ConditionSwitch(
    "game.clock.night and oasis_yuba", "BG arabasta ar_yuba_oasis_on_night",
    "oasis_yuba", "BG arabasta ar_yuba_oasis_on",
    "game.clock.night", "BG arabasta ar_yuba_oasis_off_night",
    True,"BG arabasta ar_yuba_oasis_off",
)

image BG ar_yuba_bar = ConditionSwitch(
    "yuba_bar > 0", "BG arabasta yuba ar_y_bar",
    True,"BG arabasta yuba ar_y_bar_off",
)

image BG ar_rainbase = ConditionSwitch(
    "game.clock.night", "BG arabasta rainbase ar_rainbase_night",
    True,"BG arabasta rainbase ar_rainbase",
)

# elegia
image BG elegia elegia_forest = ConditionSwitch(
    "elegia_forest_bg == 2", "BG elegia elegia_forest_2",
    "elegia_forest_bg == 3", "BG elegia elegia_forest_3",
    "elegia_forest_bg == 4", "BG elegia elegia_forest_4",
    True,"BG elegia elegia_forest_1",
)
