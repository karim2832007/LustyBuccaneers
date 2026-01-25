# Version event: 2
# Version game: 0.27

label hancock_give:
    menu:
        "Give her a Chocolate" if chocolate > 0:
            $ chocolate -= 1

            player "How are you, [hancock.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show hancock happy with dissolve
            hancock "How thoughtful, [player.n]! It's a bit unexpected but I like it, Thank you very much!"

            $ hancock_love += 2
            $ hancock_lust += 1
            narrador "[hancock.n] Love +2 | [hancock.n] Lust +1"

        "Give her a Flowers" if flowers > 0:
            $ flowers -= 1
            
            player "How are you, [hancock.n]? I have a gift for you, I hope you like it..."
            player "I think they'll bring back memories of your hometown!!"

            show hancock happy with dissolve
            hancock "Thanks [player.n]! You have such a good memory, you know I love these. Thank you very much!..."

            $ hancock_love += 2

            narrador "[hancock.n] Love +2"

        "Give her a Perfume" if perfume > 0:
            $ perfume -= 1
            
            player "How are you, [hancock.n]? I have a gift for you, I hope you like it..."
            player "I'm sure you'll love it!!"

            show hancock happy with dissolve
            hancock "How thoughtful, [player.n]! I love it, Thank you very much!"

            $ hancock_love += 3
            $ hancock_lust += 2
            narrador "[hancock.n] Love +3 | [hancock.n] Lust +2"

        "Back":
            return 
    
    jump hancock_bye