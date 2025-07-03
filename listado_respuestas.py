from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        if not isinstance(usuario, Usuario):
            raise ValueError("usuario debe ser una instancia de Usuario.")
        if not all(isinstance(r, int) for r in respuestas):
            raise ValueError("Todas las respuestas deben ser números enteros.")
        
        self._usuario = usuario
        self._respuestas = respuestas

    @property
    def usuario(self):
        return self._usuario

    @property
    def respuestas(self):
        return self._respuestas.copy()  # prevenir modificación directa
