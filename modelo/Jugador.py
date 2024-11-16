class Jugador():
    def __init__ (self, nombre, avatar):

        #Constructor para inicializar un jugador.
        #-parametro nombre: str, nombre del jugador
        #-parametro avatar: str, avatar del jugador (puede ser una cadena con la ruta de la imagen o el nombre del avatar)

        self.__nombre = nombre  # Nombre del jugador
        self.__avatar = avatar  # Avatar del jugador
        
        #BORRAR DOMINGO:
        """BORRAR DOMINGO, ESTO VOLO: rondas se fueron a jugadorPartido
        PERO ESCALON VA A TENER QUE IR EN OTRO LADO!!!
        self.__ronda1 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__ronda2 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__escalon_actual = 1  # Escalón inicial
        """
    
        # Getters
    def get_nombre_jugador(self):
        return self.__nombre

    def get_avatar(self):
        return self.__avatar




    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_avatar(self, avatar):
        self.__avatar = avatar

