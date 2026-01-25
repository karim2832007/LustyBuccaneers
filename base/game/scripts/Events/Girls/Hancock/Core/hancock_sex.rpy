# Version event: 2
# Version game: 0.27

label hancock_sex:
    menu:
        "Vaginal":
            menu hancock_sex_vaginal:
                "Missionary":
                    #narrador "This event is available in version 0.[version_id_next].\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                    #jump hancock_sex_vaginal
                    jump event_hancock_missionary_vaginal

                "Doggystyle":
                    jump event_hancock_doggystyle

                "Cowgirl":
                    jump event_hancock_cowgirl

                "Back":
                    jump hancock_sex

        "Back":
            jump hancock_lewd
