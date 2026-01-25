# Version event: 3
# Version game: 0.34

label dressrosa_h6():
    $ ui_interface = False

    $ _window_hide()
    show screen screen_black with Dissolve(0.6)
    show events dressrosa h6 h6_arena
    play ambient "ring" fadein 1.0
    hide screen screen_black with Dissolve(0.3)


    gatz "{size=40}Weeeeeeeeeelcome, ladies and gentlemen, toys and dolls!{/size}"
    gatz "{size=40}Welcome everyone to the Corrida Coliseum!{/size}"

    $ black_to_img("events dressrosa h6 h6_gatz")

    gatz "Thanks to the great kindness and benevolence of our young king..."
    gatz "Today we are all gathered here to enjoy a one-of-a-kind event in history!!"
    gatz "{size=40}What you will see today will be the event of the century!!!{/size}"
    gatz "Fighters from all the seas have gathered today with a single goal..."
    gatz "To emerge victorious from today's grand tournament and take home a unique, unmatched prize!!"
    pause 0.5
    gatz "I am [gatz.n], and I'll be your commentator and host for this tournament!!"
    pause 0.5
    gatz "With the qualifying matches concluded, only the best fighters remain..."
    gatz "These contenders will face off in 1 vs 1 battles until only one winner is left, who will then face the one and only..."
    gatz "The historic champion of the Coliseum, the hero of the Corrida Coliseum, and the great champion of the Donquixote family..."
    gatz "{size=40}{outlinecolor=#8b0000}{color=#ff6666}Diamanteeeeeeee{/color}{/outlinecolor}!{/size}"
    pause 0.5
    gatz "As you already know, the king entrusted us with an invaluable treasure..."
    gatz "Which will be awarded today to whoever wins this tournament."
    gatz "Today it is here, before you, in its original form..."
    gatz "The Devil Fruit... {outlinecolor=#a85d74}{color=#ffc0cb}Hana Hana Fruit!{/color}{/outlinecolor}!"
    gatz "Observe..."

    $ black_to_img("events dressrosa h6 h6_hanahana")

    pause 1.0

    gatz "Isn't it wonderful!?!"
    gatz "{size=40}First place in the tournament will receive the fruit as the prize!!{/size}"

    $ game.location = "dr_ac_co_arena"
    $ black_to_img("BG locations", hide="events dressrosa h6 h6_hanahana")

    pause 0.5

    gatz "Without further ado, let's go to the first matchup of the day!!"
    gatz "On one side we have a tough, veteran contender... known to all the locals on the island..."
    gatz "The captain of the Dressrosa army"
    gatz "Captain Tank [lepanto.n]!!!!"

    show expression enemy_lepanto.image with Dissolve(0.5):
        xalign 0.5
        yalign 0.5

    pause 0.5

    gatz "And on the other side... a young complete unknown, but we shouldn't underestimate him if he's here!"
    gatz "The last person to register for this wonderful tournament—give a big round of applause to..."
    gatz "{size=40}[player.n]!!!!{/size}"
    pause 0.5
    gatz "[lepanto.n] versus [player.n]!!!"
    gatz "Who will be the winner?!? The bets seem to have a clear favorite... but don't count the kid out yet!"
    pause 0.5
    gatz "!!?!"
    gatz "It seems both fighters are striking up a chat before the bout..."
    gatz "What could they be saying? It's hard to hear with how lively today's crowd is!!"

    lepanto "What is a youngster like you doing here!?!"
    player "Well, I came to enter the tournament, big guy..."
    lepanto "You?!?!... You should train many more years before coming to participate in this tournament..."
    lepanto "Don't you know how dangerous it is!?!"
    player "Everyone says the same thing... What's with you all..."
    lepanto "Why don't you get out of here right now... for your own good..."
    player "Mmm..."
    player "You're trying to act tough, but you're a terrible actor..."
    player "Aren't you the commander of the current king's army?!? You should be a bit more respectful.."
    lepanto "Hah!"
    lepanto "The current king... It's not even worth discussing the matter with a foreigner..."
    lepanto "You have no idea how much is happening here..."
    lepanto "I'm loyal to only one king... but it's too late for that..."
    lepanto "They asked me to clean the tournament of competitors... and that's exactly what I'll do..."
    lepanto "I prefer making money to chasing an unrealistic dream"
    lepanto "Get ready, kid!!!"

    call fight_start pass (enemy_pass = enemy_lepanto, no_run = True, no_interface = True) from _fight_enemy_lepanto


    lepanto "Ughhh... damn... I underestimated you way too much..."
    lepanto "You're really strong, kid..."
    lepanto "I hope you achieve your goal... and get what you're looking for..."
    lepanto "You're young... you still have hope..."
    lepanto "I've failed as a commander... I've disappointed my king, and he's dead now..."
    player "(!!!)"
    lepanto "Now I work for a false king... my life has no honor..."
    lepanto "I've tried for so many years... to protect my princess... but..."
    lepanto "But in the end, I've failed here too..."

    $ _window_hide()
    hide expression enemy_lepanto.image with Dissolve(0.8)
    pause 0.5
    
    $ black_to_img("events dressrosa h6 h6_gatz")

    gatz "Ohhhh!! No way, Captain Tank has fallen?!?"
    gatz "The crowd is going wild!!!! [player.n] wiiins!"
    gatz "Incredible!! Against all odds, [player.n] proved we shouldn't judge by appearances!"
    gatz "What a spectacular first match we've had!!"
    gatz "[player.n], please return to the fighters's preparation room and recover until your next fight!!"
    player "Alright!!"
    player "(Looks like I have to wait now...)"
    player "(Maybe I can spend some time with that beautiful warrior angel!!)"
    gatz "Let's take a short break while the next competitors prepare and head to the arena!!"
    gatz "We'll be back shortly, stay tuned!"

    stop ambient
    $ Dressrosa.h = 7
    $ _window_hide()
    $ ui_interface = True
    jump dr_ac_co_fighters_preparations
