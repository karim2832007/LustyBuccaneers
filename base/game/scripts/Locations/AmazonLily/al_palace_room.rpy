# Version event: 2
# Version game: 0.11

label al_palace_room():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True        
    $ game.location = "al_palace_room"
    scene BG locations:
        blur 3

    if not hancock_crew and not game.clock.night:
        show hancock at center
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    $ music_amazonlily()
    
    jump m_al_palace_room

label m_al_palace_room():
    if AmazonLily.h == 1 or AmazonLily.h == 2:
        menu:
            "Try to join her to the crew" if not game.clock.night:
                #narrador "This event is available in version 0.11.\n{size=+12}{a=https://www.patreon.com/LustyBuccaneers}> Download <{/a}{/size}"
                #jump m_al_palace_room
                if AmazonLily.h == 1:

                    player "[hancock.n] after spending these days with you, I've made a decision..."
                    player "You're really strong and brave... You have experience on the seas and in leading people..."
                    player "(And you have an amazing figure, beautiful breasts, and a gorgeous ass!!!)"
                    player "I want you to join my pirate crew!!!"

                    hancock "What?!?... I didn't expect you'd come with such a request..."
                    hancock "Do you know who I am, right?!? I am the empress of this island... Do you think I can just leave like that?"
                    player "You've already done so much for them, they couldn't be better organized..."
                    player "I'm sure they can handle themselves, that's not a problem..."
                    player "I have big plans in mind!!, but for that, I need an excellent crew..."
                    player "I've already decided, you can't be missing!"
                    show hancock happy with Dissolve(0.2)
                    hancock "Hahaha!! I'm not going to say I dislike your attitude... And I know I'm indebted to you for saving my sister..."
                    show hancock neutral with Dissolve(0.2)                    
                    hancock "But I'm not sure..."
                    hancock "I would never follow a weak man!!"
                    player "Lucky for me! Because I am really strong!"
                    show hancock happy with Dissolve(0.2)
                    hancock "Hahaha!! You'll have to prove it!"
                    show hancock neutral with Dissolve(0.2) 
                    hancock "How about this... If you think you're strong enough, I'll give you the chance..."
                    hancock "Fight and win 3 battles in the city's arena!"
                    hancock "If you manage to prove to me and all the amazons that you're truly strong, I'll consider joining your crew"
                    show hancock happy with Dissolve(0.2)                    
                    hancock "Ha ha ha but don't expect to win easily, they are highly trained amazons!!"
                    player "Alright, I'll prove my strength and earn your respect!!"
                    player "(You'll be mine [hancock.n]!)"

                    $ AmazonLily.h = 2

                if Strength < 15:
                    player "(I haven't trained much lately, I should spend some time in the ship's training room before fighting...)"
                    player "(I need to be well prepared if there are going to be 3 fights, it's best to come up with an excuse for now...)"
                    player "(Or it'll be really hard to win right now...)"
                    narrador "Recommended to have strength above 15. You currently have [Strength]."

                if food < 5:
                    player "(I have very little food in reserve, I think it would be ideal to have at least 5 or 6 rations in case I need to recharge my energy in the middle of the fights.)"

                menu:
                    hancock "Are you ready for the fights?"
                    "Yes":
                        hancock "Good!!!, to the arena!"
                        jump event_amazonlily_hancockcrew

                    "No":
                        hancock "I suppose you're not prepared enough, come back when you're ready!"
                        jump m_al_palace_room
                
            "Back":
                jump amazon_lily_palace
    else:
        menu:        
            "Back":
                jump amazon_lily_palace