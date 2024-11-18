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

    def get_all_jugadores(self):
            with self.__bd.cursor() as cursor:
                cursor.execute("SELECT id_partida, id_jugador,ronda1, ronda2 FROM jugador_partida")
                return cursor.fetchall()
            
    def agregar_jugador(self, jugador): # chequear si los cambios estan bien
        with self.__bd.cursor() as cursor:
            indice_jugador  = int(cursor.execute ("SELECT MAX(id_jugador) FROM jugador ")) #como id jugador no esta en el objeto jugador hago esto, no se si tendria que ser +1
            cursor.execute(
                """INSERT INTO jugador (id_jugador, nombre_jugador , avatar) 
                VALUES (%s, %s, %s)""",
                (indice_jugador, jugador.get_nombre_jugador(), jugador.get_avatar())
            )
            cursor.connection.commit()

    def limpiar_tabla_partida(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("DELETE * from jugador_partida")
            cursor.connection.commit()