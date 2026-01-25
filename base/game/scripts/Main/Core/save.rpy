# Version event: 1
# Version game: 0.13

init offset = 99

default persistent.save_naming = False


init -999 python:
        
    if persistent.pages_range is None:
        if unicode(persistent._file_page).isnumeric():
            page = int(persistent._file_page)
            persistent.pages_range = (
                (page // 10) - 1 
                if page % 10 == 0 
                else page // 10
            )
        else:
            persistent.pages_range = 0

    class FilePageBase(Action, DictEquality):
        @property
        def pages_range(self):
            page = int(persistent._file_page)
            return (page // 10) - 1 if page % 10 == 0 else page // 10

        def __call__(self):
            if not self.get_sensitive():
                return
            persistent._file_page = self.page

            if str(self.page).isdigit():
                persistent.pages_range = self.pages_range

            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None
    

    class FilePageSave(FilePageBase):
        def __init__(self, page):
            self.page = str(page)

            if page == "auto":
                self.alt = _("File page auto")
            elif page == "quick":
                self.alt = _("File page quick")
            else:
                self.alt = _("File page [text]")

        def get_selected(self):
            return self.page == persistent._file_page

        def predict(self):
            _predict_file_page(self.page)


    class FilePageSaveNext(FilePageBase):
        alt = _("Next file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, increment=1):

            page = persistent._file_page

            if page == "auto":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                elif config.has_quicksave and quick:
                    page = "quick"
                else:
                    page = "1"

            elif page == "quick":
                if increment == 10:
                    page = str((persistent.pages_range + 1) * 10 + 1)
                else:
                    page = "1"

            else:
                page = int(page) + increment

                if max is not None:
                    if page > max:
                        if wrap:
                            if config.has_autosave and auto:
                                page = "auto"
                            elif config.has_quicksave and quick:
                                page = "quick"
                            else:
                                page = "1"
                        else:
                            page = None

                if page is not None:
                    page = str(page)

            self.page = page

        def predict(self):
            _predict_file_page(self.page)


    class FilePageSavePrevious(FilePageBase):
        alt = _("Previous file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True, decrement=1):

            if wrap and max is not None:
                max = str(max)
            else:
                max = None

            page = persistent._file_page

            if page == "auto":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                else:
                    page = max

            elif page == "quick":
                if decrement == 10 and persistent.pages_range > 0:
                    page = str((persistent.pages_range - 1) * 10 + 1)
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            elif page == "1":
                if decrement == 1 and config.has_quicksave and quick:
                    page = "quick"
                elif decrement == 1 and config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            else:
                if int(page) <= decrement:
                    page = max
                else:
                    page = str(int(page) - decrement)

            self.page = page

        def predict(self):
            _predict_file_page(self.page)



screen screen_save_name(slot):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        xsize 700
        ysize 400
        background None

        add "GUI game_menu window_save":
            xalign 0.5
            yalign 0.5
        
        frame:
            yalign 0.0
            xalign 0.5
            background None
            yoffset -105

            if FileLoadable(slot):
                label _("{color=#f00}Overwrite{/color}") style "confirm_prompt"
            else:
                label _("{color=#f78222}New{/color}") style "confirm_prompt"

        vbox:
            yoffset 50
            spacing 30
            label _("Save name:") style "confirm_prompt"

            input:
                value VariableInputValue('save_name')
                length 30
                xalign 0.5
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -+:()'`."

            null width 30

            hbox:
                xfill True
                textbutton _("Yes") action FileAction(slot, confirm=False), Hide("screen_save_name") xalign 0.5 text_size 45
                textbutton _("No") action Hide("screen_save_name") xalign 0.5 text_size 45




    # No
    key "game_menu" action Hide("screen_save_name")

    # Yes
    key "K_RETURN" action FileAction(slot, confirm=False), Hide("screen_save_name")
    key "K_KP_ENTER" action FileAction(slot, confirm=False), Hide("screen_save_name")

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        if CurrentScreenName() == "save":
            frame:
                style "empty"
                style_prefix "check"
                xsize 435
                xalign 0.93
                ypos -0.07

                if persistent.save_naming:
                    textbutton _("Save naming") action ToggleField(persistent,"save_naming")
                else:
                    textbutton _("Save naming") action ToggleField(persistent,"save_naming")

        fixed:
            order_reverse True

            button:
                style "page_label"

                key_events True
                ypos -0.07
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.38

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        if renpy.current_screen().screen_name[0] == "load":
                            action FileAction(slot)
                        else:
                            selected (str(persistent._file_page) + "-" + str(slot) == renpy.newest_slot("[0-9]"))
                            if persistent.save_naming:
                                action SetVariable("save_name", FileSaveName(slot)), Show("screen_save_name", slot=slot)
                            else:
                                action SetVariable("save_name", FileSaveName(slot)), FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot).replace("[","[[").replace("{","{{"):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    style_prefix "page"
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<<") action FilePageSavePrevious(decrement=10)
                    null width 25

                    textbutton _("<") action FilePageSavePrevious()
                    null width 10

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") xminimum 80 text_size 35 text_xalign 0.5 action FilePageSave("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") xminimum 80 text_size 35 text_xalign 0.5 action FilePageSave("quick")

                    for page in range( (persistent.pages_range * 10) + 1 , (persistent.pages_range * 10) + 11 ):
                        textbutton "[page]" xminimum 70 text_size 35 text_xalign 0.5 action FilePageSave(page)

                    null width 10
                    textbutton _(">") action FilePageSaveNext()

                    null width 25
                    textbutton _(">>") action FilePageSaveNext(increment=10)

                if config.has_sync:
                        if CurrentScreenName() == "save":
                            textbutton _("Upload Sync"):
                                action UploadSync()
                                xalign 0.5
                        else:
                            textbutton _("Download Sync"):
                                action DownloadSync()
                                xalign 0.5

