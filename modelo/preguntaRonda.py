from Pregunta import Pregunta

class preguntaRonda(Pregunta):
    def __init__(self, tema, enunciado, opcionA, opcionB, opcionC, opcionD, opcionCorrecta):
        super().__init__(tema, enunciado)
        self.__opcionA = opcionA
        self.__opcionB = opcionB
        self.__opcionC = opcionC
        self.__opcionD = opcionD
        self.__opcionCorrecta = opcionCorrecta
    
    # Getters
    def get_opcionA(self):
        return self.__opcionA
    def get_opcionB(self):
        return self.__opcionB
    def get_opcionC(self):
        return self.__opcionC
    def get_opcionD(self):
        return self.__opcionD
    def get_opcionCorrecta(self):
        return self.__opcionCorrecta

    # Setters
    def set_opcionA(self, opcionA):
        self.__opcionA = opcionA
    def set_opcionB(self, opcionB):
        self.__opcionB = opcionB
    def set_opcionC(self, opcionC):
        self.__opcionC = opcionC
    def set_opcionD(self, opcionD):
        self.__opcionD = opcionD
    def set_opcionCorrecta(self, opcionCorrecta):
        self.__opcionCorrecta = opcionCorrecta

    def responder(self,opcion):
        if opcion == self.__respuestaCorrecta:
            return True
        else: 
            return False