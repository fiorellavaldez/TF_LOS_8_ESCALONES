import psycopg2
from .bd import Database
import hashlib
#En teoria esto deberia guardar la instancia en la que se encuentra el juego
#################### ESTRUCTURA #################################
# jugador_partida = id_partida(pk) + id_jugador + ronda1 + ronda
#################################################################
#ACLARACION: Cada tupla/fila guarda un jugador, aclaro porque id_partida no es descriptivo
#Estaria bueno cambiarlo EL DOMINGO 20 

class JugadorPartidaDAO:
    def __init__(self):
        self.__bd = Database()

    def get_all_jugadores_partida(self): #obtengo TODA la informacion de las tuplas de la tabla jugador_partida
            with self.__bd.cursor() as cursor:
                cursor.execute("SELECT id_partida, id_jugador,ronda1, ronda2 FROM jugador_partida")
                return cursor.fetchall()
            
    def agregar_jugador_partida(self, jugador): # entra una objeto jugador, y se lo agrega a la tabla jugador_partida
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """INSERT INTO jugador_partida (ronda1, ronda2, id_jugador) 
                VALUES (%s, %s, %s)""",
                (jugador.get_ronda1(), jugador.get_ronda2(), jugador.get_idjugador())
            )
            cursor.connection.commit()

    def actualizar_jugador_partida (self, jugador, escalon): #PRUEBA PARA GUARDAR LAS INSTANCIAS DE LAS PARTIDAS
         #if escalon.get_estado() == True:
         with self.__bd.cursor() as cursor:
              cursor.execute ("""UPDATE jugador SET ronda1 =%s, ronda2=%s 
                              WHERE id_jugador= %s""",
                              (jugador.get_ronda1(), jugador.get_ronda2(), jugador.get_idjugador())
              )
              cursor.connection.commit()
              
              
         
         

    def limpiar_tabla_partida(self): #borra todos los datos de jugador_partida, el id partida retoma desde donde quedo(no es un problema)
        with self.__bd.cursor() as cursor:
            cursor.execute("DELETE from jugador_partida")
            cursor.connection.commit()