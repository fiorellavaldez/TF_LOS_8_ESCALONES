import psycopg2
from psycopg2.extras import RealDictCursor
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
            cursor.execute("SELECT * FROM preguntas")
            return cursor.fetchall()

    def get_pregunta(self, id_pregunta):
        with self.__bd.cursor() as cursor:
            query = "SELECT * FROM preguntas WHERE id_pregunta = %s"
            cursor.execute(query, (id_pregunta,))
            result = cursor.fetchone()
            if result:
                if result['tipo_pregunta'] == 'Ronda':
                    pregunta = preguntaRonda(
                        pregunta.set_idtema(result['id_tema_pregunta']),
                        pregunta.set_enunciado(result['enunciado_pregunta']),
                        pregunta.set_opcionA(result['rta_a']),
                        pregunta.set_opcionB(result['rta_b']),
                        pregunta.set_opcionC(result['rta_c']),
                        pregunta.set_opcionD(result['rta_d']),
                        pregunta.set_opcionCorrecta(result['rta_correcta'])
                    )
                else:
                    pregunta = preguntaDesempate(
                        pregunta.set_idtema(result['id_tema_pregunta']),
                        pregunta.set_enunciado(result['enunciado_pregunta']),
                        pregunta.set_respuestaCorrecta(result['rta_correcta'])
                        
                    )
                
                return pregunta
            return None

    def devolver_preg_ronda (self, id_tema): #Ver si se usa
        lista_preguntas_ronda = []
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'M' and id_tema= %s", (id_tema,))
            preguntas_ronda = cursor.fetchall()
        random.shuffle(preguntas_ronda)
        for i in range (0,19):
            lista_preguntas_ronda.append(preguntas_ronda.pop())
        
    def devolver_pregunta_desempate (self, id_tema): #Ver si se usa
        lista_preguntas_desempate = []
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'D' and id_tema = %s", (id_tema,))
            preguntas_desempate = cursor.fetchall()
        random.shuffle(preguntas_desempate)
        for i in range (0,4):
            lista_preguntas_desempate.append(preguntas_desempate.pop())

    def devolver_all_ronda (self, id_tema):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'M' and id_tema= %s", (id_tema,))
            preguntas_ronda = cursor.fetchall()
        return preguntas_ronda

    def devolver_all_desempate(self, id_tema):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * from PREGUNTAS WHERE tipo_pregunta = 'D' and id_tema = %s", (id_tema,))
            preguntas_desempate = cursor.fetchall()
        return preguntas_desempate

    ################################ CREAR ####################################
    def agregar_pregunta(self, pregunta):
        with self.__bd.cursor() as cursor:
            if isinstance(pregunta, preguntaRonda):
                query = """
                    INSERT INTO preguntas (enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema)
                    VALUES (%s, %s, %s, %s, %s, %s, 'Ronda', %s, %s) RETURNING id_pregunta
                """
                cursor.execute(query, (
                    pregunta.get_enunciado(),
                    pregunta.get_opcionA(),
                    pregunta.get_opcionB(),
                    pregunta.get_opcionC(),
                    pregunta.get_opcionD(),
                    pregunta.get_opcionCorrecta(),
                    pregunta.get_estado(),
                    pregunta.get_idtema()
                ))
            elif isinstance(pregunta, preguntaDesempate):
                query = """
                    INSERT INTO preguntas (enunciado_pregunta, rta_correcta, tipo_pregunta, estado_pregunta, id_tema)
                    VALUES (%s, %s, 'Desempate', %s, %s) RETURNING id_pregunta
                """
                cursor.execute(query, (
                    pregunta.get_enunciado(),
                    pregunta.get_respuestaCorrecta(),
                    pregunta.get_estado(),
                    pregunta.get_idtema()
                ))
            cursor.connection.commit()
            return cursor.fetchone()[0]

    ################################ ACTUALIZAR ####################################
    def actualizar_pregunta(self, id_pregunta, pregunta):
        with self.__bd.cursor() as cursor:
            if isinstance(pregunta, preguntaRonda):
                query = """
                    UPDATE preguntas SET enunciado_pregunta = %s, rta_a = %s, rta_b = %s, rta_c = %s, rta_d = %s, rta_correcta = %s, estado_pregunta = %s, id_tema_pregunta = %s
                    WHERE id_pregunta = %s
                """
                cursor.execute(query, (
                    pregunta.get_enunciado(),
                    pregunta.get_opcionA(),
                    pregunta.get_opcionB(),
                    pregunta.get_opcionC(),
                    pregunta.get_opcionD(),
                    pregunta.get_opcionCorrecta(),
                    pregunta.get_estado(),
                    pregunta.get_idtema(),
                    id_pregunta
                ))
            elif isinstance(pregunta, preguntaDesempate):
                query = """
                    UPDATE preguntas SET enunciado_pregunta = %s, rta_correcta = %s, estado_pregunta = %s, id_tema_pregunta = %s
                    WHERE id_pregunta = %s
                """
                cursor.execute(query, (
                    pregunta.get_enunciado(),
                    pregunta.get_respuestaCorrecta(),
                   pregunta.get_estado(),
                    pregunta.get_idtema(),
                    id_pregunta
                ))
            cursor.connection.commit()

    ################################ ELIMINAR ####################################
    def borrar_pregunta(self, id_pregunta):
        with self.__bd.cursor() as cursor:
            cursor.execute("UPDATE preguntas SET estado_pregunta FALSE WHERE id_pregunta = %s", (id_pregunta,))
            cursor.connection.commit()


####################################################################################################################################################################################

#La clase RealDictCursor es una subclase de cursor proporcionada por psycopg2, una librería de Python para interactuar con bases de datos PostgreSQL.
#Esta clase permite que los resultados de las consultas se devuelvan como diccionarios en lugar de tuplas, 
#lo que puede hacer que el acceso a los datos sea más intuitivo.

#La función isinstance en Python se utiliza para verificar si un objeto es una instancia de una clase o de una tupla de clases.
#  Esto es útil cuando quieres asegurarte de que una variable o un objeto es del tipo que esperas antes de realizar ciertas operaciones sobre él
