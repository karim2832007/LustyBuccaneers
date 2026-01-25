# Version event: 2
# Version game: 0.28

label el_church_tunnels2():
    window hide
    show screen screen_black with Dissolve(0.6)

    python:
        if hide_label:
            if renpy.has_label(hide_label):
                renpy.call(hide_label)
            hide_label = None
            
    $ ui_interface = True
    $ game.location = "el_church_tunnels2"
    scene BG locations:
        blur 3
    
    hide screen screen_black with Dissolve(0.3)
    window auto

    #$ ambient_ship()
    $ music_elegia()
    jump m_el_church_tunnels2

label m_el_church_tunnels2():
    if Elegia.h == 13:
        $ ui_interface = False

        player "Now I understand why they were hiding here..."        
        player "This tunnel is so long, it's a damn maze..."
        player "Good thing I brought you with me, [robin.n]!"

        robin "Look over there, [player.n]!"

        window hide
        window auto
        show layer_tot_musica zorder 5 with Dissolve(0.8)  

        pause 1.0
        player "What the hell..."
        player "What the hell is that?!?"
        robin "Interesting..."
        robin "This is really fascinating... It's truly ancient..."
        robin "There's something written here, in a very old language..."
        robin "Luckily I can understand it... I'm familiar with this ancient form of writing!"
        player "It's amazing how nothing surprises me anymore! There's nothing you don't know, [robin.n]..."
        player "You're so sexy when you're in research mode..."

        $ robin_love += 1
        $ robin_lust += 1
        narrador "[robin.n] Love +1 and Lust +1"
        robin "Always flattering me, Captain..."
        player "Hahaha! You know me!... So, what does it say, [robin.n]?"

        robin "I think it should be something like the following:"
        #suspense music
        robin "The fear of all and their downfall."
        robin "The Tot Musica is the symbol of the end."
        robin "Fear it, flee from it."
        robin "What is the Tot Musica?"
        robin "It is a collection of ancient emotions and thoughts."
        robin "Loneliness, suffering—a shadow that haunts people."
        robin "They also call it the Demon King."

        player "Phewww... That doesn't sound good at all..."
        player "Looks like bringing you along was a smart idea..."

        robin "It's really interesting. Maybe we could come back later and study it more thoroughly..."
        robin "This place is pretty well hidden... I doubt they'll find it, and if they do, they'll hardly be able to read what this mural says."
        robin "There is still more information, with time I could make some discoveries."
        player "Sounds good. For now, we have to keep searching for [uta.n]'s vivre card."

        window hide
        window auto
        hide layer_tot_musica with Dissolve(0.8)

        robin "Understood, Captain. Let's move forward."


        window hide
        window auto
        with dissolve

        $ ui_interface = True
        $ Elegia.h = 14

    menu:
        "Continue moving through the tunnel":
            jump el_church_tunnels3

        "Back":
            jump el_church_tunnels
