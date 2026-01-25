# Version event: 5
# Version game: 0.38

label event_robin_peek:
    window hide
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "ship_girls_room"
    
    scene BG locations:
        blur 3
    show events robin peek robin_room_peek:
        xalign 0.5
        yalign 1.0

    hide screen screen_black with Dissolve(0.3)
    window auto

    pause 1.0
    player "(Wow!!! I arrived just for the show!)"   
    player "(It's [robin.n] undressing, sooo fuckin sexy!!)"    
    player "(That smooth skin... those curves... I could watch forever...)"
    player "(She's like a goddess, but dangerous enough to kill me with a smile...)"

    show events robin peek robin_room_peek2 with Dissolve(0.3):
        xalign 0.5
        yalign 1.0


    if robin_love >= 20:

        robin "Fufufu... coming in without permission, huh?"     
        robin "My Captain has gotten pretty shameless."
        player "I-I'm so sorry! I didn't hear you..."   
        robin "Although I have to admit, I like this version of you more. More... impulsive!"
        player "!!!"   

        if robin_lust >= 20:

            robin "Close the door, [player.n]. I don't want the other girls to have a heart attack if they see us."
            robin "Come on, sit next to me... or better yet..."
            player "?!?!"   
            robin "Hehe, I can keep reading while giving you all the attention you deserve."
            robin "After all, an archaeologist knows the best discoveries are made without warning!"

            $ robin_lust += 1
            narrador "[robin.n] Lust +1"
        

        robin "Haha, I'm just messing with you! Don't take it seriously."
        robin "But next time, try to let me know before coming in!"

        $ robin_love += 1
        narrador "[robin.n] Love +1"


    else:

        robin "[player.n]!! How did you come in without knocking!"
        robin "Do you make a habit of barging into a lady's room?"
        player "I... I just wanted to check if everything was alright..."
        robin "By sneaking through the keyhole first? How bold..."
        player "(Damn... she caught me red-handed...)"
        robin "You better get out right now, if you don't want to see me angry!"
        player "I'm so sorry! I thought it was empty..."
        robin "Leave here now!!!"
        player "(Shiiit!!! I arrived way too early...)"
        player "(But that view... totally worth the trouble...)"

        $ robin_love -= 1
        narrador "[robin.n] Love -1"

    $ game.clock.next()
    jump ship_mid
    
