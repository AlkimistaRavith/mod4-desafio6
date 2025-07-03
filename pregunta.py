from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, requerida, alternativas, ayuda=None):
        self._enunciado = enunciado
        self._ayuda = ayuda
        self._requerida = requerida
        self._alternativas = [
            Alternativa(alt["contenido"], alt.get("ayuda"))
            for alt in alternativas
        ]

    @property
    def enunciado(self):
        return self._enunciado

    @enunciado.setter
    def enunciado(self, nuevo_enunciado):
        self._enunciado = nuevo_enunciado

    @property
    def ayuda(self):
        return self._ayuda

    @ayuda.setter
    def ayuda(self, nueva_ayuda):
        self._ayuda = nueva_ayuda

    @property
    def requerida(self):
        return self._requerida

    @requerida.setter
    def requerida(self, valor):
        self._requerida = valor

    @property
    def alternativas(self):
        return self._alternativas.copy()  # evitar modificación directa

    def mostrar(self):
        print(f"Enunciado: {self._enunciado}")
        if self._ayuda:
            print(f"Ayuda: {self._ayuda}")
        for i, alt in enumerate(self._alternativas, 1):
            print(f"Alternativa {i}:")
            alt.mostrar()
