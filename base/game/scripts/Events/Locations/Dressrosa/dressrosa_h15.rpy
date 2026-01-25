# Version event: 2
# Version game: 0.39

label dressrosa_h15():
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
    
    gatz "The excitement is at its peak as we bring you the final round of today's tournament!"
    gatz "This match will decide who earns the right to challenge the Hero of the Colosseum, {size=40}{outlinecolor=#8b0000}{color=#ff6666}Diamanteeeeeeee{/color}{/outlinecolor}!{/size}, in the grand finals!"
    gatz "And of course, they're fighting for the ultimate prize: the legendary the [HanaHanaFruit.n] fruit!!"
    pause 0.5
    gatz "In this corner, we have a warrior whose name strikes fear and awe!"
    gatz "He is the former leader of the Happo Navy, a living legend from Kano Country!"
    gatz "A man once known as {outlinecolor=[chinjao.color]}{color=#61f59a}'Chinjao the Drill'{/color}{/outlinecolor} - with a bounty of over 500 million berries on his head!"
    gatz "Yes, folks, it's the one and only DON {size=40}[chinjao.n]{/size}!!!"
    pause 0.5
    unknown "{size=40}[chinjao.n]!! [chinjao.n]!! [chinjao.n]!!{/size}"

    show expression enemy_chinjao.image with Dissolve(0.5):
        xalign 0.5
        yalign 0.5

    gatz "Listen to that roar from the crowd! They remember his glory days!"
    gatz "And in the opposite corner, a rising star who has taken this tournament by storm!"
    gatz "This young contender came out of nowhere and defeated veteran gladiators one after another!"
    gatz "He has shown incredible strength, winning the hearts of the audience along the way!"
    gatz "Now he stands just one fight away from the championship round!"
    gatz "Give it up for our dark horse contender... {size=40}[player.n]{/size}!!!"
    pause 0.5
    unknown "{size=40}[player.n]!! [player.n]!! [player.n]!!{/size}"

    gatz "The crowd is on their feet for this newcomer!"
    gatz "Both fighters look ready to clash with everything they've got!"
    gatz "I can feel the tension from up here - this will be one for the history books!"
    gatz "Only one can move on to face Diamante and seize the [HanaHanaFruit.n] fruit!!"
    gatz "Who will it be? The veteran legend or the fearless upstart?!"
    gatz "Gladiators... FIGHT!!"

    pause 0.5

    chinjao "Before we begin... I have something to say!"
    chinjao "This tournament is a sham! Something foul is going on behind the scenes!"
    pause 0.5
    player "!!!"
    pause 0.5
    chinjao "My grandsons, Boo and Sai, fought here earlier today."
    chinjao "They were injured and taken away to treat their wounds... but they never returned!"
    chinjao "What have you people done with them?! I demand to know!"
    player "Your grandsons? I... I don't know anything about that."
    chinjao "Don't lie to me! You're part of this, whether you know it or not!"
    player "Me?!? Hahah I'm only here to fight for the prize. I'm not involved in whatever happened to them."
    chinjao "Grr... If those bastards running this event hurt my family, I swear they'll pay!"
    chinjao "I won't rest until I get Boo and Sai back!"
    player "I'm sorry about Boo and Sai. I'd be angry too if I were in your place."
    player "But right now, I'm your opponent. If you want answers, you'll have to go through me first."
    chinjao "Hmph, you cocky brat. Fine. I'll go through you!"
    chinjao "Don't think for a second that I'm some weak old man!"
    chinjao "I once had a drill for a head that could split an entire ice continent in two!"
    player "A... drill on your head?"
    chinjao "That's right! I was [chinjao.n] the Drill!"
    chinjao "Until a legendary Marine hero smashed it flat with a single punch!"
    player "I guess he was a strong guy..."
    chinjao "That accursed geezer flattened my head and took away my power!"
    chinjao "All the treasure I had beneath the ice... gone, because I couldn't crack it open anymore!"
    chinjao "For decades, I carried that shame and hatred!"
    chinjao "I won't be made a fool of again!"
    chinjao "First that geezer took my power... and now this colosseum thinks it can take my own flesh and blood!"
    chinjao "I will tear this place apart if I have to!"
    pause 0.5
    chinjao "Show me your strength, kid! Prove that you're worth my time!"
    player "You'll see soon enough!"


    call fight_start pass (enemy_pass = enemy_chinjao, no_run = True, no_interface = True) from _fight_enemy_chinjao


    chinjao "Heh... I'll be damned. I never thought you'd overpower me like that!"
    chinjao "Your blows... they carried more than just brute strength. I felt the conviction behind each strike."
    chinjao "You fought with all your heart... and you've earned this old man's respect."
    chinjao "Keep moving forward... and may your name thunder even louder than mine someday..."
    chinjao "Now... at least I can go see my nephews Boo and Sai in the hospital."


    $ _window_hide()
    hide expression enemy_chinjao.image with Dissolve(0.8)
    pause 0.5
    
    $ black_to_img("events dressrosa h6 h6_gatz")

    gatz "DON [chinjao.n] IS DOWN!!"
    gatz "We have a winner! The match goes to... {size=40}[player.n]{/size}!!!"
    gatz "He started this tournament as a nobody, but has taken down opponent after opponent!"
    pause 0.5
    unknown "{size=40}[player.n]!! [player.n]!! [player.n]!!{/size}"

    gatz "With each victory, he's proven his strength and won the hearts of the audience!"
    gatz "Now he's just one step away from claiming the grand prize!"
    gatz "But that final step is a battle against none other than the Hero of the Colosseum himself - Diamante!"
    gatz "The championship match will take place after a short recess!"
    gatz "So don't go anywhere, folks - the grand finale is coming up next!"

    stop ambient
    $ Dressrosa.h = 16
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
