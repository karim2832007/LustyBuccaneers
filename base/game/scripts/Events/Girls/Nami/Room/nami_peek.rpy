# Version event: 2
# Version game: 0.38

label event_nami_peek:
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "ship_girls_room"
    
    scene BG locations:
        blur 3
    show events nami peek nami_room_peek:
        xalign 0.5
        yalign 1.0

    hide screen screen_black with Dissolve(0.3)
    window auto

    pause 0.5
    player "(Wow!!! It's [nami.n] undressing, she is sooo sexy!!)"

    if nami_love >= 20:

        nami "[player.n], How did you come in without knocking!"
        player "He... hmnm... I-I'm so sorry! I didn't hear..."        
        nami "Stop!! Coming in without warning? You've gotten pretty bold, [player.n]."
        nami "Although... I guess certain freedoms are allowed for us now... right?"


        if nami_lust >= 20:

            nami "Lock the door..."
            player "Yeee-Yes [nami.n]-san!" 
            nami "Or would you rather someone interrupt us right when I'm getting comfortable with you?"
            nami "Come here, Captain. If you're going to invade my privacy, at least do it properly."
            nami "Maybe I'll charge you interest for this surprise visit... but I can accept other forms of payment..."
            nami "Maybe I could stop by your room later and collect it."
            player "That would be great, I'll be waiting!"

            $ nami_lust += 1
            narrador "[nami.n] Lust +1"
        

        nami "Haha, It's fine this time! I like your visits!"
        nami "But next time, try to let me know before coming in!"

        $ nami_love += 1
        narrador "[nami.n] Love +1"

    else:
        nami "[player.n], How did you come in without knocking!"
        nami "Every second you stay here, you owe me more [Berries.n]!! Get out right away!"
        player "I'm so sorry! I didn't hear anyone, I thought it was empty..."
        nami "I'm not interested, leave here now!!!"
        player "(Shiiit!!! I arrived very early...)"
        $ nami_love -= 1
        narrador "[nami.n] Love -1"


    $ game.clock.next()
    jump ship_mid
    
