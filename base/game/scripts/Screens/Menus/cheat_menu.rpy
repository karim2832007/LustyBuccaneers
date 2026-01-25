###############################################
# MINIGAME CHEAT DEFAULTS
###############################################



init python:
    if "detail_inputs" not in globals():
        detail_inputs = {
            "nami_love": "",
            "nami_lust": "",
            "robin_love": "",
            "robin_lust": "",
            "zala_love": "",
            "zala_lust": "",
            "kalifa_love": "",
            "kalifa_lust": "",
            "kalifa_subm": "",
            "vivi_love": "",
            "vivi_lust": "",
            "vivi_subm": "",
            "uta_love": "",
            "uta_lust": "",
            "uta_subm": "",
            "rebecca_love": "",
            "rebecca_lust": "",
            "rebecca_subm": "",
            "perona_love": "",
            "perona_lust": "",
            "perona_subm": "",
            "hancock_love": "",
            "hancock_lust": "",
            "hancock_subm": "",
            "alvida_love": "",
            "alvida_lust": "",
            "yamato_love": "",
            "yamato_lust": "",

            # ⭐ RESOURCE KEYS (added)
            "berries": "",
            "gold": "",
            "iron": "",
            "wood": "",
            "food": "",
            "paper": "",
            "fabric": ""
        }

# MEMORY GAME
default cheat_mg_memory_freeze = False
default cheat_mg_memory_reveal = False
default cheat_mg_memory_autowin = False

# FISHING GAME
default cheat_mg_fishing_freeze_fish = False
default cheat_mg_fishing_super_gain = False
default cheat_mg_fishing_no_loss = False
default cheat_mg_fishing_autowin = False

# SHIP BATTLE
default cheat_mg_ship_inf_hp = False
default cheat_mg_ship_always_hit = False
default cheat_mg_ship_enemy_miss = False
default cheat_mg_ship_inf_cannon = False
default cheat_mg_ship_boarding = False
default cheat_mg_ship_escape = False
default cheat_mg_ship_max_loot = False

# CARDS GAME
default cheat_mg_cards_always_win = False
default cheat_mg_cards_easy = False
default cheat_mg_cards_no_loss = False
default cheat_mg_cards_autowin = False


###############################################
# GLOBAL SETTINGS
###############################################
init -2 python:
    config.console = True

init python:
    # Bold for all text by default
    style.default.bold = True


###############################################
# ULTRA DIVINE AURA COLORS (ABSOLUTE DIVINITY)
###############################################
init python:
    # You can tweak these if you want later
    DIVINE_WHITE  = "#ffffff"
    DIVINE_GOLD   = "#ffd700"
    DIVINE_BLUE   = "#66ccff"
    DIVINE_PURPLE = "#c871ff"
    DIVINE_RED    = "#ff3366"
    DIVINE_PINK   = "#ff99cc"
    DIVINE_GREEN  = "#7CFC00"

    DIVINE_RAINBOW_OUTLINES = [
        (2, DIVINE_WHITE,  0, 0),
        (3, DIVINE_GOLD,   0, 0),
        (4, DIVINE_BLUE,   0, 0),
        (5, DIVINE_PURPLE, 0, 0),
        (6, DIVINE_RED,    0, 0),
    ]


###############################################
# ANIMATIONS / TRANSFORMS (ABSOLUTE DIVINITY)
###############################################
transform cheat_screen_in:
    alpha 0.0
    xoffset 80
    easeout_back 0.35 alpha 1.0 xoffset 0

# subtle breathing aura on the whole screen
transform divine_screen_aura:
    on show:
        parallel:
            alpha 0.95
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.95
            repeat
        parallel:
            zoom 1.0
            linear 1.0 zoom 1.02
            linear 1.0 zoom 1.0
            repeat

# button idle fade-in
transform cheat_button_idle_t:
    alpha 0.0
    yoffset 10
    linear 0.25 alpha 1.0 yoffset 0

# button hover divine aura
transform cheat_button_hover_t:
    on hover:
        parallel:
            easeout 0.12 zoom 1.10 yoffset -2
    on idle:
        easein 0.12 zoom 1.0 yoffset 0

