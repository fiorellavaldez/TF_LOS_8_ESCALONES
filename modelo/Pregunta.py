from abc import ABC

class Pregunta(ABC):
    def __init__(self, tema, enunciado):
        self._idPregunta = None
        self._tema = tema
        self._enunciado = enunciado
    
    def get_enunciado (self):
        return self._enunciado
    
    def set_enunciado(self, enunciado):
        self._enunciado = enunciado
    
    def get_idPregunta(self):
        return self._idPregunta
    
    def set_idPregunta(self, id_pregunta):
        self._id_pregunta = id_pregunta