#from .PreguntasDAO import PreguntasDAO
#eso me parece qye bi va
from preguntaRonda import Pregunta

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
    def get_enunciado (self):
        return self._enunciado  
    def get_idPregunta(self):
        return self._idPregunta
    def get_idtema (self):
        return self._tema
    def get_estado (self):
        return self._estado
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
    def set_enunciado(self, enunciado):
        self._enunciado = enunciado
    def set_idPregunta(self, id_pregunta):
        self._id_pregunta = id_pregunta
    def set_estado (self, estado):
        self._estado = estado
    def set_idtema (self, idtema):
        self._tema = idtema
##############


    def responder(self,opcion):
        if opcion == self.__opcionCorrecta:
            return True
        else: 
            return False