# button click explosion
transform cheat_button_click_t:
    on activate:
        parallel:
            ease 0.06 zoom 0.92
            ease 0.06 zoom 1.12
            ease 0.06 zoom 1.0
        parallel:
            alpha 1.0
            linear 0.18 alpha 0.7
            linear 0.10 alpha 1.0

# error shake for popup
transform cheat_error_shake:
    alpha 1.0
    linear 0.03 xoffset -6
    linear 0.03 xoffset 6
    linear 0.03 xoffset -4
    linear 0.03 xoffset 4
    linear 0.03 xoffset 0

# divine halo behind some frames (like stat detail)
transform divine_frame_halo:
    alpha 0.9
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.9
    repeat


###############################################
# BUTTON / TEXT STYLES (ABSOLUTE DIVINITY)
###############################################
# Title / standalone text style (outlines supported)
style cheat_title_text:
    outlines DIVINE_RAINBOW_OUTLINES
    color DIVINE_GOLD
    bold True
    italic True
    xalign 0.5

# Base divine button (auto width)
style cheat_button:
    background "#222222"
    hover_background "#6666ff"
    padding (8, 6)
    size 20
    color "#ffffff"
    bold True
    italic True
    text_align 0.5

# Fixed-width divine button (characters + stats)
style cheat_button_fixed is cheat_button:
    xsize 260
    text_align 0.5


###############################################
# SAFE INTEGER PARSER
###############################################
init python:
    def safe_int(s):
        try:
            return int(str(s).strip())
        except Exception:
            return None


###############################################
# ERROR POPUP (DIVINE SHAKE + GLOW)
###############################################
default cheat_error = ""

screen cheat_error_popup():
    zorder 300
    if cheat_error:
        frame at cheat_error_shake:
            style_prefix "say"
            xalign 0.5
            yalign 0.1
            background "#000000cc"
            padding (20, 10)
            text "[cheat_error]" color "#ff4444" size 28 outlines DIVINE_RAINBOW_OUTLINES
            timer 2.5 action SetVariable("cheat_error", "")


###############################################
# CHEATS OVERLAY BUTTON (LOCKED BY ACTIVATION)
###############################################
screen cheats_overlay():
    zorder 200

    if persistent.current_activation == "YouTubeSubscriber":
        frame:
            background None
            padding (20, 20)
            xpos 1.0
            ypos 1.0
            xanchor 1.0
            yanchor 1.0

            textbutton "CHEATS" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_GOLD
                action Show("cheat_menu")


###############################################
# MAIN CHEAT MENU (DIVINE AURA)
###############################################
screen cheat_menu():
    tag cheat
    modal True
    zorder 201

    frame at cheat_screen_in, divine_screen_aura:
        xalign 1.0
        yalign 0.0
        xsize 320
        yfill True
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 16

            text "Cheat Menu" size 32 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5

            textbutton "Characters" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_BLUE
                action [Hide("cheat_menu"), Show("characters")]

            textbutton "Resources" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_GOLD
                action [Hide("cheat_menu"), Show("resource_stats")]

            # ⭐ NEW BUTTON — MINIGAMES CHEAT MENU
            textbutton "Minigames" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_PURPLE
                action [Hide("cheat_menu"), Show("cheat_minigames")]

            null height 16

            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5

###############################################
# CHARACTERS SCREEN (DIVINE AURA)
###############################################
screen characters():
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    frame at cheat_screen_in, divine_screen_aura:
        xalign 1.0
        yalign 0.0
        xsize 320
        yfill True
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 12

            text "Characters" size 32 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5

            # FIXED-WIDTH DIVINE BUTTONS FOR CHARACTERS
            textbutton "Alvida" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color DIVINE_WHITE
                action [Hide("characters"), Show("character_stats", character="alvida")]

            textbutton "Yamato" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color DIVINE_RED
                action [Hide("characters"), Show("character_stats", character="yamato")]

            textbutton "Hancock" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color DIVINE_PURPLE
                action [Hide("characters"), Show("character_stats", character="hancock")]

            textbutton "Nami" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color "#ff9100"
                action [Hide("characters"), Show("character_stats", character="nami")]

            textbutton "Perona" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color "#ff51a2"
                action [Hide("characters"), Show("character_stats", character="perona")]

            textbutton "Rebecca" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color "#ff9ecf"
                action [Hide("characters"), Show("character_stats", character="rebecca")]

            textbutton "Robin" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color "#09195f"
                action [Hide("characters"), Show("character_stats", character="robin")]

            textbutton "Uta" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color DIVINE_PURPLE
                action [Hide("characters"), Show("character_stats", character="uta")]

            textbutton "Vivi" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color DIVINE_BLUE
                action [Hide("characters"), Show("character_stats", character="vivi")]

            textbutton "Kalifa" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color DIVINE_GOLD
                action [Hide("characters"), Show("character_stats", character="kalifa")]

            textbutton "Zala" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button_fixed"
                text_color DIVINE_WHITE
                action [Hide("characters"), Show("character_stats", character="zala")]

            null height 16

            # UNIVERSAL CLOSE BUTTON
            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5

