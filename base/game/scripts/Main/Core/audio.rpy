# Version event: 2
# Version game: 0.1


init python:
    class AudioChannelPrefix(object):
        def __init__(self,prefix=""):
            if prefix and prefix[-1]!=" ":
                # para despues ser audio door_open
                prefix+=" "#
            self.prefix=prefix
        def __add__(self,other):
            if isinstance(other,basestring):
                rv=getattr(audio,self.prefix+other,None)
                if rv is not None:
                    return rv
            return other


    def prepare_audio_channels():
        renpy.music.register_channel("ambient", "sfx", True, True)
        renpy.music.register_channel("gems", "sfx", False)
        #renpy.music.register_channel("ambient", "ambient", True, True)
        #renpy.music.alias_channel(1, "ambient")

        for channel_id,channel in renpy.audio.audio.channels.items():
            if isinstance(channel_id,basestring):
                prefix = channel_id
            else:
                prefix = "sound"

            channel.file_prefix=AudioChannelPrefix(prefix)

        #actulizo los auto_channels con los nuevos prefijos
        config.auto_channels={id:(mixer,AudioChannelPrefix(prefix or "sound"),suffix) for id,(mixer,prefix,suffix) in config.auto_channels.items()}

    prepare_audio_channels()


    def music_time_day():        
        #if game.clock.night:
        #    if renpy.music.get_playing() != "music_base_night":
        #        renpy.music.stop("music", 2.0)
        #        renpy.music.stop("sound", 1.0)
        #        renpy.music.play("music_base_night", "music", True, relative_volume=1.0)
        #else:
        if renpy.music.get_playing() != "music_base":
            renpy.music.stop("music", 2.0)
            renpy.music.stop("sound", 1.0)
            renpy.music.play("music_base", "music", True, fadein=2.0, relative_volume=1.0)

    def music_thrillerbark():
        if renpy.music.get_playing() != "music_thrillerbark":
            renpy.music.stop("music", 2.0)
            renpy.music.play("music_thrillerbark", "music", True, fadein=2.0, relative_volume=1.0)

    def music_drumisland():
        if renpy.music.get_playing() != "music_drumisland":
            renpy.music.stop("music", 2.0)
            renpy.music.play("music_drumisland", "music", True, fadein=2.0, relative_volume=1.0)

    def music_amazonlily():
        if renpy.music.get_playing() != "music_amazonlily":
            renpy.music.stop("music", 2.0)
            renpy.music.play("music_amazonlily", "music", True, fadein=2.0, relative_volume=1.0)

    def music_arabasta():
        if renpy.music.get_playing() != "music_arabasta":
            renpy.music.stop("music", 2.0)
            renpy.music.play("music_arabasta", "music", True, fadein=2.0, relative_volume=1.0)

    def music_elegia():
        if renpy.music.get_playing() != "music_elegia":
            renpy.music.stop("music", 2.0)
            renpy.music.play("music_elegia", "music", True, fadein=2.0, relative_volume=1.0)

    def music_dressrosa():
        if renpy.music.get_playing() != "music_dressrosa":
            renpy.music.stop("music", 2.0)
            renpy.music.play("music_dressrosa", "music", True, fadein=2.0, relative_volume=1.0)

    def ambient_ship():
        if game.clock.night:
            if renpy.sound.get_playing(channel="ambient") != "waves_night":
                renpy.music.stop("ambient", 2.0)
                renpy.music.play("waves_seagull", "ambient", True, fadein=1.0, relative_volume=1.0)
        else:
            if renpy.sound.get_playing(channel="ambient") != "waves_seagull":
                renpy.music.stop("ambient", 2.0)
                renpy.music.play("waves_seagull", "ambient", True, fadein=1.0, relative_volume=1.0)


    # SOUND FRAME
    import functools

    def frame_sound(sound, channel="sound"):
        return functools.partial(play_effect, sound, channel)

    def play_effect(sound, channel, trans, st, at):
        renpy.music.play(sound, channel)