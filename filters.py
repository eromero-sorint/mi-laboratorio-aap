# filter_plugins/mis_filtros.py

def decorar_texto(texto):
    """Convierte el texto a mayúsculas y le añade estrellas."""
    return f"✨ {texto.upper()} ✨"

class FilterModule(object):
    def filters(self):
        return {
            'decorar_texto': decorar_texto
        }