###############################################
# CHARACTER STATS SCREEN (DIVINE AURA)
###############################################
screen character_stats(character):
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    frame at cheat_screen_in, divine_screen_aura:
        xalign 1.0
        yalign 0.0
        xsize 320
        yfill True
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 12

            ###########################################
            # CHARACTER NAME TITLE
            ###########################################
            $ char_labels = {
                "alvida": "Alvida",
                "yamato": "Yamato",
                "hancock": "Hancock",
                "nami": "Nami",
                "perona": "Perona",
                "rebecca": "Rebecca",
                "robin": "Robin",
                "uta": "Uta",
                "vivi": "Vivi",
                "kalifa": "Kalifa",
                "zala": "Zala",
            }
            $ title_name = char_labels.get(character, character.capitalize())

            text "[title_name] Cheats" size 32 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5


            ###########################################
            # CHARACTER STAT LISTS
            ###########################################
            if character == "alvida":
                $ stats = [
                    ("alvida_love", "Love", DIVINE_PINK),
                    ("alvida_lust", "Lust", DIVINE_RED),
                ]

            elif character == "yamato":
                $ stats = [
                    ("yamato_love", "Love", DIVINE_PINK),
                    ("yamato_lust", "Lust", DIVINE_RED),
                ]

            elif character == "hancock":
                $ stats = [
                    ("hancock_love", "Love", DIVINE_PINK),
                    ("hancock_lust", "Lust", DIVINE_RED),
                    ("hancock_subm", "Submission", DIVINE_GOLD),
                ]

            elif character == "nami":
                $ stats = [
                    ("nami_love", "Love", DIVINE_PINK),
                    ("nami_lust", "Lust", DIVINE_RED),
                ]

            elif character == "perona":
                $ stats = [
                    ("perona_love", "Love", DIVINE_PINK),
                    ("perona_lust", "Lust", DIVINE_RED),
                    ("perona_subm", "Submission", DIVINE_GOLD),
                ]

            elif character == "rebecca":
                $ stats = [
                    ("rebecca_love", "Love", DIVINE_PINK),
                    ("rebecca_lust", "Lust", DIVINE_RED),
                    ("rebecca_subm", "Submission", DIVINE_GOLD),
                ]

            elif character == "robin":
                $ stats = [
                    ("robin_love", "Love", DIVINE_PINK),
                    ("robin_lust", "Lust", DIVINE_RED),
                ]

            elif character == "uta":
                $ stats = [
                    ("uta_love", "Love", DIVINE_PINK),
                    ("uta_lust", "Lust", DIVINE_RED),
                    ("uta_subm", "Submission", DIVINE_GOLD),
                ]

            elif character == "vivi":
                $ stats = [
                    ("vivi_love", "Love", DIVINE_PINK),
                    ("vivi_lust", "Lust", DIVINE_RED),
                    ("vivi_subm", "Submission", DIVINE_GOLD),
                ]

            elif character == "kalifa":
                $ stats = [
                    ("kalifa_love", "Love", DIVINE_PINK),
                    ("kalifa_lust", "Lust", DIVINE_RED),
                    ("kalifa_subm", "Submission", DIVINE_GOLD),
                ]

            elif character == "zala":
                $ stats = [
                    ("zala_love", "Love", DIVINE_PINK),
                    ("zala_lust", "Lust", DIVINE_RED),
                ]

            else:
                $ stats = []


            ###########################################
            # DIVINE STAT BUTTONS
            ###########################################
            for varname, label, col in stats:
                textbutton "[label]" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                    style "cheat_button_fixed"
                    text_color col
                    action [
                        Hide("character_stats"),
                        Show("stat_detail", varname=varname, label=label, character=character)
                    ]

            null height 20


            ###########################################
            # UNIVERSAL CLOSE BUTTON
            ###########################################
            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5

