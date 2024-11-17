class Jugador():
    def __init__ (self, nombre, avatar):
        self.__id_jugador =  None
        self.__ronda1 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__ronda2 = 0 
        self.__nombre = nombre  # Nombre del jugador
        self.__avatar = avatar  # Avatar del jugador

    
        # Getters
    def get_nombre_jugador(self):
        return self.__nombre

    def get_avatar(self):
        return self.__avatar
    def get_idjugador(self):
        return self.__id_jugador
    def get_ronda1(self):
        return self.__ronda1
    def get_ronda2(self):
        return self.__ronda2

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_avatar(self, avatar):
        self.__avatar = avatar
    def set_idjugador(self, idjugador):
        self.__id_jugador = idjugador

    def set_ronda1 (self, ronda1):
        self.__ronda1 = ronda1
    def set_ronda2 (self,ronda2):
        self.__ronda2 = ronda2

    def actualizar_ronda(self, ronda1, ronda2): #este metodo es para que le pongan los valores que sacaron de las tuplas
        self.set_ronda1(ronda1)
        self.set_ronda2(ronda2)
