# Version event: 2
# Version game: 0.37

image movie_robin_undressing = MovieFallback(play="movie/robin/undressing/1.webm", image="movie/robin/undressing/img.webp", character="robin")

label robin_undressing:
    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    
    $ game.location = "ship_bathroom"
    scene BG locations:
        blur 3
    
    show robin c1_bra at center

    show movie_robin_undressing:
        xalign 0.5
        yalign 1.0

    hide screen screen_black with Dissolve(0.3)
    pause 2.0

    player "(Woow… this is NOT what I expected when I walked into the bathroom.)"
    player "(Is [robin.n]... changing!? Why right now of all times?!)"
    player "(God, what a body... every part of it... pure perfection...)"
    player "(Focus, idiot! I need to say something and fix this...)"
    player "(Don't look. Don't look! ...Okay, I looked—no going back now... but it was like half a second!)"
    player "(How am I supposed to explain this without looking like a lucky pervert?)"
    player "(She's definitely going to kill me... and honestly, it might be worth it...)"

    if robin_love >= 30:

        robin "What are you doing here!?"
        player "Ah! I'm sorry! I didn't know someone was inside!"
        robin "You didn't know...? And it didn't occur to you to knock before entering?"

        if robin_lust >= 30:
            robin "Oh... so you prefer dramatic entrances. Or could it be you just couldn't resist the curiosity?"
            robin "Was that an accident... or a very clumsy attempt at flirting?"
            player "It was an accident! I swear it wasn't on purpose... But if you like the second one..."
            robin "Hehe..."
            robin "Did you like what you saw? I hope you at least earned it with a bet."
            robin "I hope it stays engraved in your memory... as a nice, sexy little memory..."
            player "(Oh, it sure did!! Engraved—burned into my brain, I swear!)"
            robin "I knew this crew was bold, but not THAT bold..."

            pause 0.5
            hide movie_robin_undressing with Dissolve(0.5)
            show robin smile with Dissolve(0.3)

            robin "Anyway... since you're already here, you could at least hand me the towel. Or does that make you nervous too?"
            player "(Look at those breasts... they're incredible...)"
            player "(I don't think any man could ever get tired of this view...)"
            robin "Hey, are you still there?!"
            robin "I'm... in the middle of changing."
            player "I can see that—! I mean— I didn't see anything! I swear I didn't!"
            robin "Hhaha it wouldn't be the first time!!"
            robin "We know each other pretty well by now! Not much left to be embarrassed about..."
            player "Hahah that's true, but still, I'm really sorry."
            robin "It's fine. Just make sure you learn the rule: on this ship, ask before going in is law"
            robin "There are lots of girls around here... or is it that you want to see all of them naked?!"
            player "...Well maybe..."
            robin "Hahah shut up, Captain! Now leave please!"
            player "Yes, ma'am!"
            
            $ robin_love += 1
            $ robin_lust += 1
            narrador "[robin.n] Love and lust +1"            

        else:
            pause 0.5
            hide movie_robin_undressing with Dissolve(0.5)
            show robin neutral with Dissolve(0.3)
            pause 0.5

            robin "Well... what's done is done..."
            robin "I'm... in the middle of changing, so maybe you could let me finish..."
            player "I can see that—! I mean— I didn't see anything! I swear I didn't!"
            robin "Hahah you're so cute, [player.n]... I can't stay mad at you..."
            robin "Relax... no need to stare at the ceiling. It's too late for that anyway."
            player "I'm really embarrassed. I'm sorry, [robin.n]!"
            player "Please don't misunderstand... I didn't mean anything bad."
            robin "Maybe not... but that doesn't erase the scene."
            player "Is there anything I can do to make it up to you?"
            robin "Hmm... you could start by leaving. And then bring me a cup of tea without spilling a single drop."
            player "Done! Anything. Tea, coffee, the whole kitchen if needed!"
            player "I'm really sorry, truly."
            robin "It's fine. Just make sure you learn the rule: on this ship, ask before going in is law"
            player "Burned into my memory..."
            robin "I hope so. Now go... before I regret forgiving you so easily."
            player "Yes! I'm going. I'm... out!"
            robin "Please..."
            player "Yes, ma'am!"

    else:
        robin "What are you doing here!?"
        player "Ah! I'm sorry! I didn't know someone was inside!"
        robin "You didn't know...? And it didn't occur to you to knock before entering?"
        player "It was an accident! I swear it wasn't on purpose..."
        robin "Wow... how gentlemanly of you to burst in without asking."

        hide movie_robin_undressing with Dissolve(0.5)
        show robin anger with Dissolve(0.3)

        robin "I'm... in the middle of changing."
        player "I can see that—! I mean— I didn't see anything! I swear I didn't!"
        robin "..."
        player "..."

        $ _window_hide()
        show robin annoyed with Dissolve(0.3)
        pause 0.5

        robin "Relax... no need to stare at the ceiling. It's too late for that."
        player "I'm really embarrassed. I'm sorry, [robin.n]!"
        robin "Hmph... Is this your habit with ladies? Barging in without asking before going in?"
        player "No, of course not! It was clumsiness. Or desperation... to get to the bathroom."
        robin "Desperation? To going in the bathroom like a whirlwind without listening?"
        player "I want to disappear right now..."
        robin "Funny. I'd also like you to disappear... at least for a few seconds."
        player "Please don't misunderstand... I didn't mean anything bad."
        robin "Maybe not... but that doesn't erase the scene."
        player "Is there anything I can do to make it up to you?"
        robin "No, it's too late for that..."
        player "I'm really sorry, truly."
        robin "It's fine. Just make sure you learn the rule: on this ship, ask before going in is law"
        player "Burned into my memory..."
        robin "I hope so. Now go..."
        player "Yes! I'm going. I'm out!"

        $ robin_love -= 1
        narrador "[robin.n] Love -1"


    $ game.clock.next()
    jump ship_mid
    
