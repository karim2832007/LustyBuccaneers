# Version event: 2
# Version game: 0.9

label drum_island_sakura():
    window hide
    show screen screen_black with Dissolve(0.6)
            
    $ game.location = "drum_island_sakura"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto


    $ music_drumisland()
    jump m_drum_island_sakura

label m_drum_island_sakura():
    if DrumIsland.h == 8:

        yamato "There it is! That must be the Sakura tree"

        nami "It's so beautiful!"

        robin "And it seems to be blooming in this cold weather... how incredible!"

        nami "Great, we can pick the [SakuraFlower.n] and leave this island..."

        yamato "Watch out, captain! There's something behind the trees!"

        window hide
        show expression enemy_lapahn.image with Dissolve(1.0):
            xalign 0.5
            yalign 0.5

        pause 0.8
        window auto

        robin "It's a Lapahn, from what the people told us in the village they're not friendly and they're carnivorous animals!"
        yamato "Watch out!!"
        
        call fight_start pass (enemy_pass = enemy_lapahn) from _fight_DrumIsland_h8
        
        hide expression enemy_lapahn.image with Dissolve(0.8)

        if not fight_return:
            jump drum_island_forest

        $ music_drumisland()

        robin "Now we can pick the [SakuraFlower.n]"
        player "We'll take several, they might be useful for something..."

        $ DrumIsland.h = 9
        $ sakuraflower = 4
        narrador "+4 [SakuraFlower.n]"

        $ game.clock.next()
        
    menu:        
        "Back":
            jump drum_island_forest
