# Version event: 3
# Version game: 0.23

label vivi_hangout_3:
    vivi "[player.n], I have noticed that the crew sees you as their leader, and I want to make something clear..."
    vivi "You know how much I respect you and that I will be forever grateful to you all..."
    vivi "It's an unpayable debt I have with your group, I will surely figure out how to repay it over time..."
    player "(Hahaha, I'm sure you will!)"
    vivi "But I must always act for the good of my people, and even though I trust you, I must do what I believe is best for Alabasta."
    vivi "I cannot allow anyone else to dictate my decisions, especially if they go against these interests."


    menu:
        "No one here is forcing you to do anything":
            player "No one here is forcing you to do anything, we are a team."
            player "[vivi.n], there are no orders here, we all work together."
            player "You are part of the team, and your decisions will always be respected."
            vivi "That's good to hear... It makes me feel more at home here."
            $ vivi_love += 1
            narrador "[vivi.n] love +1"

        "You will have to get used to following my orders":
            
            player "If you're in my crew, you follow my rules."
            show vivi c1 serious with Dissolve(0.2)
            vivi "I don't know if I like that idea..."
            player "In time, you'll see that it's not a bad thing… I'm sure you'll like it..."
            vivi "We'll see... I'm not entirely comfortable with this conversation..."
            vivi "We'll talk later..."

            $ vivi_love -= 1
            narrador "[vivi.n] love -1"


    return