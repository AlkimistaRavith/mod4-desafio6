#2. clase Alternativa
class Alternativa:
    def __init__(self, contenido, ayuda):
        self._contenido = contenido
        self._ayuda = ayuda

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, nuevo_contenido):
        self._contenido = nuevo_contenido

    @property
    def ayuda(self):
        return self._ayuda

    @ayuda.setter
    def ayuda(self, nueva_ayuda):
        self._ayuda = nueva_ayuda

    #método mostrar.
    def mostrar(self):
        print(f"- {self._contenido}")
        if self._ayuda:
            print(f"  (Ayuda: {self._ayuda})")
