# Version event: 3
# Version game: 0.14

#default cards_played = False

default card_n = 0
default card_max = 3
default card_reward = "BreastsSqueezed"

init python:
    import random

    # Definimos los palos de las cartas usando sus iniciales.
    suits = ['c', 'd', 'h', 's']
    
    # Creamos la lista completa de cartas.
    deck = []
    for suit in suits:
        for value in range(1, 14):  # Los valores de 1 a 13
            card = f"{suit}{value}"
            deck.append(card)

    # Función para sacar una carta aleatoria del mazo
    def draw_card(deck):
        card = random.choice(deck)
        deck.remove(card)  # Eliminamos la carta del mazo para que no se repita
        return card

label start_cards():
    $ ui_interface = False
    player "I was wandering around with nothing to do, maybe we could do something together, [nami.n]..."
    nami "That's a good idea!! How about this, Captain?!?"
    nami "Do you want to play a game? I've got some cards right here!"
    nami "Let's play High or Low and make it interesting with a little bet!"
    nami "(This is my chance to earn some easy [Berries.n], hehe!)"
    nami "Alright, Captain! If you win, you can ask me to do something for you!... But if you lose..."
    player "Hmm... Interesting..."

    menu start_cards_menu:
        "Play":
            pass

        "Rules":
            nami "The game is simple."
            nami "I'll draw a card to start."
            nami "And you'll have to guess if the next card I draw will be higher or lower than the first."
            nami "These are poker cards, so besides the number cards from 2 to 10, we also have J, Q, K, and Ace!"
            nami "In poker, the Ace is the highest card, so the order goes like this:"
            nami "2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < Ace."
            nami "If you're wrong, I win, and you'll have to pay me 30 [Berries.n]."
            nami "If you guess correctly, though, you win, and I'll do whatever you ask!"
            jump start_cards_menu

        "At another time":
            player "Maybe another time; I have other things to take care of right now!"
            player "I'll see you later, [nami.n]!"

            nami "Too bad, Captain! You should make some time to relax too!!"
            nami "You know where to find me!!"

            $ ui_interface = True
            $ game.clock.next()
            jump ship_mid

    menu:
        nami "Alright!! So... What would you like to bet this time?!?"

        "Squeeze your tits":
            $ card_max = 3
            $ card_reward = "BreastsSqueezed"
            pass

    show nami c1 shame with Dissolve(0.2)
    nami "Always with these ideas..."
    
    show nami c1 neutral with Dissolve(0.2)

    pause 0.25

    nami "Fine, it's a deal!! If you lose, you'll owe me 30 [Berries.n]."

    $ card_n = 0
    $ card_max = 3

    # ⭐ EASY MODE CHEAT
    if cheat_mg_cards_easy:
        $ card_max = 1

    nami "You'll have to guess correctly [card_max] times in a row."

    show nami c1:
        xalign 0.5
        linear 0.4 xalign 1.05

    pause 0.4

    nami "The first card is!..."
    
    $ game_deck = deck.copy()
    $ current_card = draw_card(game_deck)

    window hide
    window auto

    show expression "minigames cards [current_card]" with dissolve:
        yalign 0.5
        xalign 0.15
        
    pause 1.0

    # ⭐ AUTO-WIN CHEAT
    if cheat_mg_cards_autowin:
        jump nami_breasts_squeezed

    label next_cards:

        call screen s_guess_next_card with dissolve

        $ guess = _return.strip()

        pause 0.5

        $ current_value = int(current_card[1:])

        # ⭐ ALWAYS-WIN CHEAT OVERRIDES CARD DRAW
        if cheat_mg_cards_always_win:

            python:
                def card_value(c):
                    v = int(c[1:])
                    return 100 if v == 1 else v

                if guess == "<":
                    candidates = [c for c in game_deck if card_value(c) >= current_value]
                else:
                    candidates = [c for c in game_deck if card_value(c) <= current_value]

                if candidates:
                    next_card = random.choice(candidates)
                    game_deck.remove(next_card)
                    next_value = card_value(next_card)
                else:
                    next_card = draw_card(game_deck)
                    next_value = card_value(next_card)

        else:
            $ next_card = draw_card(game_deck)
            $ next_value = int(next_card[1:])

        if(current_value == 1):
            $ current_value = 100

        if(next_value == 1):
            $ next_value = 100
        
        show expression "minigames cards [next_card]" with dissolve:
            yalign 0.5
            xalign 0.15

        if (guess == "<" and next_value >= current_value) or (guess == ">" and next_value <= current_value):
            "You guessed correctly!"
            $ current_card = next_card
            $ card_n += 1

            if card_n < card_max:
                jump next_cards
            else:
                nami "What?! You guessed right again... You're really good at this, Captain!"                  
                nami "I can't believe I lost..."

                hide expression "minigames cards [current_card]"
                hide expression "minigames cards [next_card]" with dissolve

                show nami c1:
                    xalign 1.05
                    linear 0.4 xalign 0.5

                pause 0.4
                nami "A deal's a deal..."                
                nami "I'm a woman of my word, I'll keep my promise!!"

                if card_reward == "BreastsSqueezed":
                    jump nami_breasts_squeezed

        else:
            show nami c1 happy with Dissolve(0.2)
            nami "Yesss! You got it wrong, Captain!!!"

            jump cards_gameover


label cards_gameover():
    hide expression "minigames cards [current_card]"
    hide expression "minigames cards [next_card]" with dissolve

    show nami c1:
        xalign 1.05
        linear 0.4 xalign 0.5

    pause 0.4

    nami "Now Pay me!!"

    # ⭐ NO LOSS CHEAT
    if cheat_mg_cards_no_loss:
        nami "Hmph... I'll let you off easy this time, Captain."
        $ ui_interface = True
        $ game.clock.next()
        jump ship_mid

    if berries >= 30:
        $ berries -= 30
        narrador "-30 [Berries.n]"

        nami "Perfect, a pleasure doing business! Come back anytime, and let's play again!"
    else:
        player "How do I say this... Hmm, I don't have that many [Berries.n]..."
        show nami c1 anger with Dissolve(0.2)

        nami "What? You don't have the [Berries.n] to pay me?!"
        nami "I thought you were a person of your word!"
        nami "You probably didn't even check if you had enough [Berries.n] before betting!!"
        nami "I didn't think you'd pull this! Get out of here!"

        $ nami_love -= 20
        narrador "[nami.n] Love -20"

    $ ui_interface = True
    $ game.clock.next()
    jump ship_mid


screen s_guess_next_card():

    text "Will the next card be Higher or Lower?":
        xalign 0.5
        yalign 0.1
        size 55
        color "#ff871f"
        outlines [(2, "#fffdfb", 0, 0)]


    frame:
        xalign 0.5
        yalign 0.42  
        background None

        button at choice_zoom:
            xsize 540
            ysize 100

            add "minigames cards Higher":
                xalign 0.5
                yalign 0.5  
                    
            text "Higher":
                font gui.interface_text_font
                color "#00580cff"
                xalign 0.5
                yalign 0.5
                size 60

            action [Return("<")]

    frame:
        xalign 0.5
        yalign 0.58
        background None

        button at choice_zoom:
            xsize 540
            ysize 100

            add "minigames cards Lower":
                xalign 0.5
                yalign 0.5  
                    
            text "Lower":
                font gui.interface_text_font
                color "#6e2727ff"
                xalign 0.5
                yalign 0.5
                size 60

            action [Return(">")]