# Version event: 2
# Version game: 0.32

label dressrosa_h3():
    # dr_ac_co_reception
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "dr_ac_co_reception"
    scene BG locations:
        blur 3
    
    show rebecca c2 at center

    hide screen screen_black with Dissolve(0.3)
    window auto

    pause 1.0

    unknown "Ahh, it's you again..."
    unknown "You know what the public thinks of you... and even so you insist on signing up..."  
    unknown "Truth is, you're in luck—there are two spots left..."
    unknown "Do you want to enter the tournament with a nickname?... Either way, everyone knows who you are..."

    call set_name_rebecca from _call_set_name_rebecca

    rebecca "No, register me under my name, [rebecca.n]"
    player "(Wow... [rebecca.n]... She's like an angel in her battle armor!!)"
    player "(A very revealing armor!!! Now I get why they say the women are fire here!!)"
    player "(Is she really planning to take part in the tournament!?!)"
    player "(I wouldn't mind getting beaten up by a woman like that...)"
    unknown "I don't know what you plan to do here... but you're going to have a bad time... you know that already..."
    rebecca "..." 
    show rebecca c2 at x_move(x_start=0.5, x_end=0.1, dur=0.3)

    rebecca "Doesn't matter... I'm leaving..."
    player "(Wait, don't go!!!)"
    show rebecca c2 at x_move(x_start=0.1, x_end=-1.0, dur=0.5)

    unknown "Next..."
    player "(Damn, she left too fast!! And I can't leave without registering...)"
    unknown "Hey, are you there?!?... If not, I'll let the next one through!"
    player "Yes! Sorry, sorry!! I'm here, I'm here!"
    player "She and I will sign up for the tournament!"
    
    show yamato with dissolve:  
        xalign 0.20  
        yalign 1.0  

    yamato "That's right!!! And we're going to win it!!"
    unknown "Mmm... I'm sorry to inform you there's only one spot left, only one of you two will be able to participate!"
    player "What!?! Are you serious?!... Isn't it possible to add more people?"
    unknown "Unfortunately, the family's rules are very strict... Spots are limited..."
    show yamato annoyed with Dissolve(0.2)       
    yamato "Incredible!! How could we have arrived so late!!"
    yamato "Don't worry, [player.n]... you sign up, I'm sure you won't let us down!"
    player "It's a shame, [yamato.n], but don't worry, I'll get that fruit!"
    unknown "Alright, then it'll be you... How should I register you?"
    player "[player.n]"
    player "I won't use a nickname, I'm not hiding from anyone haha!!"
    unknown "Alright... It'll be [player.n] then, please enter alone and get ready, good luck!"
    player "Well, it's time to go in then..."
    player "(I'll go look for [rebecca.n] hehe! Who knows, maybe I'll manage to impress her)"

    #gunshots future
    player "Mmm!?!?!"
    player "What are those gunshots!!"
    
    $ _window_hide()
    hide yamato with dissolve    
    
    pause 1.0
    $ Dressrosa.h = 4
    jump dr_ac_colosseum
