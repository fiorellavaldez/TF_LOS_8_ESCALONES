import psycopg2
from .bd import Database
import hashlib

#################### ESTRUCTURA ####################
# jugador = id_jugador(pk) + nombre_jugador + avatar
#####################################################

class JugadorDAO:
    def __init__(self):
        self.__bd = Database()
    
    ######################################## LECTURA ########################################
    def get_all_jugadores(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * FROM jugador")
            return cursor.fetchall()

    def get_jugador(self, id_jugador):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT nombre_jugador, FROM jugador WHERE id_jugador = %s", (id_jugador,))
            return cursor.fetchone()
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
    def actualizar_jugador(self, id_jugador, nombre, avatar): #chequear si los cambios estan bien
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """UPDATE jugador SET nombre_jugador = %s, avatar = %s 
                WHERE id_jugador = %s""",
                (nombre, avatar, id_jugador)
            )
            self.__bd.commit()
            
            
    ######################################## ELIMINAR #######################################
    def borrar_jugador(self, id_jugador): #jugador ya no tiene la columna estado_jugador esto ya no iria
        with self.__bd.cursor() as cursor:
            cursor.execute("UPDATE jugador SET estado_jugador FALSE WHERE id_jugador = %s", (id_jugador,))
            self.__bd.commit()
