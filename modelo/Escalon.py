class Escalon():
    # escalon_partida = nro_escalon(pk) + estado + id_tema
#################################################################
    def __init__(self, nro_escalon):
        self.__nro_Escalon = nro_escalon
        self.__tema = None
        self.__estado = False # falso no se esta el escalon, True se esta jugando
        self.__jugadores = []
    

    #Getters
    def get_tema (self):
        return self.__tema
    def get_jugadores(self):
        return self.__jugadores
    def get_nro_escalon (self):
        return self.__nro_Escalon
    def get_estado(self):
        return self.__estado
     
    #setters
    def set_nro_escalon(self, nro_escalon):
        self.__nro_Escalon = nro_escalon
    def set_jugadores(self, listaJugadores):
        self.__jugadores = listaJugadores
    def set_tema(self, tema):
        self.__tema = tema
    def set_estado (self, estado):
        self.__estado = estado
        
    def eliminar_jugador(self, jugador): # Esto es para sacar de la lista de jugadores activos, al jugador que perdio en ese escalon
        self.__jugadores.remove(jugador)
    
    #def set_jugadorEliminado(self, jugador): # agrega al jugador que perdio a jugadorEliminado
    #    self.__jugadorEliminado = jugador
    #def get_jugadorEliminado(self):
    #    return self.__jugadorEliminado