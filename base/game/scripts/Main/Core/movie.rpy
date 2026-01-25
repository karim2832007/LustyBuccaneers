# Version event: 1
# Version game: 0.15

init python:
    class MovieFallback(renpy.display.video.Movie):
        def __init__(self, *args, **kwargs):
            self.character = kwargs["character"] if "character" in kwargs else None
            
            if "play" in kwargs:
                if not renpy.loader.loadable(kwargs["play"]):
                    kwargs["play"] = None
                self._original_play = kwargs["play"]
            
            if "image" in kwargs and "start_image" not in kwargs:
                kwargs["start_image"] = kwargs["image"]
            
            super(MovieFallback, self).__init__(*args, **kwargs)
        
        def play(self, old):
            #if self.character:
            #    skin = skins.filter_character(self.character, True)
            #    if len(skin) > 0:
            #        new_play = "skin/{}/{}".format(skin[0].name, self._original_play)
            #        if renpy.loader.loadable(new_play):
            #            self._play = new_play
            #    else:
            #        self._play = self._original_play
            
            return super(MovieFallback, self).play(old)
