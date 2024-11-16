import psycopg2
from psycopg2.extras import RealDictCursor
from Pregunta import Pregunta, preguntaRonda, preguntaDesempate
from .bd import Database
# preguntas distinguiendo entre preguntas de ronda y desempate
class PreguntaDAO:
    def __init__(self):
        self.__bd = Database()
    
    def get_pregunta(self, id_pregunta):
        with self.__bd.cursor(cursor_factory=RealDictCursor) as cursor:
            query = "SELECT * FROM preguntas WHERE id_pregunta = %s"
            cursor.execute(query, (id_pregunta,))
            result = cursor.fetchone()
            if result:
                if result['tipo_pregunta'] == 'Ronda':
                    pregunta = preguntaRonda(
                        tema=result['id_tema_pregunta'],
                        enunciado=result['enunciado_pregunta'],
                        opcionA=result['rta_a'],
                        opcionB=result['rta_b'],
                        opcionC=result['rta_c'],
                        opcionD=result['rta_d'],
                        opcionCorrecta=result['rta_correcta']
                    )
                else:
                    pregunta = preguntaDesempate(
                        tema=result['id_tema_pregunta'],
                        enunciado=result['enunciado_pregunta'],
                        respuestaCorrecta=result['rta_correcta']
                    )
                pregunta.estado = result['estado_pregunta']
                return pregunta
            return None

    def agregar_pregunta(self, pregunta):
        with self.__bd.cursor() as cursor:
            if isinstance(pregunta, preguntaRonda):
                query = """
                    INSERT INTO preguntas (enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema_pregunta)
                    VALUES (%s, %s, %s, %s, %s, %s, 'Ronda', %s, %s) RETURNING id_pregunta
                """
                cursor.execute(query, (
                    pregunta.get_enunciado(),
                    pregunta.get_opcionA(),
                    pregunta.get_opcionB(),
                    pregunta.get_opcionC(),
                    pregunta.get_opcionD(),
                    pregunta.get_opcionCorrecta(),
                    pregunta.get_estado_pregunta(),
                    pregunta.get_id_tema_pregunta()
                ))
            elif isinstance(pregunta, preguntaDesempate):
                query = """
                    INSERT INTO preguntas (enunciado_pregunta, rta_correcta, tipo_pregunta, estado_pregunta, id_tema_pregunta)
                    VALUES (%s, %s, 'Desempate', %s, %s) RETURNING id_pregunta
                """
                cursor.execute(query, (
                    pregunta.get_enunciado(),
                    pregunta.get_respuestaCorrecta(),
                    pregunta.get_estado_pregunta(),
                    pregunta.get_id_tema_pregunta()
                ))
            self.__bd.commit()
            return cursor.fetchone()[0]

#    def actualizar_pregunta(self, id_pregunta, pregunta):
#        with self.__bd.cursor() as cursor:
#            if isinstance(pregunta, preguntaRonda):
#               query = """
#                    UPDATE preguntas SET enunciado_pregunta = %s, rta_a = %s, rta_b = %s, rta_c = %s, rta_d = %s, rta_correcta = %s, estado_pregunta = %s, id_tema_pregunta = %s
#                    WHERE id_pregunta = %s
#                """
#                cursor.execute(query, (
#                    pregunta.get_enunciado(),
#                    pregunta.get_opcionA(),
#                    pregunta.get_opcionB(),
#                    pregunta.get_opcionC(),
#                    pregunta.get_opcionD(),
#                    pregunta.get_opcionCorrecta(),
#                    pregunta.get_estado_pregunta(),
#                    pregunta.get_id_tema_pregunta(),
#                    id_pregunta
#                ))
#            elif isinstance(pregunta, preguntaDesempate):
#                query = """
#                    UPDATE preguntas SET enunciado_pregunta = %s, rta_correcta = %s, estado_pregunta = %s, id_tema_pregunta = %s
#                    WHERE id_pregunta = %s
#                """
#                cursor.execute(query, (
#                    pregunta.get_enunciado(),
#                    pregunta.get_respuestaCorrecta(),
#                   pregunta.get_estado_pregunta(),
#                    pregunta.get_id_tema_pregunta(),
#                    id_pregunta
#                ))
#            self.__bd.commit()

    def borrar_pregunta(self, id_pregunta):
        with self.__bd.cursor() as cursor:
            query = "DELETE FROM preguntas WHERE id_pregunta = %s"
            cursor.execute(query, (id_pregunta,))
            self.__bd.commit()


#La clase RealDictCursor es una subclase de cursor proporcionada por psycopg2, una librería de Python para interactuar con bases de datos PostgreSQL.
#Esta clase permite que los resultados de las consultas se devuelvan como diccionarios en lugar de tuplas, 
#lo que puede hacer que el acceso a los datos sea más intuitivo.

#La función isinstance en Python se utiliza para verificar si un objeto es una instancia de una clase o de una tupla de clases.
#  Esto es útil cuando quieres asegurarte de que una variable o un objeto es del tipo que esperas antes de realizar ciertas operaciones sobre él
