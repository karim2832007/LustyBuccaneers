# Version event: 2
# Version game: 0.28

label uta_cook:
    show uta c1 with dissolve
    player "Hello [uta.n]! I was just needing help with today's cooking... What do you say, can you give me a hand?"
    player "You're a genius when it comes to music, and I wonder if you're also good at other things, like cooking..." 
    player "I could really use your help, to be honest. If you don't know how, no worries..."
    player "Some of the girls are better at it than me, but I think we can learn and have fun together!"

    if uta_love < 5: 
        narrador "Requires [uta.n] love greater than 5"
        show uta serious with Dissolve(0.2)
        uta "Oh I'm sorry captain, I was just passing by, but I'm in a hurry..."
        uta "I have something urgent to take care of, maybe next time?"


    else: 
        uta "Excellent [player.n]! I love the idea..." 
        uta "I'm sure we'll have fun! Just thinking about spending more time with you is what I like the most."

        $ uta_love += 2
        narrador "[uta.n] Love +2"

    $ game.clock.next()
   
    jump expression game.location