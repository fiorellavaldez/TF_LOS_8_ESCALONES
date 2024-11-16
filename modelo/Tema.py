class Tema():
    def __init__(self, idTema, nombreTema):
        self.__disponible = False # se inicia un tema como no disponible y se evalua la disponibilidad una vez se agrega una pregunta
        self.__idTema = idTema
        self.__nombreTema = nombreTema
        self.__preguntasRonda = []
        self.__preguntasDesempate = []

    # Getter y setter para disponible
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self, disponible):
        self.__disponible = disponible

    # Getter y setter para idTema
    def get_idTema(self):
        return self.__idTema
    def set_idTema(self, idTema):
        self.__idTema = idTema

    # Getter y setter para nombreTema
    def get_nombreTema(self):
        return self.__nombreTema
    def set_nombreTema(self, nombreTema):
        self.__nombreTema = nombreTema

    # Getter y setter para preguntasRonda
    def get_preguntasRonda(self):
        return self.__preguntasRonda
    def set_preguntasRonda(self, preguntasRonda):
        self.__preguntasRonda = preguntasRonda

    # Getter y setter para preguntasDesempate
    def get_preguntasDesempate(self):
        return self.__preguntasDesempate
    def set_preguntasDesempate(self, preguntasDesempate):
        self.__preguntasDesempate = preguntasDesempate