# Version event: 1
# Version game: 0.1

image GUI clock = ConditionSwitch(
    "game.clock.morning", "GUI clock morning clock_time",
    "game.clock.afternoon", "GUI clock afternoon clock_time",
    "game.clock.evening", "GUI clock evening clock_time",
    "game.clock.night", "GUI clock night clock_time",
)