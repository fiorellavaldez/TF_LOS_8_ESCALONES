class Partida():
    def __init__(self, escalones):
        self.__escalones = escalones
    
    def set_escalones(self, escalones):
        self.__escalones = escalones
    def get_escalones(self):
        return self.__escalones