# Version event: 3
# Version game: 0.1

label event_yamato_give:
        menu:
                "Give her a Bento" if bento_yamato > 0:
                        $ bento_yamato -= 1
                        player "How are you, [yamato.n]? I have a gift for you, I hope you like it..."
                        player "I think it will bring back memories of your hometown!!"
                        show yamato happy with dissolve
                        yamato "You're so thoughtful, Captain! You have such a good memory, you know I love them. Thank you so much!..."

                        $ yamato_love += 4
                        $ yamato_lust += 2
                        narrador "[yamato.n] Love +4 | [yamato.n] Lust +2"

                "Give her a Earrings" if earrings_yamato > 0:
                        $ earrings_yamato -= 1
                        player "How are you, [yamato.n]? I have a gift for you, I hope you like it..."
                        player "I'm sure you'll love it!!"

                        show yamato happy with dissolve
                        yamato "How considerate, Captain! It's a bit unexpected but I like it, and the material it's made of is so fine! Thank you so much!..."
                        $ yamato_love += 2
                        $ yamato_lust += 1
                        narrador "[yamato.n] Love +2 | [yamato.n] Lust +1"

                "Give her a Tangerine" if tangerine_nami > 0:
                        $ tangerine_nami -= 1
                        player "How are you, [yamato.n]? I have a gift for you, I hope you like it..."
                        player "I'm sure you'll love it!!"

                        show yamato with dissolve
                        yamato "Mmm, I guess it's nice... It's a bit unexpected, I might like it, I'm not sure, to be honest!"
                        $ yamato_love -= 1
                        $ yamato_lust -= 1
                        narrador "[yamato.n] Love -1 | [yamato.n] Lust -1"

                "Back":
                        return


        hide yamato with moveoutright
        pause 0.5

        $ game.clock.next()
        jump expression game.location
