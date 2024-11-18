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
            cursor.execute("SELECT nombre_jugador FROM jugador WHERE id_jugador = %s", (id_jugador,))
            return cursor.fetchone()
    ######################################## CREAR ########################################
    def agregar_jugador(self, nombre, avatar): # chequear si los cambios estan bien
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """INSERT INTO jugador ( nombre_jugador , avatar) 
                VALUES (%s, %s)""",
                (nombre, avatar)
            )
            cursor.connection.commit()

    ######################################## ACTUALIZAR ########################################
    def actualizar_jugador(self, id_jugador, nombre, avatar): #chequear si los cambios estan bien
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """UPDATE jugador SET nombre_jugador = %s, avatar = %s 
                WHERE id_jugador = %s""",
                (nombre, avatar, id_jugador)
            )
            cursor.connection.commit()
    



    ################################ BUSCAR ####################################

    def buscar_jugador(self, nombre):
        with self.__bd.cursor() as cursor:
            cursor.execute(
            """SELECT COUNT(*) FROM jugador WHERE nombre_jugador = %s""",
            (nombre,) ) # Asegúrate de pasar 'nombre' como una tupla
        
            resultado = cursor.fetchone()
          
        if resultado[0] == 1:  # Acceder al primer elemento de la tupla resultado
            return True
        else:
            return False
#Todos los metodos que estan arriba de esta marca funcionan bien

            #SI HAY 0 :  0 > 0 RETURN FALSE
            #SI YA HAY 1 (si esta el nombre) 1>0 RETURN TRUE 
            
    