###############################################
# RESOURCE STATS SCREEN (DIVINE AURA)
###############################################
screen resource_stats():
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    frame at cheat_screen_in, divine_screen_aura:
        xalign 1.0
        yalign 0.0
        xsize 320
        yfill True
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 12

            ###########################################
            # TITLE
            ###########################################
            text "Resource Cheats" size 32 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5


            ###########################################
            # RESOURCE LIST
            ###########################################
            $ resource_list = [
                ("berries", "Berries", DIVINE_GOLD),
                ("gold", "Gold", DIVINE_GOLD),
                ("iron", "Iron", DIVINE_WHITE),
                ("wood", "Wood", "#8B4513"),
                ("food", "Food", DIVINE_GREEN),
                ("paper", "Paper", DIVINE_WHITE),
                ("fabric", "Fabric", DIVINE_PINK),
            ]

            for varname, label, col in resource_list:
                textbutton "[label]" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                    style "cheat_button_fixed"
                    text_color col
                    action [
                        Hide("resource_stats"),
                        Show("stat_detail", varname=varname, label=label, character="Resources")
                    ]

            null height 20


            ###########################################
            # UNIVERSAL CLOSE BUTTON
            ###########################################
            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5

###############################################
# STAT DETAIL SCREEN (ABSOLUTE DIVINITY)
###############################################


init 999 python:
    for stat in [
        "nami_lust", "nami_love",
        "robin_lust", "robin_love",
        "zala_lust", "zala_love",
        "kalifa_lust", "kalifa_love", "kalifa_subm",
        "vivi_lust", "vivi_love", "vivi_subm",
        "uta_lust", "uta_love", "uta_subm",
        "rebecca_lust", "rebecca_love", "rebecca_subm",
        "perona_lust", "perona_love", "perona_subm",
        "hancock_lust", "hancock_love", "hancock_subm",
        "alvida_lust", "alvida_love",
        "yamato_lust", "yamato_love",
    ]:
        detail_inputs.setdefault(stat, "")

screen stat_detail(varname, label, character):
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    # Divine halo frame
    frame at cheat_screen_in, divine_frame_halo:
        xalign 0.5
        yalign 0.10
        xsize 380
        background "#000000dd"
        padding (20, 20)

        vbox:
            spacing 16

            ###########################################
            # CURRENT VALUE DISPLAY
            ###########################################
            $ cur_val = getattr(renpy.store, varname, 0)
            if hasattr(cur_val, "value"):
                $ display_val = cur_val.value
            elif hasattr(cur_val, "level"):
                $ display_val = cur_val.level
            elif isinstance(cur_val, (int, float)):
                $ display_val = cur_val
            else:
                $ display_val = "❌Unsupported"

            text "[label] (Current: [display_val])" size 28 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5


            ###########################################
            # INPUT FIELD + APPLY BUTTON
            ###########################################
            hbox:
                spacing 10
                xalign 0.5

                # Divine input field
                input:
                    id "input_" + varname
                    value DictInputValue(detail_inputs, varname)
                    length 6
                    allow "-0123456789"
                    xsize 120
                    color DIVINE_WHITE

                # Apply button
                textbutton "Apply" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                    style "cheat_button"
                    text_color DIVINE_BLUE
                    action Function(
                        apply_var_change_safe,
                        varname,
                        detail_inputs.get(varname, ""),
                        label
                    )


            ###########################################
            # QUICK + / - BUTTONS
            ###########################################
            hbox:
                spacing 12
                xalign 0.5

                textbutton "+" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                    style "cheat_button"
                    text_color DIVINE_GOLD
                    action Function(apply_var_change_safe, varname, "1", label)

                textbutton "–" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                    style "cheat_button"
                    text_color DIVINE_RED
                    action Function(apply_var_change_safe, varname, "-1", label)


            ###########################################
            # BACK BUTTON
            ###########################################
            textbutton "Back to [character]" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_WHITE
                action [
                    Hide("stat_detail"),
                    Show("resource_stats" if character == "Resources" else "character_stats", character=character)
                ]
                xalign 0.5

            null height 10

            ###########################################
            # UNIVERSAL CLOSE BUTTON
            ###########################################
            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5

