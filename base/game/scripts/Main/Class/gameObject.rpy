# Version event: 1
# Version game: 0.4

init -990 python:
    class gameObject(objectRevertable):
        def __init__(self):
            super().__init__()
            self.clock = gameClock()
            self.location = None

default game = gameObject()

