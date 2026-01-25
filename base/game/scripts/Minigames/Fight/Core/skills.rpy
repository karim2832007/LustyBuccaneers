# Version event: 2
# Version game: 0.40

default armament_punch = False

init -1 python:
    class Ability:
        """Define una habilidad mágica con daño y costo de maná."""
        def __init__(self, name, damage, mana_cost, multiplier, attack_type="magic", image="none"):
            self.name = name
            self.damage = damage
            self.mana_cost = mana_cost
            self.multiplier = multiplier
            self.attack_type = attack_type
            self.image = image

    # Base de datos de habilidades mágicas
    ABILITIES = {
        # Habilidades mágicas (usan power y gastan mana)
        "Fireball": Ability("Fireball", 40, 30, 2, "magic"),

        # Player
        "Strong attack": Ability("Strong attack", 20, 30, 2, "physical"),

        # Crocodile
        "Desert spada": Ability("Desert spada", 30, 25, 1.5, "magic", image="skill_desert_spada"),
        "Sables": Ability("Sables", 40, 30, 2, "magic", image="skill_sables"),

        # Diamante
        "Death Swarm": Ability("Death Swarm", 50, 50, 1.5, "magic", image="skill_death_swarm"),
        "Half Moon Glaive": Ability("Half Moon Glaive", 60, 60, 2, "magic", image="skill_half_moon_glaive"),

        # Haki
        "Armament Punch": Ability("Armament Punch", 70, 50, 2, "physical", image="skill_armament_punch"),

    }