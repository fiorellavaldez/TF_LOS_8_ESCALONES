class jugadorPartido():
    # jugador_partida = id_partida(pk) + id_jugador + ronda1 + ronda
    
    
    # RESOLVER DOMINGO: COMO MANEJAR RONDAS? 
    # SI, SE INICIALIZA EN 0, PERO CUANDO SE RESTAURA HAY QUE TRAER DE BASE
    def __init__(self, id_jugador, ronda1, ronda2):
        ## ME HACE RUIDO ID_JUGADOR 
        ## pero aca no es clave y es muy probable que lo necesiten
        self.__id_jugador =  id_jugador
        self.__ronda1 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        self.__ronda2 = 0  # 0: no contestó, 1: respondió bien, 2: respondió mal
        
        
    
    ############################################ GETTERS
    def get_id_jugador(self):
        return self.__id_jugador
    def get_ronda1(self):
        return self.__ronda1
    def get_ronda2(self):
        return self.__ronda2


############################################ SETTERS

    def set_id_jugador(self, id_jugador):
        self.__id_jugador = id_jugador
    def set_ronda1(self, ronda1):
        self.__ronda1 = ronda1
    def set_ronda2(self, ronda2):
        self.__ronda2 = ronda2