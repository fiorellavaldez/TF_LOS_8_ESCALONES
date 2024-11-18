import psycopg2
from psycopg2.extras import DictCursor
from modelo.preguntaRonda import  preguntaRonda 
from modelo.preguntaDesempate import preguntaDesempate
from .bd import Database
import random
from modelo.Tema import  Tema


#################### ESTRUCTURA ####################################################
#  PREGUNTAS = id_pregunta(pk) + enunciado_pregunta + rta_a + rta_b 
#               + rta_c + rta_d + rta_correcta + tipo_pregunta 
#               + estado_pregunta + id_tema (FK) 
####################################################################################
class PreguntaDAO:
    def __init__(self):
        self.__bd = Database()
    ############################### LECTURA ####################################
    def get_all_preguntas(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * FROM preguntas WHERE estado_pregunta = TRUE") #Para que solo seleccione las preguntas "disponibles"
            return cursor.fetchall()

 #Por ahora no se usan   
    def get_pregunta_ronda(self, id_pregunta): 
        with self.__bd.cursor() as cursor: 
            query = "SELECT * FROM preguntas WHERE id_pregunta = %s and tipo_pregunta = 'M'" 
            cursor.execute(query, (id_pregunta,)) 
            return cursor.fetchone() 
        
    def get_pregunta_desempate(self, id_pregunta): 
        with self.__bd.cursor() as cursor: 
            query = "SELECT * FROM preguntas WHERE id_pregunta = %s and tipo_pregunta = 'D'" 
            cursor.execute(query, (id_pregunta,)) 
            return cursor.fetchone() 
 

    def devolver_preg_ronda (self, id_tema): #Ver si se usa
        lista_preguntas_ronda = []
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'M' and id_tema= %s and estado_pregunta = True", (id_tema,))
            preguntas_ronda = cursor.fetchall()
        random.shuffle(preguntas_ronda)
        for i in range (0,18):
            lista_preguntas_ronda.append(preguntas_ronda.pop())
        return lista_preguntas_ronda
    
    def devolver_pregunta_desempate (self, id_tema): #Ver si se usa
        lista_preguntas_desempate = []
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'D' and id_tema = %s and estado_pregunta = True", (id_tema,))
            preguntas_desempate = cursor.fetchall()
        random.shuffle(preguntas_desempate)
        for i in range (0,2):
            lista_preguntas_desempate.append(preguntas_desempate.pop())
        return lista_preguntas_desempate

    def devolver_all_ronda (self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'M' and estado_pregunta = True") 
            preguntas_ronda = cursor.fetchall()
        return preguntas_ronda

    def devolver_all_desempate(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'D' and estado_pregunta = True")
            preguntas_desempate = cursor.fetchall()
        return preguntas_desempate

    ################################ CREAR ####################################
    def agregar_pregunta_ronda(self, enunciado, opcion_a, opcion_b, opcion_c,opcion_d, opcion_correcta, id_tema):
        with self.__bd.cursor() as cursor:
                query = """
                    INSERT INTO preguntas (enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta,estado_pregunta, id_tema)
                    VALUES (%s, %s, %s, %s, %s, %s, 'M', 'True', %s)
                """
                cursor.execute(query, (enunciado,opcion_a,opcion_b,opcion_c,opcion_d,opcion_correcta,id_tema))
                cursor.connection.commit()

    def agregar_pregunta_desempate (self,enunciado, opcion_correcta, id_tema):
        with self.__bd.cursor() as cursor:
            query = """
                 INSERT INTO preguntas (enunciado_pregunta,rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta,estado_pregunta, id_tema)
                 VALUES (%s, 'null', 'null', 'null', 'null', %s, 'D', 'True %s)
                 """
            cursor.execute(query, (enunciado, opcion_correcta,id_tema))
            cursor.connection.commit()


    ################################ ACTUALIZAR ####################################
    def actualizar_pregunta_ronda(self, enunciado, opcion_a, opcion_b, opcion_c,opcion_d, opcion_correcta, id_pregunta):
        with self.__bd.cursor() as cursor:
                query = """
                    UPDATE preguntas SET enunciado_pregunta = %s, rta_a = %s, rta_b = %s, rta_c = %s, rta_d = %s, rta_correcta = %s
                    WHERE id_pregunta = %s and tipo_pregunta = 'M'
                """
                cursor.execute(query, (enunciado,opcion_a,opcion_b,opcion_c,opcion_d,opcion_correcta,id_pregunta
                ))
                cursor.connection.commit()

    def actualizar_pregunta_desempate(self, enunciado, rta_correcta, id_pregunta):
        with self.__bd.cursor() as cursor:
                query = """
                    UPDATE preguntas SET enunciado_pregunta = %s, rta_correcta = %s
                    WHERE id_pregunta = %s and tipo_pregunta = 'D'
                """
                cursor.execute(query, (
                    enunciado,rta_correcta,id_pregunta
                ))
                cursor.connection.commit()

    ################################ ELIMINAR ####################################
    def borrar_pregunta(self, id_pregunta):
        with self.__bd.cursor() as cursor:
            cursor.execute("UPDATE preguntas SET estado_pregunta = FALSE WHERE id_pregunta = %s", (id_pregunta,))
            cursor.connection.commit()


####################################################################################################################################################################################

#La clase RealDictCursor es una subclase de cursor proporcionada por psycopg2, una librería de Python para interactuar con bases de datos PostgreSQL.
#Esta clase permite que los resultados de las consultas se devuelvan como diccionarios en lugar de tuplas, 
#lo que puede hacer que el acceso a los datos sea más intuitivo.

#La función isinstance en Python se utiliza para verificar si un objeto es una instancia de una clase o de una tupla de clases.
#  Esto es útil cuando quieres asegurarte de que una variable o un objeto es del tipo que esperas antes de realizar ciertas operaciones sobre él
