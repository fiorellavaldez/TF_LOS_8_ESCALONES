from  modelo.JugadorDAO import JugadorDAO
from modelo.Jugador import Jugador 

class JugadorABM:
    def __init__(self):
        self.__lista_jugadores = self.obtener_jugadores()
    
    @property
    def lista_jugadores(self):
        return self.__lista_jugadores
    
    def obtener_jugadores(self):
        lista=JugadorDAO().get_all_jugadores()
        lista_jugadores=[]
        for id_jugador,nombre_jugador, avatar in lista: #estamos ignorando el atributo estado_tema, pasara algo?
            jug = (Jugador(nombre_jugador, avatar)) 
            jug.set_idjugador(id_jugador)
            lista_jugadores.append(jug)
        return lista_jugadores
            
    
    def actualizar_jugador(self, jugador: Jugador):
        for j in range(0,len(self.lista_jugadores)):
            if self.lista_jugadores[j].get_idjugador() == jugador.get_idjugador():
                self.lista_jugadores[j].set_nombre(jugador.get_nombre_jugador())
                self.lista_jugadores[j].set_avatar(jugador.get_avatar())
        JugadorDAO().actualizar_jugador(jugador.get_idjugador(), jugador.get_nombre_jugador(), jugador.get_avatar())


    def existe_jugador(self, jugador: Jugador):
        tope =len(self.__lista_jugadores)
        id = 0 
        encontrado = False
        while id < tope and not encontrado:
            if self.__lista_jugadores[id].get_nombre_jugador() == jugador.get_nombre_jugador():
                encontrado = True
            id +=1
        return encontrado

    def agregar_jugador(self, jugador: Jugador):
        self.__lista_jugadores.append(jugador)
        JugadorDAO().agregar_jugador(jugador.get_nombre_jugador(), jugador.get_avatar())

#Los jugadores no se borran?