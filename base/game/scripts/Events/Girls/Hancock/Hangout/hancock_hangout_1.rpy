# Version event: 2
# Version game: 0.12

label hancock_hangout_1:
    player "How about you tell me something from your past, [hancock.n], something significant that shaped you..."
    player "I like to know the past or stories of the people I'm traveling with..."
    show hancock serious with Dissolve(0.2)
    hancock "Well, [player.n], I don't like talking about my past, to be honest..." 
    hancock "Everyone always talks about the Kuja's hatred for men..."
    hancock "And much of it has to do with what my sisters and I went through in the past..."
    
    if hancock_love >= 20:
        show hancock c1 neutral with dissolve 
        hancock "With you, though... I don't know why, but it's always different..."
        hancock "Even though I don't usually share this, especially with men, it's different with you..." 
        hancock "There's something that always makes me want to open up to you..."
        hancock "It's quite strange, I don't know what it is, but it makes me want to tell you..."
        hancock "When I was 12, my sisters and I were enslaved by the World Nobles in the Holy Land of Mary Geoise..."
        hancock "That cursed land is a hell... I assure you, the worst crimes in the world happen there..." 
        hancock "In that place, that's supposed to be a paradise in the world..."
        hancock "Fortunately, a few years ago, there was an attack on the city, and many of us slaves managed to escape..."
        hancock "Since then, I vowed never to be controlled by anyone ever again..." 
        hancock "I will never allow men like the ones from Mary Geoise to lay a finger on me or have control over me again..."
        show hancock c1 annoyed with dissolve
        hancock "I will have my revenge someday..."

        menu:
            "You will have revenge, no one messes with my girls":
                show hancock c1 neutral with dissolve
                player "I can't imagine how hard that must have been..."
                player "Rest assured, you'll get your revenge on the World Government..."
                player "No one messes with my girls!"
                show hancock c1 shame with dissolve
                hancock "I'm surprised you say that, [player.n]..."
                hancock "It feels nice to be protected and supported every once in a while!"
                show hancock c1 neutral with dissolve
                hancock "I hope to have your help in the future."
                $ hancock_love += 1
                $ hancock_lust += 1
                narrador "[hancock.n] lust and love +1"

            "The entire crew will help you settle this debt...":
                show hancock c1 neutral with dissolve
                player "I can't imagine how hard that must have been..."
                player "Rest assured, you'll get your revenge on the World Government..."
                player "You can count on the entire crew for this!"
                hancock "It's good to know I have the group for a possible confrontation..."
                hancock "I hope to have everyone's help in the future!"

                $ hancock_love += 1
                narrador "[hancock.n] love +1"

    else:
        narrador "Requires [hancock.n] love greater than 20."
        show hancock c1 neutral with dissolve
        hancock "But I don't feel comfortable talking about that..."

        menu:
            "You can tell me, I'm your captain after all...":
                player "You can tell me, I'm your captain after all"
                hancock "That's something private to me"
                hancock "I don't feel comfortable having this conversation"
                hancock "I'd better go, we'll talk later..."

                $ hancock_love -= 1
                narrador "[hancock.n] love -1"

            "If you ever feel like talking about it, you know where to find me":
                player "If you ever feel like talking about it, you know where to find me"
                show hancock c1 neutral with dissolve
                hancock "Thank you [player.n], I knew you would understand..."
                hancock "It's not that I don't trust you, but right now I just don't feel ready to talk about it..."
                hancock "Maybe another day I can tell you"
                player "Whenever you feel comfortable, you'll tell me. See you next time!"

                $ hancock_love += 1
                narrador "[hancock.n] love +1"

    return