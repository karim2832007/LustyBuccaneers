# Version event: 1
# Version game: 0.1

init -1000 python:
    class objectRevertable(renpy.python.RevertableObject):
        #nosave = []
        
        # Devuelve un diccionario que contiene todos los atributos del objeto
        def __getstate__(self):
            return vars(self).copy()

        #  Actualiza los atributos del objeto (self) con los valores del diccionario proporcionado
        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)