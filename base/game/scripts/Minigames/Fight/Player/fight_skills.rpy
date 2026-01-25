# Version event: 1
# Version game: 0.23

label fight_skills():
    # Player attack
    #$ ability_damage, ability_name, attack_type = RPGPlayer.use_ability( id = action_id )
    $ ability_damage, ability = RPGPlayer.use_ability( ability_key = action_id )

    $ print(f"Using ability: {ability.name}")
    $ print(f"Ability damage: {ability_damage}")

    $ damage, criti_attack = RPGPlayer.attack(attack_type=ability.attack_type, ability_damage=ability.damage, multiplier=ability.multiplier)

    if criti_attack:
        narrador "A CRITICAL HIT!"

    if ability.image:
        show screen skill_effect_player(ability.image) with Dissolve(0.3)

    narrador "[ability.name]"
    $ talk = enemy_figth.take_damage(damage = damage)

    narrador "[talk]"

    return