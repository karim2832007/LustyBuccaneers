# Version event: 4
# Version game: 0.4

init -1 python:
    class createCharacter(renpy.character.ADVCharacter):
        def resolve_say_attributes(self, predict, attrs):            
            if not self.image_tag:
                self.image_tag = "none"

            talk_on = (not predict and self.image_tag and last_image_tag != self.image_tag)
        
            if not attrs and not talk_on:
                return

            # necesario?
            if attrs is None:
                attrs = ()
            else:
                attrs = tuple(attrs)
            
            tag_attrs = (self.image_tag,) + attrs
            
            images = renpy.game.context().images

            layer = renpy.exports.default_layer(None, self.image_tag)
            
            if images.showing(layer, (self.image_tag,)):
                
                final_image = images.apply_attributes(layer, self.image_tag, tag_attrs)
                
                if final_image is None:
                    final_image = tag_attrs
                
                show_image = (self.image_tag,) + attrs
                
                if predict:
                    renpy.exports.predict_show(final_image)
                else:
                    self.show_talk(show_image)
                    return True
                
        @property
        def n(self):#"#2b221b"
            return renpy.substitute("{outlinecolor=#2b221b}{color=" + str(self.who_args["color"]) + "}" + str(self.name) + "{/color}{/outlinecolor}{space=2}")# {/b}

        @property
        def color(self):#"#2b221b"
            return str(self.who_args["color"])

        def restore_say_attributes(self, predict, state, interact):
            # actualiza los last_image_tag
            global last_image_tag
            if not predict and self.image_tag:
                last_image_tag = self.image_tag
            return super(createCharacter, self).restore_say_attributes(predict, state, interact)
        
        @staticmethod
        def show_talk(name, at_list=None, layer=None, what=None, zorder=None, tag=None, behind=None, atl=None, transient=False, munge_name=True):            
            global last_image_tag
            
            at_list = at_list or []
            behind = behind or []

            # necesario tuplas?????
            if not isinstance(name, tuple):
                name = tuple(name.split())

            scene_lists = renpy.game.context(-1).scene_lists
            #renpy.display.core.scene_lists()

            #key es necesario? siempre es key no????
            key = tag or name[0]
            layer = renpy.default_layer(layer, key)
            
            # si no tiene valor lista y 
            if not at_list and key in scene_lists.at_list[layer]:
                at_list = scene_lists.at_list[layer][key]
            
            if a_talk in at_list:
                at_list.remove(a_talk)

            #ERRROR: si se esta moviendo eliminar x_move sino poner una variable activa que la proxima vez la borre
            
            # En rollback no va, tampoco con skip
            if key != last_image_tag and not renpy.is_skipping() and not renpy.in_rollback():
                at_list.insert(0, a_talk)
                last_image_tag = key
            
            renpy.show(name, at_list, layer, what, zorder, tag, behind, atl, transient, munge_name)

default last_image_tag = None