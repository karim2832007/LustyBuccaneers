# Version event: 3
# Version game: 0.34

label dressrosa_h7():
    $ ui_interface = False

    show rebecca c2 with Dissolve(0.5):
        xalign 0.5
        yalign 1.0

    player "(Yeah, I knew you'd be here... My angel in armor!)"
    player "Hey [rebecca.n]!!! How's everything going!?!"
    show rebecca c2 happy with Dissolve(0.2)
    rebecca "Hi [player.n], I was just here warming up, I'm about to head back into the arena!"
    rebecca "I saw your last fight... You were really amazing!"
    rebecca "[lepanto.n] was a very experienced fighter... Really tough..."
    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "You really surprised me... It was like it didn't take you much effort to defeat him..."

    menu:
        "It was, wasn't it? It really didn't take me much ":
            player "It was, wasn't it? I felt it was easy too..."
            player "It was an easy fight, honestly."

        "It was a tough battle!":
            player "The guy was tough, you could see his experience..."
            player "Maybe it looked easy, but he was a worthy opponent..."
            player "It was an interesting fight."

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"

    rebecca "You were really great, you surprised everyone out there!"
    rebecca "Even [lepanto.n] himself was surprised, I'm sure..."
    player "Thanks, I appreciate the compliment!"
    player "That guy... [lepanto.n]... In the end he told me some rather interesting last words before he fell..."
    rebecca "Oh yeah?!? With the crowd, you couldn't hear much of what you two said..."
    rebecca "What did he say?"
    player "He told me about his past, apparently... obviously closely tied to [Dressrosa.n]..."
    show rebecca c2 serious with Dissolve(0.2)
    rebecca "..."
    player "Apparently the former king died, and he was in his service... Now he serves the current king, but it seems he doesn't do it willingly."
    player "He said he no longer had honor... He'd failed his previous master and now had no hope..."
    player "Supposedly he's protecting a princess... But it was all very strange; he didn't say much."
    player "Do you know anything about all this, [rebecca.n]?"
    rebecca "Mmm..."
    rebecca "No... I don't know... I don't know exactly what you're talking about..."
    pause 0.5
    player "(She doesn't sound very convinced...)"
    rebecca "From what you're saying, it seems [lepanto.n] is still loyal to the former king..."
    rebecca "If he fought in the name of the old king... then he must have been someone with a noble heart."
    rebecca "Although in here, in this coliseum... noble hearts usually end up broken..."
    player "You talk like you know what you're talking about."
    rebecca "Let's say... I've heard many stories about the old kingdom, about what [Dressrosa.n] was like before all this."
    rebecca "Some say the former king was a just man... others that he was deceived."
    rebecca "But no one dares to speak about that out loud. It could cost you more than just a fight in the arena..."
    player "And what do you think?"
    rebecca "I think the truth is buried beneath many lies... and only fools try to unearth it."
    rebecca "You should focus on the tournament. Here, secrets don't help you survive."
    player "Maybe... but sometimes understanding the past helps win the present."
    rebecca "Hmph... maybe you're right... You're really interesting, [player.n]..."


    menu:
        "Well, we've talked plenty about history...":
            player "Well, we've talked plenty about history..."
            player "Maybe we could change the subject..."

        "And about the matter of the princess...":
            player "And about the matter of the princess..."
            player "(I'm sure she must be a beauty too!)"
            show rebecca c2 neutral with Dissolve(0.2)
            rebecca "..."
            rebecca "You ask too many questions... You're very interested in knowing about [Dressrosa.n] and its history, haha"

            $ rebecca_love += 1
            narrador "[rebecca.n] love +1"

            rebecca "But here, names carry weight. Don't ask about royalty out loud without thinking."
            player "Does that woman have some kind of problem?"
            rebecca "... They say she's a dancer with eyes that pierce through lies."
            player "Wow, is she a witch or something?!?..."
            show rebecca c2 happy with Dissolve(0.2)
            rebecca "Hahaha no, no, nothing like that..."
            player "And what's her name?!?"
            pause 0.5
            show rebecca c2 serious with Dissolve(0.2)
            rebecca "Her name is not important.. But don't ask too loudly about her..."
            show rebecca c2 annoyed with Dissolve(0.2)
            rebecca "Apparently she betrayed the former king... Or that's what everyone says..."
            pause 0.5
            show rebecca c2 serious with Dissolve(0.2)
            rebecca "But I don't know... My heart tells me I'm wrong..."
            player "(What does she mean? Do they know each other?)"
            rebecca "Either way, that doesn't change reality..."
            rebecca "Her power is real... so she can see who's asking and why."
            rebecca "She's with the Donquixote family now..."
            rebecca "If anyone were aware of movements in the shadows, it would be someone with her eyes."
            rebecca "Knowing too much in [Dressrosa.n] can turn you into another piece on the board. Or worse..."
            player "Do you know her?"
            rebecca "..."
            rebecca "I've seen her from afar... enough to understand that not everyone chooses where they end up."
            rebecca "If you cross paths with her, respond with sincerity. She hates lies more than swords."
            rebecca "But anyway... That'll be another story..."

    pause 0.5
    show rebecca c2 neutral with Dissolve(0.2)
    rebecca "Maybe another time we can keep talking... it's getting late... But promise me something..."
    player "What is it?"
    rebecca "That if you manage to reach the end... don't forget what you saw in the eyes of those who fall."
    rebecca "Many of them don't fight for glory or gold... but for something they lost long ago."
    rebecca "And not everyone is lucky enough to keep searching."
    player "You speak with great passion, [rebecca.n]. Who do you fight for? You never quite tell me everything..."
    rebecca "...that... maybe I'll tell you when all this is over."
    rebecca "If we're still alive, of course."

    $ _window_hide()
    show rebecca c2 helmet with Dissolve(0.8)

    rebecca "We'll see each other again..."
    rebecca "These fights aren't like the preliminary ones anymore... It should be full of powerful enemies."
    rebecca "I'm off to fight!"
    player "I trust you!"
    rebecca "Thanks... Goodbye [player.n]"
        

    $ Dressrosa.h = 8
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_statue
