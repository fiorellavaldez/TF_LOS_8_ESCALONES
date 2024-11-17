import psycopg2
from .bd import Database
import hashlib
import random

#################### ESTRUCTURA #################################
# TEMAS = id_tema(pk) + nombre_tema + estado_tema
#################################################################

class TemasDAO:
    def __init__(self):
        self.__bd = Database()

    ################################ LECTURA ####################################
    def get_all_temas(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * FROM temas")
            return cursor.fetchall()

    def get_tema(self, id_tema): 
        with self.__bd.cursor() as cursor:
            cursor.execute(
                "SELECT id_tema, nombre_tema FROM temas WHERE id_tema = %s ", 
                (id_tema,)
                )
            return cursor.fetchone()

    def temas_partida (self): #Devuelve lista con 8 temas
        temas = self.get_all_temas()
        lista_temas_partida = []
        random.shuffle(temas)
        for i in range (0,9):
            lista_temas_partida.append(temas.pop())
        return lista_temas_partida    
    

    ################################ CREAR ####################################
    def agregar_tema(self, tema):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                "INSERT INTO temas (nombre_tema) VALUES (%s)",
                (tema,)
                )
            cursor.connection.commit()
            
    ################################ ACTUALIZAR ####################################
    def actualizar_tema(self, id, tema):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                "UPDATE temas SET nombre_tema = %s WHERE id_tema = %s",
                (tema, id)
                )
            cursor.connection.commit()


    ##################################### BORRAR #########################################
    def borrar_tema(self, id_tema):
        with self.__bd.cursor() as cursor:
            #cursor.execute(" UPDATE temas SET estado_tema = FALSE WHERE id_tema = %s", (id_tema,))
            cursor.execute("DELETE FROM temas WHERE id_tema = %s", (id_tema,))
            cursor.connection.commit()