# Version event: 3
# Version game: 0.6

label event_perona_call:

    show perona c1 with dissolve

    perona "Hello, Captain. Do you need anything from me?"

    jump event_perona_call_menu

label event_perona_call_menu:
    menu:
        "Normal Chatting":
            call perona_hangout from _call_perona_hangout_call

        "Lewd":
            jump event_perona_lewd

        "Give":
            call perona_give from _call_perona_give_call
            jump event_perona_call_menu

        "Dismiss Her":
            player "That's all, [perona.n]. You can go back to your tasks."

            if perona_love < 10: 
                show perona anger with Dissolve(0.2)
                perona "Nobody gives me orders [player.n]! And especially doesn't waste my time... If you don't have something important to say, don't call me..."

            elif perona_love < 20:
                show perona with dissolve
                perona "If you need me for something else, call me. I'm quite bored!"

            elif perona_love >= 20:
                show perona with dissolve
                perona "What a shame, Captain! I'd like to spend more time with you next time... I hope you call me soon!"

                if perona_lust >= 20:
                    perona "If you need anything else, call me! We could even meet tonight, I've been feeling quite lonely lately..."
                else:
                    perona "If you need anything else, call me!"

    window hide
    hide perona with moveoutright
    pause 0.5
    
    $ game.clock.next()
    jump expression game.location