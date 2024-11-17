from modelo.Pregunta import Pregunta

class preguntaDesempate(Pregunta):
    def __init__(self, tema, enunciado, respuestaCorrecta):
        super().__init__(tema, enunciado)
        self.__respuestaCorrecta = respuestaCorrecta
    
    #Getters
    def get_respuestaCorrecta (self):
        return self.__respuestaCorrecta
    def get_enunciado (self):
        return self._enunciado
    def get_idPregunta(self):
        return self._idPregunta
    def get_idtema (self):
        return self._tema
    def get_estado (self):
        return self._estado
    
    #Setters
    def set_respuestaCorrecta(self, respuestaCorrecta):
        self.__respuestaCorrecta = respuestaCorrecta

    def set_enunciado(self, enunciado):
        self._enunciado = enunciado

    def set_idPregunta(self, id_pregunta):
        self._id_pregunta = id_pregunta
    
    def set_idtema (self, idtema):
        self._tema = idtema
        
    def set_estado (self, estado):
        self._estado = estado

    def responder(self, respuesta):
        return abs( self.__respuestaCorrecta - respuesta) # devuelve la distancia entre la respuesta correcta y la respuesta del jugador
    


    

    

    



    



    
