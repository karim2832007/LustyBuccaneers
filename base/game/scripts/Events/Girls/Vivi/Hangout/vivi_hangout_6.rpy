# Version event: 3
# Version game: 0.23

label vivi_hangout_6:
    player "Vivi, have you ever regretted not staying in [Arabasta.n]?"
    vivi "Sometimes I wonder... But I know my place will always be in [Arabasta.n], no matter when."
    show vivi c1 serious with Dissolve(0.2)
    vivi "The best thing I can do for the kingdom is to be here with you all… And prevent the past from repeating itself."
    player "Don't worry, with time and the fame we will gain, no one will dare lay a hand on [Arabasta.n] again…"
    player "I promise you!"
    show vivi c1 happy with Dissolve(0.2)
    vivi "That means so much to me, [player.n]."

    $ vivi_love += 2
    narrador "[vivi.n] love +2"

    player "If one day you wish to visit again, you will be able to do so without any problems!"
    player "You will always be part of this crew, no matter the distance."
    show vivi c1 neutral with Dissolve(0.2)
    vivi "You are so good to me, [player.n], a few words and all my doubts disappear..."
    vivi "I trust you so much after everything we went through in Arabasta..."
    vivi "I never stop thinking about the adventures I might miss if we are not together..."


    menu:
        "I can think of several adventures":
            player "I can think of many adventures we could have together... Just you and me!"
            player "But I'm especially interested in the ones just the two of us will have..."
            player "Do you know what I mean?... I really want to get to know you even more beyond everything that happened in your kingdom"
            show vivi c1 shame with Dissolve(0.2)
            vivi "I know exactly what you mean, Captain... It's not that I don't want us to get to know each other better..."
            vivi "But I hope you will be patient with me, I don't want to rush things too much..."
            vivi "I am very inexperienced in all of this..."
            player "Don't worry, we'll take it slow. I'll make sure you never feel uncomfortable!"
            player "(This is excellent, I've got her!! She hasn't refused at all!)"
            show vivi c1 neutral with Dissolve(0.2)
            vivi "Thank you for understanding me, Captain. Shall we talk later?"

            $ vivi_love += 1
            $ vivi_lust += 3
            narrador "[vivi.n] Love +1 and lust +3"

        "We will enjoy great adventures together":
            player "Have no doubt, we will enjoy great adventures together"          
            player "In this crew, great adventures will never be missing!"
            player "We will have amazing moments with all the other girls!"
            vivi "I have no doubt about that, [player.n]"

            $ vivi_love += 1
            narrador "[vivi.n] love +1"


    return