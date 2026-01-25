# Version event: 1
# Version game: 0.1

## Navigation screen
screen navigation():
    frame:
        xsize 330
        xoffset 45
        yalign 0.5
        background None

        vbox:
            style_prefix "navigation"
            yalign 0.5
            xalign 0.5
            spacing gui.navigation_spacing
        
            if main_menu:
                textbutton _("New Game") action Start()
            else:
                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")
            textbutton _("Settings") action ShowMenu("preferences")

            #textbutton _("Achievements") action ShowMenu("achievements")

            ###############################################################
            # MEMBERSHIP COUNTDOWN (server expiry-based, auto-updating)
            ###############################################################
            python:
                active = membership_active()
                if active:
                    remaining = membership_remaining_seconds()
                    days = remaining // 86400
                    hours = (remaining % 86400) // 3600
                    minutes = (remaining % 3600) // 60
                    seconds = remaining % 60
                    timer_text = f"{days}d {hours:02d}:{minutes:02d}:{seconds:02d}"

            if active:
                frame:
                    background None
                    has vbox

                    # Timer text styled like navigation menu text
                    text timer_text xalign 0.5 style "navigation_button_text"

                    # Auto-update every second
                    timer 1.0 action renpy.restart_interaction

            else:
                vbox:
                    spacing 10
                    textbutton _("Unlock Cheats"):
                        style "navigation_button"
                        text_style "navigation_button_text"
                        action Function(lambda: renpy.call_in_new_context("ask_generated_key"))
            ###############################################################

            if main_menu:
                textbutton _("Credits") action ShowMenu("about")

            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    hover_sound "menu_button"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    xalign 0.5
    size 40
    hover_color "#ff9901"
    color "#fff"
    outlines [(2, "#744005cc", 1, 1)]
    properties gui.button_text_properties("navigation_button")


## Main Menu Screen
screen main_menu():

    tag menu

    add gui.main_menu_background

    if gui.show_name:
        text "V.[config.version]":
            yalign 0.0
            xalign 1.0
            xoffset -20
            color "#3a120550"
            size 20

    if version_id < version_end:
        frame:
            background None
            yoffset 10
            ysize 100
            xsize 325
            xalign 0.5

            vbox:
                style_prefix "new_version"
                yalign 0.5
                xalign 0.5

                textbutton _("New Version")  at new_version:
                    yalign 0.5
                    xalign 0.5
                    text_align 0.5
                    
                textbutton _("Available Here")  at new_version:
                    yalign 0.5
                    xalign 0.5
                    text_align 0.5

            button:
                action OpenURL("https://www.patreon.com/LustyBuccaneers")

    use navigation