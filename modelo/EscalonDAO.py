import psycopg2
from psycopg2.extras import RealDictCursor
from .bd import Database
from Escalon import Escalon

class EscalonDAO:
    def __init__(self):
        self.__bd = Database()
    
    def get_escalon(self, nro_escalon):
        with self.__bd.cursor() as cursor:
            query = "SELECT * FROM escalon WHERE nro_escalon = %s"
            cursor.execute(query, (nro_escalon,))
            return cursor.fetchone()


    def agregar_escalon(self, escalon):
        with self.__bd.cursor() as cursor:
            query = "INSERT INTO escalon (id_tema, estado) VALUES (%s, %s) RETURNING nro_escalon"
            cursor.execute(query, (escalon.get_tema(), escalon.get_estado()))
            self.connection.commit()
            return cursor.fetchone()[0]

    def actualizar_escalon(self, escalon):
        with self.__bd.cursor() as cursor:
            query = "UPDATE escalon SET id_tema = %s, estado = %s WHERE nro_escalon = %s"
            cursor.execute(query, (escalon.get_tema(), escalon.get_estado(), escalon.get_nro_escalon()))
            self.__bd.commit()

    def borrar_escalon(self, nro_escalon):
        with self.__bd.cursor() as cursor:
            query = "DELETE FROM escalon WHERE nro_escalon = %s"
            cursor.execute(query, (nro_escalon,))
            self.__bd.commit()
