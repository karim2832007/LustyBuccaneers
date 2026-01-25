# Version event: 2
# Version game: 0.35

label dressrosa_h8():
    $ ui_interface = False

    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    show events dressrosa h6 h6_gatz
    play ambient "ring" fadein 1.0
    hide screen screen_black with Dissolve(0.3)

    gatz "{size=40}Weeeeeeeeeelcome back, ladies and gentlemen, toys and dolls!{/size}"
    gatz "{size=40}Welcome everyone once again to the Corrida Coliseum!{/size}"
    gatz "After the battle arena has been reset following the last matches, we return to our regular schedule..."
    
    $ game.location = "dr_ac_co_arena"
    show BG locations
    hide events dressrosa h6 h6_gatz with dissolve
    
    gatz "This time, two great fighters will face off..."
    pause 0.5
    gatz "On one side, a martial artist from the Longleg Tribe..."
    gatz "A fierce warrior who has shown his incredible strength in previous battles..."
    gatz "And who many consider one of the top contenders to reach the grand final!!"
    gatz "Without further ado..."
    gatz "Give a big round of applause to the favorite of this match..."
    gatz "{size=40}[gilly.n]{/size}!!!"

    show expression enemy_gilly.image with Dissolve(0.5):
        xalign 0.5
        yalign 0.5

    pause 0.5

    # change
    gatz "And on the other side, a young unknown who made quite an impression in his last fight!"
    gatz "Whispered among the crowd as a rising star of the tournament..."
    gatz "The one who defeated the current Captain of the [Dressrosa.n] army..."
    gatz "Give a warm welcome to....."
    gatz "{size=40}[player.n]!!!!{/size}"
    pause 0.5
    gatz "What an incredible atmosphere we have today..."
    gatz "[gilly.n] versus [player.n]!!!"
    gatz "Who will emerge victorious?!?"
    gatz "Let's enjoy the show these fighters are about to give us!"
    pause 0.5

    gilly "Let's see what you've got, kid..."
    gilly "I promise I won't kick you too hard..."
    player "Heh... We'll see about that!"

    call fight_start pass (enemy_pass = enemy_gilly, no_run = True, no_interface = True) from _fight_enemy_gilly


    gilly "Heh... Incredible, I underestimated you..."
    gilly "You're... really strong..."

    $ _window_hide()
    hide expression enemy_gilly.image with Dissolve(0.8)
    pause 0.5
    
    $ black_to_img("events dressrosa h6 h6_gatz")

    gatz "{size=40}Iiiiiiiiincredibleeeeeee!!!!{/size}"
    gatz "{size=40}[player.n] has done it again!!!!!!!{/size}"
    gatz "Against all odds, once more..."
    gatz "{size=40}[player.n] wins!!{/size}"
    gatz "{size=40}Is there anyone out there who can stop [player.n]??!!!!{/size}"
    gatz "Give him a big round of applause as he leaves the arena! And get ready..."
    gatz "We'll be back shortly with the next matches... Stay tuned!!"

    stop ambient
    $ Dressrosa.h = 9
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