###############################################
# SAFE STAT CHANGE FUNCTION (ABSOLUTE DIVINITY)
###############################################
init python:
    def apply_var_change_safe(varname, amount_str, label=None):
        # Convert input to integer safely
        amt = safe_int(amount_str)
        if amt is None:
            renpy.store.cheat_error = "Invalid input: must be a number."
            return

        # Get current value
        cur = getattr(renpy.store, varname, 0)

        ###########################################
        # CASE 1 — Simple int/float
        ###########################################
        if isinstance(cur, (int, float)):
            new_val = cur + amt
            setattr(renpy.store, varname, new_val)
            renpy.notify(f"{label or varname} → {new_val}")
            return

        ###########################################
        # CASE 2 — Objects with .value
        ###########################################
        if hasattr(cur, "value"):
            try:
                cur.value += amt
                if cur.value < 0:
                    cur.value = 0
                renpy.notify(f"{label or varname} → {cur.value}")
            except Exception as e:
                renpy.store.cheat_error = f"Cannot edit {varname}: {e}"
            return

        ###########################################
        # CASE 3 — Objects with .level
        ###########################################
        if hasattr(cur, "level"):
            try:
                cur.level += amt
                renpy.notify(f"{label or varname} → {cur.level}")
            except Exception as e:
                renpy.store.cheat_error = f"Cannot edit {varname}: {e}"
            return

        ###########################################
        # CASE 4 — Fallback (attempt +=)
        ###########################################
        try:
            new_val = cur + amt
            setattr(renpy.store, varname, new_val)
            renpy.notify(f"{label or varname} → {new_val}")
        except Exception as e:
            renpy.store.cheat_error = f"Cannot edit {varname}: unsupported type."

screen cheat_minigames():
    tag cheat
    modal True
    zorder 201

    frame at cheat_screen_in, divine_screen_aura:
        xalign 0.5
        yalign 0.0
        xsize 600
        ysize 900
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 30

            text "Minigame Cheats" size 40 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5

            textbutton "Memory Game" style "cheat_button":
                text_color DIVINE_BLUE
                action Show("cheat_memory")

            textbutton "Fishing Game" style "cheat_button":
                text_color DIVINE_BLUE
                action Show("cheat_fishing")

            textbutton "Ship Battle" style "cheat_button":
                text_color DIVINE_BLUE
                action Show("cheat_shipbattle")

            textbutton "Cards Game" style "cheat_button":
                text_color DIVINE_BLUE
                action Show("cheat_cards")

            null height 40

            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5

screen cheat_memory():
    tag cheat
    modal True
    zorder 201

    frame at cheat_screen_in, divine_screen_aura:
        xalign 0.5
        yalign 0.0
        xsize 600
        ysize 700
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 20

            text "Memory Game Cheats" size 35 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5

            textbutton "Freeze Timer" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_memory_freeze else DIVINE_RED)
                action ToggleVariable("cheat_mg_memory_freeze")

            textbutton "Reveal All Cards" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_memory_reveal else DIVINE_RED)
                action ToggleVariable("cheat_mg_memory_reveal")

            textbutton "Auto-Win" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_memory_autowin else DIVINE_RED)
                action ToggleVariable("cheat_mg_memory_autowin")

            null height 40

            textbutton "Back" style "cheat_button":
                text_color DIVINE_RED
                action [Hide("cheat_memory"), Show("cheat_minigames")]
                xalign 0.5

            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5


