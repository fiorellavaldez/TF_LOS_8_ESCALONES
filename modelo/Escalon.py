class Escalon():
    def __init__(self):
        #self.__idEscalon = 0
        self.__tema = None
        self.__jugadores = []
    
    def get_tema (self):
        return self.__tema
    def set_tema(self, tema):
        self.__tema = tema
    
    def get_jugadores(self):
        return self.__jugadores
    def set_jugadores(self, listaJugadores):
        self.__jugadores = listaJugadores

    def eliminar_jugador(self, jugador): # Esto es para sacar de la lista de jugadores activos, al jugador que perdio en ese escalon
        self.__jugadores.remove(jugador)
    
    #def set_jugadorEliminado(self, jugador): # agrega al jugador que perdio a jugadorEliminado
    #    self.__jugadorEliminado = jugador
    #def get_jugadorEliminado(self):
    #    return self.__jugadorEliminado