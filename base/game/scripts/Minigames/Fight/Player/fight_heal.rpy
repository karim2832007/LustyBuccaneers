# Version event: 2
# Version game: 0.23

label fight_heal():
    python:
        valid_heals = []
        for heal in HEALS:
            item_name = heal["item"]
            
            if globals()[item_name] > 0:
                valid_heals.append(heal)

        selected_heal = valid_heals[action_id]  # Obtener la curación elegida
        item_name = selected_heal["name"]
        item_id = selected_heal["item"]

        talk = RPGPlayer.heal(heal_amount=selected_heal["heal_amount"], min_heal=selected_heal["min_heal"])

        globals()[item_id] -= 1  # Restar el ítem usado

    narrador "-1 [item_name]"
    narrador "[talk]"
    return
