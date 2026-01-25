# Version event: 2
# Version game: 0.12

label hancock_cook:
    show hancock c1 with dissolve
    player "Hello [hancock.n]! I was just needing help with today's cooking... What do you say, can you give me a hand?"
    player "I don't know who took care of the meals in [AmazonLily.n], as an empress you probably had your own cooks, but I can teach you!"
    player "Some of the girls are better at it than me, but I think we can learn and have fun together!"

    if hancock_love < 5: 
        narrador "Requires [hancock.n] love greater than 5"
        show hancock anger with Dissolve(0.2)
        hancock "Just because you're the Captain doesn't mean I'll do everything you say..."
        hancock "As you said, an empress like me cannot dirty her hands with such basic tasks in [AmazonLily.n]... And here too!"
        show hancock annoyed with Dissolve(0.2)
        hancock "I have better things to do... Until next time..."

    else: 
        hancock "As you say, an empress like me cannot dirty her hands with such basic tasks in [AmazonLily.n]..."
        hancock "But... This time will be different, I have to learn and be self-sufficient!"
        hancock "Tell me what to do [player.n], this could be fun..."
        $ hancock_love += 2
        narrador "[hancock.n] Love +2"

    $ game.clock.next()
    #_ se puede hacer sin saltar
    jump expression game.location