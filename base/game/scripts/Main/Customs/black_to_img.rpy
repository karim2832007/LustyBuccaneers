# Version event: 1
# Version game: 0.32

init -1000 python:
    def black_to_img(image_name, dur=0.8, screen_name="screen_black", layer="master", at_list=None, zorder=None, behind=None, hide=None):
        """
        image_name : nombre completo de la imagen a mostrar (p.ej. "events dressrosa h1 h1_1")
        hide       : string o lista con imágenes a ocultar ANTES de mostrar la nueva.
        Puede ser nombre completo o tag; se extrae el tag automáticamente.
        Ej: "events dressrosa h1 h1_1" -> tag "events"
        """

        # -------- Normalizaciones --------
        image_name = str(image_name) if image_name is not None else ""

        # at_list -> lista de transforms
        if at_list is None:
            at_list = []
        elif not isinstance(at_list, (list, tuple)):
            at_list = [at_list]

        # behind -> lista de tags
        if behind is None:
            behind = []
        elif isinstance(behind, (str, bytes)):
            behind = [behind]
        elif not isinstance(behind, (list, tuple)):
            behind = [behind]

        # hide -> lista de NOMBRES o TAGS; lo paso a lista de TAGS
        def _to_tag(name_or_tag):
            s = str(name_or_tag).strip()
            # si viene "events dressrosa h1 h1_1" devuelvo "events"
            return s.split()[0] if " " in s else s

        if hide is None:
            hide_tags = []
        elif isinstance(hide, (list, tuple)):
            hide_tags = [_to_tag(x) for x in hide]
        else:
            hide_tags = [_to_tag(hide)]

        # -------- Window & transición a negro --------
        _window_hide()

        renpy.show_screen(screen_name)
        renpy.with_statement(Dissolve(dur))

        # -------- Ocultar imágenes anteriores (por tag) --------
        for t in hide_tags:
            renpy.hide(t, layer=layer)

        # -------- Mostrar imagen nueva --------
        renpy.show(image_name, at_list=at_list, layer=layer, zorder=zorder, behind=behind)

        # -------- Salir de negro --------
        renpy.hide_screen(screen_name)
        renpy.with_statement(Dissolve(dur))

        #_window_show(auto=True)
