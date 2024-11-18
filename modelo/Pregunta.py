from abc import ABC

class Pregunta:
    def __init__(self, idTema, enunciado):
        self._idPregunta = None
        self._idtema = idTema
        self._enunciado = enunciado

    
    def get_enunciado (self):
        return self._enunciado
    
    def set_enunciado(self, enunciado):
        self._enunciado = enunciado
    
    def get_idPregunta(self):
        return self._idPregunta
    
    def set_idPregunta(self, id_pregunta):
        self._idPregunta = id_pregunta

    def get_idtema (self):
        return self._idtema
    
    def set_idtema (self, idtema):
        self._idtema = idtema
 
 
