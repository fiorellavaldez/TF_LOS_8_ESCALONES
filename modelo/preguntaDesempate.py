from modelo.Pregunta import Pregunta

class preguntaDesempate(Pregunta):
    def __init__(self, tema, enunciado, respuestaCorrecta):
        super().__init__(tema, enunciado)
        self.__respuestaCorrecta = respuestaCorrecta
    
    #Getters
    def get_respuestaCorrecta (self):
        return self.__respuestaCorrecta

    #Setters
    def set_respuestaCorrecta(self, respuestaCorrecta):
        self.__respuestaCorrecta = respuestaCorrecta


    def responder(self, respuesta):
        return abs( self.__respuestaCorrecta - respuesta) # devuelve la distancia entre la respuesta correcta y la respuesta del jugador
    


    

    

    



    



    
