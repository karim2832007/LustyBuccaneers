# Version event: 3
# Version game: 0.37

label haki_h3():
    if Haki.h == 2:
        narrador "When you arrive at the bar looking for [rayleigh.n], you see him in a corner talking to one of the girls."

        show rayleigh c1:
            xalign 0.15
            yalign 1.0

        show girl_2:
            xalign 0.75
            yalign 1.0

        with dissolve


        pause 0.2
        girl_2 "Buuuuuut you told me we were going shopping!!!"
        girl_2 "Why do you always do this to me, [rayleigh.n]!?!"
        girl_2 "You keep standing me up!!"
        rayleigh "Hahaha what are you talking about, girl!"
        rayleigh "I never said we were going out for a walk... Don't make me look bad in front of the people around here! Hahaha"
        pause 0.5
        rayleigh "Today's a bit complicated for me, you know... Maybe we could plan for another day..."
        girl_2 "{size=45}Nooooooo!!{/size}"
        girl_2 "That's not how things work!! You'll have to make it up to me right now!!!"
        pause 0.5
        girl_2 "No one stands me up!"
        rayleigh "Uh... It's just... I don't know, maybe... Or better..."
        pause 0.5
        rayleigh "!!!"
        pause 0.5
        rayleigh "Look... My boy here came looking for me... I told you I was busy today!!"
        player "Hii..."
        rayleigh "Come closer, kid... I was waiting for you."
        player "But... How did you know I was coming, [rayleigh.n]?"
        rayleigh "Hahaha what do you mean... We already had plans today..."
        rayleigh "{size=20}Play along, kid...{/size}"
        girl_2 "Mmnmn... Interesting..."
        girl_2 "I didn't know you had such... Sexy friends..."
        player "(.... Is she talking about me?!?!)"
        rayleigh "Hahahaha always so blunt... That's what I like about you..."
        rayleigh "You two can grab some drinks another day..."
        player "But why another day... It could be ri—"
        rayleigh "Hahaha hush hush! Come on kid, let's get out of here... We've got a lot of work to do..."

        hide rayleigh with moveoutleft

        player "Wait, don't leave!"
        pause 0.5
        girl_2 "Hahaha I hope to see you another day... sexy boy."

        $ _window_hide()    
        show screen screen_black with Dissolve(0.6)
        hide girl_2 with Dissolve(0.8)
        $ game.location = "shells_town_outside"
        scene BG locations:
            blur 3
        hide screen screen_black with Dissolve(0.3)

        pause 1.0
        
        narrador "After getting some distance, you find yourself in a clearing on the outskirts of the city..."
        pause 0.5
        narrador "In the distance, you can even see the Marine Base, 153rd Division."

        show rayleigh c1 with Dissolve(0.2):
            xalign 0.5
            yalign 1.0

        rayleigh "Phew... Good thing we got away..."
        rayleigh "She's a good girl, but she can be really exhausting and spoiled sometimes..."
        pause 0.5
        rayleigh "You handled yourself well, kid..."
        rayleigh "I owe you some beers next time..."
        pause 0.5
        rayleigh "Alright... I'll take my leave first..."
        pause 0.5

        show rayleigh c1:
            xalign 0.5
            yalign 1.0
            linear 0.4 xalign 0.9
        pause 0.5
        player "Wait, [rayleigh.n]!!"

        rayleigh "Mnmn?!?"
        pause 0.5  
        show rayleigh c1:
            xalign 0.9
            yalign 1.0
            linear 0.4 xalign 0.5

        rayleigh "What is it, kid..."
        player "Back at the bar, I came looking for you... You said you were going to train me!"
        rayleigh "Ah... That's right... We talked about that last time..."
        rayleigh "Alright..."
        rayleigh "How should we do this..."
        rayleigh "Mnmnm...."
        rayleigh "Well... Even though I said that, and I know you've got potential... I think you should prove your worth first..."
        rayleigh "Like I told you, there are thousands of people with potential... but very few manage to make use of it..."
        player "Alright!! I don't mind... How can I prove my worth?"
        rayleigh "Well then..."
        rayleigh "Maybe the first thing is to show me your fundamentals..."
        rayleigh "Without a solid foundation... anything we build will collapse..."
        rayleigh "And if you can't handle this, it'll be very hard for me to train you..."
        player "Alright, no problem... what do I need to do?"
        rayleigh "Well, let's start with something easy, kid..."
        rayleigh "Give me 100 push-ups... Without stopping, obviously..."
        player "!!!"
        player "Alright!! I'll do it, master!"

        $ Haki.h = 3

    else:
        pause 0.5
        show rayleigh c1:
            xalign 0.5
            yalign 1.0

        rayleigh "Here we are again, kid... Let's see if you've improved."
        rayleigh "Let's go outside and repeat the training from the beginning!"
        player "!!!"
        player "Alright!! I'll do it, master!"

    if Strength < 10:
        narrador "You need 10 strength, and your current strength is [Strength]."

        rayleigh "You still need to train your body more. Come back when you're ready."
        rayleigh "For now, let's return to the bar."

        $ _window_hide()
        hide rayleigh with Dissolve(0.8)    
        jump shells_town_bar

    $ _window_hide()    
    show screen screen_black with Dissolve(0.6)
    $ game.clock.next()
    hide screen screen_black with Dissolve(0.3)

    pause 1.0

    rayleigh "Very well done!"
    player "Thank you, master!"
    rayleigh "But... the day doesn't end here..."
    rayleigh "Now I want you to follow me... We're running 100 laps around that mountain."
    player "!!!"
    player "You've got to be kidding me, right?!"
    pause 0.5
    rayleigh "Do I... Look like I'm kidding?!?"
    rayleigh "Follow me... I don't have a slow pace..."

    if Strength < 15:
        narrador "You need 15 strength, and your current strength is [Strength]."

        rayleigh "Looks like you still don't have what it takes... You still need to train your body more."
        rayleigh "For now, let's return to the bar."

        $ _window_hide()
        hide rayleigh with Dissolve(0.8)    
        jump shells_town_bar

    $ _window_hide()    
    show screen screen_black with Dissolve(0.6)
    $ game.clock.next()
    hide screen screen_black with Dissolve(0.3)

    show rayleigh c1 with Dissolve(0.2):
        xalign 0.5
        yalign 1.0

    player "Ugh... We're finally done..."
    pause 0.5
    player "I hate running..."
    pause 0.5
    rayleigh "Hahaha! Always so straightforward... I like that..."
    rayleigh "Well then... You've fulfilled it... You're at an... acceptable level..."
    rayleigh "Looks like your body is ready... We can continue!"
    player "Great!! Excellent, master... what's the next step?"
    pause 0.5
    rayleigh "Calm down, boy... There's no rush... This is only the beginning..."
    rayleigh "We'll continue your training another time... It will be a... special... kind of training..."
    rayleigh "For now, let's go back to the bar."
    pause 0.4   

    $ _window_hide()
    hide rayleigh with Dissolve(0.8)    

    $ Haki.h = 4
    jump shells_town_bar