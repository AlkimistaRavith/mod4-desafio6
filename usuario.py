from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        self._correo = correo
        self._edad = edad
        self._region = region

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, nueva_region):
        self._region = nueva_region

    def contestar_encuesta(self, encuesta, respuestas):
        listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado)
