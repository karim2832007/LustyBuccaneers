# Version event: 1
# Version game: 0.11

default version_id_save = 1

init python:
    def check_and_transfer():
        # 17/09/2024
        if renpy.store.version_id_save < 11:
            if 'tb_camp_boa' in globals():
                if renpy.store.tb_camp_boa:
                    renpy.store.tb_camp_hancock = True
                else:
                    renpy.store.tb_camp_hancock = False
                    if 'boa_name' in globals():
                        renpy.store.hancock_name = boa_name
        
            renpy.hide("boa")
            renpy.store.version_id_save = renpy.store.version_end
            renpy.block_rollback()

        else:
            renpy.store.version_id_save = renpy.store.version_end
        

define config.after_load_callbacks = [check_and_transfer]

#if hasattr(obj, 'attr_name'):
    #obj.attr_name exists.

#if 'myVar' in globals():
    #myVar exists.

#if 'myVar' in locals():
    #myVar exists.