screen cheat_fishing():
    tag cheat
    modal True
    zorder 201

    frame at cheat_screen_in, divine_screen_aura:
        xalign 0.5
        yalign 0.0
        xsize 600
        ysize 700
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 20

            text "Fishing Game Cheats" size 35 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5

            textbutton "Freeze Fish" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_fishing_freeze_fish else DIVINE_RED)
                action ToggleVariable("cheat_mg_fishing_freeze_fish")

            textbutton "Super Progress Gain" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_fishing_super_gain else DIVINE_RED)
                action ToggleVariable("cheat_mg_fishing_super_gain")

            textbutton "No Progress Loss" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_fishing_no_loss else DIVINE_RED)
                action ToggleVariable("cheat_mg_fishing_no_loss")

            textbutton "Auto-Win" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_fishing_autowin else DIVINE_RED)
                action ToggleVariable("cheat_mg_fishing_autowin")

            null height 40

            textbutton "Back" style "cheat_button":
                text_color DIVINE_RED
                action [Hide("cheat_fishing"), Show("cheat_minigames")]
                xalign 0.5

            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5


screen cheat_shipbattle():
    tag cheat
    modal True
    zorder 201

    frame at cheat_screen_in, divine_screen_aura:
        xalign 0.5
        yalign 0.0
        xsize 600
        ysize 900
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 20

            text "Ship Battle Cheats" size 35 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5

            textbutton "Infinite HP" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_ship_inf_hp else DIVINE_RED)
                action ToggleVariable("cheat_mg_ship_inf_hp")

            textbutton "Always Hit" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_ship_always_hit else DIVINE_RED)
                action ToggleVariable("cheat_mg_ship_always_hit")

            textbutton "Enemy Always Miss" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_ship_enemy_miss else DIVINE_RED)
                action ToggleVariable("cheat_mg_ship_enemy_miss")

            textbutton "Infinite Cannonballs" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_ship_inf_cannon else DIVINE_RED)
                action ToggleVariable("cheat_mg_ship_inf_cannon")

            textbutton "100% Boarding" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_ship_boarding else DIVINE_RED)
                action ToggleVariable("cheat_mg_ship_boarding")

            textbutton "100% Escape" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_ship_escape else DIVINE_RED)
                action ToggleVariable("cheat_mg_ship_escape")

            textbutton "Max Loot" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_ship_max_loot else DIVINE_RED)
                action ToggleVariable("cheat_mg_ship_max_loot")

            null height 40

            textbutton "Back" style "cheat_button":
                text_color DIVINE_RED
                action [Hide("cheat_shipbattle"), Show("cheat_minigames")]
                xalign 0.5

            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5



screen cheat_cards():
    tag cheat
    modal True
    zorder 201

    frame at cheat_screen_in, divine_screen_aura:
        xalign 0.5
        yalign 0.0
        xsize 600
        ysize 700
        background "#000000cc"
        padding (20, 20)

        vbox:
            spacing 20

            text "Cards Game Cheats" size 35 color DIVINE_GOLD outlines DIVINE_RAINBOW_OUTLINES xalign 0.5

            textbutton "Always Win" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_cards_always_win else DIVINE_RED)
                action ToggleVariable("cheat_mg_cards_always_win")

            textbutton "Easy Streak (1 Win)" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_cards_easy else DIVINE_RED)
                action ToggleVariable("cheat_mg_cards_easy")

            textbutton "No Loss" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_cards_no_loss else DIVINE_RED)
                action ToggleVariable("cheat_mg_cards_no_loss")

            textbutton "Auto-Win" style "cheat_button":
                text_color (DIVINE_GREEN if cheat_mg_cards_autowin else DIVINE_RED)
                action ToggleVariable("cheat_mg_cards_autowin")

            null height 40

            textbutton "Back" style "cheat_button":
                text_color DIVINE_RED
                action [Hide("cheat_cards"), Show("cheat_minigames")]
                xalign 0.5

            textbutton "Close Menu" at cheat_button_idle_t, cheat_button_hover_t, cheat_button_click_t:
                style "cheat_button"
                text_color DIVINE_RED
                action [
                    Hide("cheat_menu"),
                    Hide("characters"),
                    Hide("character_stats"),
                    Hide("resource_stats"),
                    Hide("stat_detail"),
                    Hide("cheat_minigames"),
                    Hide("cheat_memory"),
                    Hide("cheat_fishing"),
                    Hide("cheat_shipbattle"),
                    Hide("cheat_cards")
                ]
                xalign 0.5
