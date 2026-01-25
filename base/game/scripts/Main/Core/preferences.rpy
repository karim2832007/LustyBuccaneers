# Version event: 2
# Version game: 0.15

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "any window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")

                    if not preferences.transitions:
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

                vbox:
                    style_prefix "radio"
                    label _("Language")

                    textbutton "English":
                        action Language(None)  # Default language
                        xalign 0.0   

                    textbutton "Spanish":
                        action Language("spanish")
                        xalign 0.0
                
                    textbutton "Portuguese":
                        action Language("portuguese")
                        xalign 0.0

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                    label _("Textbox Opacity")
                    bar value VariableValue("persistent.textbox_alpha", range=1.0, step=0.05) style "slider_slider"

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox



style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

#--------------------------------------------------------

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    ysize 65
    properties gui.button_properties("radio_button")
    #idle_background "GUI game_menu radio_off"
    #hover_background "GUI game_menu radio_hover"
    selected_background "GUI game_menu radio_on"
    xpadding 45

#style radio_button_text:
#    properties gui.button_text_properties("radio_button")

#style radio_button:
#    variant "small"
#    foreground "gui/phone/button/radio_[prefix_]foreground.png"

#--------------------------------------------------------

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    ysize 65
    properties gui.button_properties("check_button")
    idle_background "GUI game_menu check_off"
    hover_background "GUI game_menu check_hover"
    selected_background "GUI game_menu check_on"
    xpadding 45


#style check_textbutton:
#    properties gui.button_text_properties("check_button")
#    idle_background "GUI game_menu check_hover"
#    hover_background "GUI game_menu check_hover"

#style check_button_text:
#    properties gui.button_text_properties("check_button")
#    idle_background "GUI game_menu check_hover"
#    hover_background "GUI game_menu check_hover"

#style check_button:
#    variant "small"
#    foreground "gui/phone/button/check_[prefix_]foreground.png"

#--------------------------------------------------------

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

style slider_slider:
    xysize (525,55)
    left_gutter 8
    right_gutter 16
    left_bar Frame("GUI game_menu bar_full",32,0,)
    right_bar Frame("GUI game_menu bar_empty",32,0)
    thumb_offset 27
    thumb "GUI game_menu bar_thumb"
    hover_thumb "GUI game_menu bar_thumb"