# Version event: 2
# Version game: 0.15

default memory_time = 100
default memory_time_range = 100
default memory_reward = "BreastsSqueezed"
default selected_cards = []
default delay_flip_back = False
default memory_win = False

init python:
    import random

    #memory_deck
    card_values = ["m1", "m1", "m2", "m2", "m3", "m3", "m4", "m4", "m5", "m5", "m6", "m6"]


    def shuffle_deck(deck):
        random.shuffle(deck)

    #memory_flip_card
    def flip_card(index):
        global delay_flip_back
        global memory_win

        if board[index]["flipped"] or board[index]["matched"] or delay_flip_back:
            return  # Ignorar si la carta ya está volteada o emparejada
        
        board[index]["flipped"] = True
        selected_cards.append(index)

        # Comprobar si hay dos cartas volteadas
        if len(selected_cards) == 2:
            i1, i2 = selected_cards
            if board[i1]["value"] == board[i2]["value"]:
                board[i1]["matched"] = True
                board[i2]["matched"] = True
                selected_cards.clear()

                if all(card["matched"] for card in board):
                    memory_win = True

            else:
                delay_flip_back = True


    def flip_back():
        global delay_flip_back
        i1, i2 = selected_cards
        board[i1]["flipped"] = False
        board[i2]["flipped"] = False
        selected_cards.clear()
        delay_flip_back = False

    # Cheat-enabled timer handler
    def memory_tick():
        # Auto-win cheat: instantly win
        try:
            if cheat_mg_memory_autowin:
                renpy.store.memory_win = True
                return
        except Exception:
            pass

        # Freeze timer cheat: do not decrement
        try:
            if cheat_mg_memory_freeze:
                return
        except Exception:
            pass

        # Normal countdown
        renpy.store.memory_time -= 0.01

        if renpy.store.memory_time <= 0:
            renpy.jump("memory_gameover")


screen memory_countdown:
    if not memory_win:
        timer 0.01 repeat True action Function(memory_tick) 
    
    frame:
        background None
        xsize 60
        ysize 920
        xalign 0.18
        yalign 0.5
    
        add "minigames memory bar_memory_back":
            yalign 1.0

        if(memory_time < memory_time_range/2):
            if(memory_time < memory_time_range/4):
                image "minigames memory bar_memory_red":
                    yalign 1.0
                    crop (0, 0, 60, int(memory_time*920/memory_time_range))
                    zoom -1
            else:
                image "minigames memory bar_memory_yellow":
                    yalign 1.0
                    crop (0, 0, 60, int(memory_time*920/memory_time_range))
                    zoom -1
        else:
            image "minigames memory bar_memory":
                yalign 1.0
                crop (0, 0, 60, int(memory_time*920/memory_time_range))
                zoom -1


transform flip_card_animation():
    xalign 0.5 yalign 0.5
    xzoom 0.0
    linear 0.2 xzoom 1.0

screen memory_game():
    zorder -20
    modal True

    frame:
        background None
        xalign 0.4
        yalign 0.5

        grid 4 3 spacing 10:
            for i, card in enumerate(board):
                frame:
                    background None
                    xsize 200
                    ysize 300

                    if cheat_mg_memory_reveal or card["flipped"] or card["matched"]:
                        #add card["value"]
                        add "minigames memory " + card["value"] at flip_card_animation()
                    else:
                        add "minigames memory m0" at flip_card_animation()

                        button:
                            focus_mask None
                            action Function(flip_card, i)

    if delay_flip_back:
        timer 1.0 action Function(flip_back)

    # Auto-win hook: ensure the screen reflects the cheat toggle immediately
    if cheat_mg_memory_autowin:
        $ memory_win = True

    if memory_win:
        timer 1.0 action Return()

label start_cards_memory():
    $ ui_interface = False
    player "I was wandering around with nothing to do, maybe we could do something together, [robin.n]..."
    player "You know, kill some time, have some fun together... You can take a break from your reading..."
    robin "That's a good idea!! How about this, Captain?!?"
    robin "Do you want to play a game? I've got some cards right here!"
    robin "Let's see how sharp your memory is, I hope you'll surprise me!"
    robin "(This is my chance to take advantaje, hehe!)"
    robin "Alright, Captain! If you win, you can ask me to do something for you!... But if you lose, you'll have to pay me!"
    player "Hmm... Interesting... Fine for me!"

    menu start_cards_memory_menu:
        "Play":
            pass

        "Rules":
            robin "Alright, here are the rules..."
            robin "This is a simple memory game..."
            robin "Tap a card to flip it and reveal its image."
            robin "Then, tap another card."
            robin "If the images match, the cards will remain uncovered."
            robin "If they don't match, both will flip back over."
            robin "Your goal is to find all the pairs."
            robin "But you'll have to do this before time runs out."
            robin "If you run out of time and don't have all the cards uncovered, you'll have to pay me 30 [Berries.n]."

            jump start_cards_memory_menu

        "At another time":
            player "Maybe another time, I have other things to take care of right now!"
            player "I'll see you later, [robin.n]!"

            robin "Too bad, Captain! You should make some time to relax too!!"
            robin "You know where to find me!!"

            $ ui_interface = True
            $ game.clock.next()
            jump ship_mid

    menu:
        robin "Alright!! So... What would you like to bet this time?!?"

        "Squeeze your tits":
            $ memory_time = 25
            $ memory_time_range = 25
            $ memory_reward = "BreastsSqueezed"

    show robin c1 shame with Dissolve(0.2)
    robin "Always with these ideas..."
    show robin c1 neutral with Dissolve(0.2)

    pause 0.25

    # START

    show robin c1:
        xalign 0.5
        linear 0.4 xalign 1.05

    pause 0.4

    robin "Let's start!!"

    window hide
    window auto

    $ shuffle_deck(card_values)
    $ selected_cards = []
    $ board = [{"value": value, "flipped": False, "matched": False} for value in card_values]
    $ delay_flip_back = False
    $ memory_win = False

    show screen memory_countdown
    call screen memory_game with Dissolve(0.8)
    hide screen memory_countdown

    show robin c1:
        xalign 1.05
        linear 0.4 xalign 0.5

    pause 0.4

    robin "Congratulations! You found all the pairs, you have surprised me!"
    robin "I'll keep my part of the deal!"

    if memory_reward == "BreastsSqueezed":
        jump robin_breasts_squeezed

    jump robin_breasts_squeezed


label memory_gameover():
    show robin c1:
        xalign 1.05
        linear 0.4 xalign 0.5

    pause 0.4

    robin "Time's up, Captain!!!"
    robin "You lost!"
    robin "Now Pay me!!"

    # No-loss cheat: skip penalty and return to ship_mid
    if cheat_mg_memory_no_loss:
        robin "Hmph... I'll let you off easy this time, Captain."
        $ ui_interface = True
        $ game.clock.next()
        jump ship_mid

    if berries >= 30:
        $ berries -= 30
        narrador "-30 [Berries.n]"

        robin "You need to practice your memory more, Captain! Let's play again later."
    else:
        player "How do I say this... Hmm, I don't have that many [Berries.n]..."
        show robin c1 anger with Dissolve(0.2)

        player "I'm sorry, but I just realized I don't have [Berries.n]..."
        robin "What?! You don't have [Berries.n] to pay me?!"
        robin "It's very irresponsible of you to bet with me without having a way to pay!"
        robin "Leave right now, I'm very disappointed and angry with you, Captain!"

        $ robin_love -= 20
        narrador "[robin.n] Love -20"

    $ ui_interface = True
    $ game.clock.next()
    jump ship_mid