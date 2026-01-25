# Version event: 1
# Version game: 0.28

label uta_sex:
    menu:
        "Vaginal":
            menu:
                "Missionary":
                    jump event_uta_missionary_vaginal
        
                #"Cowgirl":
                #    jump event_uta_cowgirl
        
                "Back":
                    jump uta_sex

        "Anal":
            menu:
                "Doggystyle":
                    jump uta_doggystyle_anal

                "Back":
                    jump uta_sex

        "Back":
            jump uta_lewd
