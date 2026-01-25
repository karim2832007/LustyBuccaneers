# Version event: 2
# Version game: 0.26

label vivi_cook:
    show vivi c1 with dissolve
    player "Hi [vivi.n], good to see you! I just have a problem here..."
    player "[nami.n] got mad at me for a debt and forced me to take care of today's meal in her place... I have no idea what to do..." 
    player "What do you say, can you give me a hand?"
    player "I don't know who took care of the meals in [Arabasta.n], as a princess you probably had your own cooks, but maybe you learned a thing or two"
    player "Some of the girls are better at it than me, but I think we can learn and have fun together!"

    if vivi_love < 5: 
        narrador "Requires [vivi.n] love greater than 5"
        show vivi anger with Dissolve(0.2)
        vivi "I'm just kind of busy today... Besides..."
        vivi "As you said, an princess like me cannot dirty her hands with such basic tasks in [Arabasta.n]... And here too!"
        show vivi annoyed with Dissolve(0.2)
        vivi "Sorry... Maybe next time..."

    else: 
        vivi "Just like you say... A princess like me wouldn't have to deal with these tasks..."
        vivi "But now that's changed!... This time will be different, I have to learn and be self-sufficient!"
        vivi "Tell me what to do [player.n], this could be fun..."
        $ vivi_love += 2
        narrador "[vivi.n] Love +2"

    $ game.clock.next()
    #_ se puede hacer sin saltar
    jump expression game.location