def decorar_texto(texto):
    return f"✨ {texto.upper()} ✨"

class FilterModule(object):
    def filters(self):
        return {
            'decorar_texto': decorar_texto
        }
