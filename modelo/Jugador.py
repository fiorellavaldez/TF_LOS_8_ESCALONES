class Jugador():
    def __init__ (self, nombre, avatar):

        #Constructor para inicializar un jugador.
        #-parametro nombre: str, nombre del jugador
        #-parametro avatar: str, avatar del jugador (puede ser una cadena con la ruta de la imagen o el nombre del avatar)

        self.__nombre = nombre  # Nombre del jugador
        self.__avatar = avatar  # Avatar del jugador
        self.__ronda1 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__ronda2 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__escalon_actual = 1  # Escalón inicial

    def avanzar_escalon(self):
        # Método para avanzar al siguiente escalón
        self.__escalon_actual += 1
    
        # Getters
    def get_nombre(self):
        return self.__nombre

    def get_avatar(self):
        return self.__avatar

    def get_ronda1(self):
        return self.__ronda1

    def get_ronda2(self):
        return self.__ronda2

    def get_escalon_actual(self):
        return self.__escalon_actual

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_avatar(self, avatar):
        self.__avatar = avatar

    def set_ronda1(self, ronda1):
        self.__ronda1 = ronda1

    def set_ronda2(self, ronda2):
        self.__ronda2 = ronda2