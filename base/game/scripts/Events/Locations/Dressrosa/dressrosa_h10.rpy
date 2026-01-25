# Version event: 2
# Version game: 0.37

label dressrosa_h10():
    $ ui_interface = False

    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    show events dressrosa h6 h6_gatz
    play ambient "ring" fadein 1.0
    hide screen screen_black with Dissolve(0.3)

    gatz "{size=40}Weeeeeeeeeelcome back, ladies and gentlemen, toys and dolls!{/size}"
    gatz "{size=40}Welcome everyone once again to the Corrida Coliseum!{/size}"
    
    $ game.location = "dr_ac_co_arena"
    show BG locations
    hide events dressrosa h6 h6_gatz with dissolve
    
    gatz "We are here in front of a fierce battle, with two participants who are quickly rising in popularity!"
    pause 0.5
    gatz "With no clear favorite, but a great duel ahead!"
    gatz "On one side, we have a member of the long-arm tribe..."
    gatz "A competitor who has declared he comes with a single objective, the [HanaHanaFruit.n] fruit!!"
    gatz "The fighter known as the 'Destruction Cannon'!!!"
    gatz "Give a warm welcome to..."
    gatz "{size=40}The Destruuuction Caaaaaannon...{/size}"
    gatz "{size=40}[ideo.n]{/size}!!!"

    pause 0.5

    unknown "{size=40}[ideo.n]!! [ideo.n]!! [ideo.n]!!{/size}"

    show expression enemy_ideo.image with Dissolve(0.5):
        xalign 0.5
        yalign 0.5

    pause 0.5

    gatz "And on the other side..."
    gatz "A fighter who has proven not to be a nobody... even though we know little about his past!"
    gatz "Someone who slowly won the hearts of a large part of the crowd..."
    gatz "Through great fights and a heavy punch!"
    gatz "Give a warm welcome to..."
    gatz "{size=40}[player.n]!!!!{/size}"

    pause 0.5
    unknown "{size=40}[player.n]!! [player.n]!! [player.n]!!{/size}"
    pause 0.5

    gatz "What an interesting matchup we have today!"
    gatz "[ideo.n] versus [player.n]!!!"
    gatz "Who will emerge victorious?!?"
    gatz "Let's enjoy the show these fighters are about to give us!"
    pause 0.5

    ideo "So we finally face each other... I've seen your strength in the previous rounds, outsider."
    ideo "Your style is unpredictable, wild... but not without purpose."
    player "Coming from you, that almost sounds like a compliment."
    ideo "Do not be mistaken. I don't respect you... yet. But I recognize power when I see it."
    ideo "The arena does not lie. Only the worthy rise here... and I plan to be the last one standing."
    player "Confidence isn't something you're lacking, huh?"
    ideo "It's not confidence, it's conviction! My fists burn with the fiery will of my clan!"
    ideo "I trained among storms, bled over stone... survived where many fell."
    ideo "And you? Are you ready to stake your life on this dance of strength?"
    player "I didn't come all the way here to back down. Let's see what those fists of yours are made of."
    ideo "Ha! That's what I like!"
    ideo "If you fall, you'll fall with honor... But I don't think you'll get that far."
    ideo "Losing is not in my vocabulary!"
    ideo "Today, I will write a new chapter of legend with every blow I land on you."
    ideo "Let this arena hear our names... and tremble with the echo of this battle!"
    player "Then let's stop talking... and fight!"
    ideo "{size=40}Come! Show me you deserve to be in this tournament!{/size}"



    call fight_start pass (enemy_pass = enemy_ideo, no_run = True, no_interface = True) from _fight_enemy_ideo


    ideo "Heh... damn... I didn't expect you to overpower me like that!"
    ideo "Your blows... carried more than strength. There was purpose..."
    ideo "You fought with your heart... and that deserves respect."
    ideo "Don't forget this battle... because I certainly won't."
    ideo "Keep moving forward... and may your name thunder louder than mine someday..."

    $ _window_hide()
    hide expression enemy_ideo.image with Dissolve(0.8)
    pause 0.5
    
    $ black_to_img("events dressrosa h6 h6_gatz")

    gatz "{size=40}Iiiiiiiiincredibleeeeeee!!!!{/size}"
    gatz "Once again in an amazing showdown, [player.n] rises victorious!!"
    gatz "{size=40}Is there anyone out there who can stop [player.n]??!!!!{/size}"
    gatz "For now, that question seems to have no answer!"
    gatz "But don't rush, the day is still long!"
    gatz "We'll see you again with more fights after the break, see you soon!"


    stop ambient
    $ Dressrosa.h = 11
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
