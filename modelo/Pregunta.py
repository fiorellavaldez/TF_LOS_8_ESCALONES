from abc import ABC

class Pregunta(ABC):
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
        self._id_pregunta = id_pregunta

<<<<<<< HEAD
    def get_idtema (self):
        return self._idtema
    
    def set_idtema (self, idtema):
        self._idtema = idtema
 
 
=======
    def get_idTema (self):
        return self._tema
    
    def set_idTema (self, idtema):
        self._tema = idtema
>>>>>>> 1f98bb39030c955d92607eb0afefefc8128d1cd5
