# Version event: 4
# Version game: 0.6

label event_robin_call:

    show robin c1 with dissolve

    robin "Hello, Captain. Do you need anything from me?"

    jump event_robin_call_menu

label event_robin_call_menu:
    menu:
        "Normal Chatting":
            call robin_hangout from _call_robin_hangout_call

        "Lewd":
            jump event_robin_lewd

        "Give":
            call event_robin_give from _call_event_robin_give_call
            jump event_robin_call_menu

        "Dismiss Her":
            player "That's all, [robin.n]. You can go back to your tasks."

            if robin_love < 10: 
                show robin anger with Dissolve(0.2)
                robin "If there's nothing important to do, please try not to waste my time. I get distracted from my research!"

            elif robin_love < 20:
                show robin with dissolve
                robin "Great, Captain. You know I'm here if you need any advice!"

            elif robin_love >= 20:
                show robin with dissolve
                robin "What a shame! I thought we would continue spending time together. Call me again whenever you wish, Captain!"

                if robin_lust >= 20:
                    robin "Time flew by so quickly!! You know I love learning anything with you. When you have time, I'd like you to teach me more privately!"
                else:
                    robin "If you need anything else, just call me!"

    window hide
    hide robin with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location