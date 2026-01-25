# Version event: 3
# Version game: 0.11

label event_amazonlily_hancockcrew:
    window hide
    window auto
    $ ui_interface = False

    show screen screen_black with Dissolve(0.6)

    $ game.location = "none"
    scene BG amazonlily amazon_lily_ring_top

    play ambient "ring" fadein 1.0
    
    hide screen screen_black with Dissolve(0.3)
    
    pause 2.5

    $ game.location = "amazon_lily_ring"
    scene BG locations with Dissolve(0.6):
        blur 3
    
    player "(Wow, she wasn't lying when she said there are only women on this island...)"
    player "(There are so many of them... and many are really beautiful!!, maybe I should think about taking two or three more with me...)"
    hancock "Very well, let the fights begin..."
    hancock "Today, this man will be tested in 3 battles to prove his courage and manhood..."
    hancock "I don't recall any man leaving this ring alive..."
    hancock "Many have been food for my beloved pet, and for your first battle, pirate..."
    hancock "I want you to bring Bacura!!"
    hancock "Fight as hard as you can, we'll watch until the end without intervening..."

    window hide
    show expression enemy_bacura.image with Dissolve(1.0):
        xalign 0.5
        yalign 0.5

    pause 0.8
    window auto

    hancock "This black panther is called Bacura, it's a carnivorous beast that has served as an executioner for the empresses of this kingdom for many generations!"
    hancock "It has a habit of not leaving even a bone when it's done!!"
    hancock "I hope you're really prepared!"

    call fight_start pass (enemy_pass = enemy_bacura, event_gameover = "hancockcrew_end") from _fight_AmazonLily_Ring_Fight_1
    
    if not fight_return:
        jump hancockcrew_run

    hide expression enemy_bacura.image with Dissolve(0.8)

    #$ music_amazonlily()

    unknown "It's incredible, that guy defeated Bacura... He's really strong..."
    unknown "Usually men don't defeat Bacura..."
    hancock "Quite impressive... If you were a fourth-rate pirate..."
    hancock "But I always knew you'd win... Let's raise the difficulty a bit..."
    hancock "Bring [marguerite.n] now..."

    window hide
    window auto

    show expression enemy_marguerite.image with Dissolve(1.0):
        xalign 0.5
        yalign 0.5

    pause 0.5

    player "(She turned her to stone and now she's making her fight... Her reputation as the Kuja Empress is well deserved!)"
    hancock "It's your chance to redeem yourself, [marguerite.n]... Don't disappoint me..."
    marguerite "I will, my Empress!"
    marguerite "I have nothing against you, man, but I won't go easy on you..."
    marguerite "I will defeat you to regain the respect of my Empress, [hancock.n]!!"
    unknown "That's right, Captain!!"
    unknown "Defeat this man!! Have no mercy!..."
    unknown "It'll be easy for you!! We know you'll win!!"
    player "I don't have anything against you either... But I have to defeat you, there's too much at stake... Get ready!"

    call fight_start pass (enemy_pass = enemy_marguerite, event_gameover = "hancockcrew_end") from _fight_AmazonLily_Ring_Fight_2
    
    if not fight_return:
        jump hancockcrew_run

    hide expression enemy_marguerite.image with Dissolve(0.8)

    #$ music_amazonlily()
    unknown "..."
    unknown "It's impossible!! He must have cheated!!"
    player "(These women... They're pushing my patience...)"
    hancock "Enough!!!"
    hancock "[marguerite.n] was simply weak... She underestimated her opponent and didn't rise to the challenge..."
    hancock "It's still quite impressive though..."
    hancock "But the first two battles are nothing compared to your next fight!"
    hancock "Finish him off, Sister!"

    window hide
    window auto

    show expression enemy_marigold.image with Dissolve(1.0):
        xalign 0.5
        yalign 0.5

    pause 0.5
    
    call set_name_marigold from _call_set_name_marigold

    pause 0.5

    narrador "The crowd's shouts echoed loudly"
    unknown "Kill him! Kill him! Kill him!" # maybe something like "Ma-ta-lo!" // #in English it doesn't quite fit
    player "Alright, I just need to beat you now, right?"
    unknown "..."
    unknown "Ahahah! Did you just hear what that man said?!?"
    unknown "How funny, does he really think he can take on one of the Gorgon Sisters!!!"
    unknown "Finish him! You've got this, [marigold.n]!"
    player "(They're really underestimating me!!)"
    hancock "Now, let the fight begin!!"
    marigold "Sorry, it's nothing personal!"

    call fight_start pass (enemy_pass = enemy_marigold, event_gameover = "hancockcrew_end") from _fight_AmazonLily_Ring_Fight_3

    if not fight_return:
        jump hancockcrew_run

    #$ music_amazonlily()

    hancock "Surprising..."

    hancock "([player.n] is really strong... But it's not over yet!)"

    hancock "[marigold.n] I thought I ordered you to fight that man, not to play with him..."

    marigold "But, sister, he helped us..."

    hancock "I refuse to tolerate this any longer!!! Go all out against him, don't underestimate him!"

    marigold "Forgive me, sister! I'll finish him off right now!"

    window hide
    window auto

    hide expression enemy_marigold.image

    show expression enemy_marigold_v2.image:
        xalign 0.5
        yalign 0.5
    
    with flash

    pause 1.0

    player "(A cobra woman?... Is this real?!?... Another devil fruit...)"

    player "(It seems like everyone here has different kinds of powers!)"

    call fight_start pass (enemy_pass = enemy_marigold_v2, event_gameover = "hancockcrew_end") from _fight_AmazonLily_Ring_Fight_4

    if not fight_return:
        jump hancockcrew_run


    hide expression enemy_marigold_v2.image with Dissolve(0.8)

    # intro Haki

    narrador "The coliseum fell silent for a moment as [player.n] stood, breathing heavily after his victory over [marigold.n]. But the calm didn't last long..."

    #$ music_amazonlily()

    narrador "From the stands, the Kuja warriors' shouts began to rise, filled with discontent and disdain."

    unknown "He's nothing but an insignificant man!!!"

    unknown "He just got lucky!! He's not worthy of stepping into our arena!"

    narrador "The shouts quickly multiplied. The Kuja crowd couldn't accept that a man had defeated one of their own, let alone one of the Gorgon sisters. Their eyes were filled with hate and contempt."

    unknown "You're not worthy of being here!"

    unknown "Get off our island, you monkey!"

    player "That's enough! I've had it with this!!"

    narrador "Despite his demand to silence the proud Kuja, they were not willing to accept his victory and continued their aggression, even more fiercely!"

    unknown "That barbarian thinks he can yell at us!!"

    unknown "What a violent animal!!"

    unknown "He shouldn't be allowed to live!!"

    
    player "{size=+16}I said shut up!!{/size}"

    window hide
    # sound haki
    with flashaki
    window auto

    stop ambient fadeout 2.0

    narrador "In that instant, the air in the coliseum changed. An invisible pressure fell upon the Kuja warriors, making them stagger heavily."

    narrador "One by one, several warriors began to faint, unable to withstand the overwhelming presence."

    narrador "Silence took over the place. The weaker warriors collapsed to the ground, unconscious, while the stronger ones barely managed to stay on their feet."

    unknown "What was that? It's impossible..."

    unknown "That Haki... what was that?!?"

    marigold "(I've never seen anyone else with that haki except for [hancock.n])"

    hancock "(It can't be!! He's like me!)"

    hancock "You... You have that... Only a few chosen ones are born with that strength... Maybe... Maybe you are worthy after all..."

    player "Seems like now you're actually listening to me..."

    marigold "(He doesn't seem to realize he used Conqueror's Haki...)"

    hancock "The fight is over, everyone must leave the arena immediately!!"

    hancock "Come, [player.n], let's return to the palace, we need to talk!"

    window hide
    window auto

    show screen screen_black with Dissolve(0.6)

    $ game.location = "al_palace_room"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)

    show hancock with dissolve
    player "Well? What do you say now... I have no problem doing this all day!"

    hancock "You've proven that you are not a weak man..."

    hancock "I'm quite impressed with your performance, to be honest..."
    #cara sonrojada
    hancock "You're... You're really something special..."

    player "I told you that you'd end up accepting!"
    show hancock happy with Dissolve(0.2)
    hancock "Haha, I still haven't said yes yet!"

    hancock "You're really interesting!!"

    hancock "For now, I'll keep my word and join your crew..."
    #cara sonrojada
    hancock "I think I might be interested in your adventure... It might even be fun..."

    

    #WIN
    $ AmazonLily.h = 3
    $ hancock_crew = True
    $ ui_interface = True

    jump al_palace_room



label hancockcrew_end:

    show screen screen_basic_black with Dissolve(0.6)

    stop ambient fadeout 2.0
    stop music fadeout 2.0

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None

    narrador "You passed out and your crew took you out of the arena."

    narrador "When you open your eyes, you see that you're lying in your cabin."

    narrador "You feel very weak."

    player "(I should eat something to regain my strength)"

    $ player_hp = 1

    $ hide_label = "hancockcrew_end_hide"
    jump sleep


label hancockcrew_end_hide():
    hide screen screen_basic_black
    return

label hancockcrew_run:

    narrador "By surrendering, the confrontation was canceled."

    jump al_palace_room