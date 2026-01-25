# Version event: 3
# Version game: 0.1

label event_yamato_call:

    show yamato c1 with dissolve

    yamato "Hello, Captain. Do you need anything from me?"

    jump event_yamato_call_menu

label event_yamato_call_menu:
    menu:
        "Normal Chatting":
            call yamato_hangout from _call_yamato_hangout_call

        "Lewd":
            jump event_yamato_lewd
                
        "Give":
            call event_yamato_give from _call_event_yamato_give_call
            jump event_yamato_call_menu

        "Dismiss Her":
            player "That's all, [yamato.n]. You can go back to your tasks."

            if yamato_love < 10:
                show yamato anger with Dissolve(0.2)
                yamato "If there's nothing important to do, please try not to waste my time. Every second lost in training gives our rivals a greater advantage!"

            elif yamato_love < 20:
                show yamato with dissolve
                yamato "Perfect, Captain. You know where to find me if there are any issues!"

            elif yamato_love >= 20:
                show yamato with dissolve
                yamato "So soon?! We hadn't even warmed up yet!"

                if yamato_lust >= 20:
                    yamato "If you need anything else, call me! I have no problem doing additional training with you at night... I could learn a thing or two if you teach me!"
                else:
                    yamato "If you need anything else, just call me!"


    hide yamato with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location