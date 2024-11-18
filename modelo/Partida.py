class Partida():
    def __init__(self, escalones, jugadores):
        self.__escalones = escalones
        self.__jugadores = jugadores

    def set_escalones(self, escalones):
        self.__escalones = escalones
    def get_escalones(self):
        return self.__escalones
    
    def set_jugadores(self, jugadores):
        self.__jugadores = jugadores
    def get_jugadores(self):
        return self.__jugadores