from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre, preguntas):
        self._nombre = nombre
        self._preguntas = preguntas  # lista de objetos Pregunta
        self._listados_respuestas = []  # lista de objetos ListadoRespuestas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def preguntas(self):
        return self._preguntas

    @property
    def listados_respuestas(self):
        return self._listados_respuestas

    def mostrar(self):
        print(f"\nEncuesta: {self._nombre}")
        for i, pregunta in enumerate(self._preguntas, 1):
            print(f"\nPregunta {i}:")
            pregunta.mostrar()

    def agregar_listado_respuestas(self, listado):
        if isinstance(listado, ListadoRespuestas):
            self._listados_respuestas.append(listado)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, preguntas, edad_minima, edad_maxima):
        super().__init__(nombre, preguntas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    @property
    def edad_minima(self):
        return self.__edad_minima

    @property
    def edad_maxima(self):
        return self.__edad_maxima

    def agregar_listado_respuestas(self, listado):
        edad = listado.usuario.edad
        if self.__edad_minima <= edad <= self.__edad_maxima:
            super().agregar_listado_respuestas(listado)
        else:
            print("Usuario fuera del rango de edad permitido.")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas, regiones):
        super().__init__(nombre, preguntas)
        self.__regiones = regiones  # lista de enteros

    @property
    def regiones(self):
        return self.__regiones

    def agregar_listado_respuestas(self, listado):
        region = listado.usuario.region
        if region in self.__regiones:
            super().agregar_listado_respuestas(listado)
        else:
            print("Región del usuario no permitida para esta encuesta.")
