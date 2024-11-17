import psycopg2
from .bd import Database
import hashlib

#################### ESTRUCTURA #################################
# jugador_partida = id_partida(pk) + id_jugador + ronda1 + ronda
#################################################################
#ACLARACION: Cada tupla/fila guarda un jugador, aclaro porque id_partida no es descriptivo
#Estaria bueno cambiarlo EL DOMINGO 20 

class JugadorPartidaDAO:
    def __init__(self):
        self.__bd = Database()
    
    ######################################## LECTURA ########################################
    # EXTRAE LOS 8 JUGADORES PARA RESTAURAR
    def get_all_jugadores(self):
            with self.__bd.cursor() as cursor:
                cursor.execute("SELECT id_partida, id_jugador,ronda1, ronda2 FROM jugador_partida")
                return cursor.fetchall()

    """ Este se puede usar si queremos guardar mas de una partida, sino lo borramos
    def get_partida(self, id_partida):
            with self.__bd.cursor() as cursor:
                cursor.execute("SELECT * FROM jugador WHERE id_partida = %s", (id_partida,))
                return cursor.fetchone()
    """
    
    ######################################## CREAR ########################################
    def agregar_jugador(self, jugador): # chequear si los cambios estan bien
        with self.__bd.cursor() as cursor:
            indice_jugador  = int(cursor.execute ("SELECT MAX(id_jugador) FROM jugador ")) #como id jugador no esta en el objeto jugador hago esto, no se si tendria que ser +1
            cursor.execute(
                """INSERT INTO jugador (id_jugador, nombre_jugador , avatar) 
                VALUES (%s, %s, %s)""",
                (indice_jugador, jugador.get_nombre_jugador(), jugador.get_avatar())
            )
            self.__bd.commit()
            
    ######################################## ACTUALIZAR ########################################
    # La tabla jugador_partida no tiene actualizaciones.

    ######################################## ELIMINAR ########################################
    def limpiar_tabla_partida(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("DELETE * from jugador_partida")
            self.__bd.commit()
