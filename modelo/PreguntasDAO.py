import psycopg2
from .bd import Database
import hashlib

class PreguntasDAO:
    def __init__(self):
        self.__bd = Database()
    

    def get_all_preguntas(self):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * FROM preguntas")
            return cursor.fetchall()

    def get_pregunta(self, id_pregunta):
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT * FROM preguntas WHERE id_pregunta = %s", (id_pregunta,))
            return cursor.fetchone()

    def agregar_pregunta(self, pregunta): #ID PREGUNTA TIENE QUE SER AUTO INCREMENTAL, pregunta que entra como parametro es un objeto tipo pregunta
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """INSERT INTO preguntas (enunciado_pregunta, rta_a, rta_b, rta_c, rta_d, rta_correcta, tipo_pregunta, estado_pregunta, id_tema_pregunta) 
                VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)""",
                (pregunta.get_enunciado_pregunta(), pregunta.get_rta_a(), pregunta.get_rta_b(), pregunta.get_rta_c(), pregunta.get_rta_d(), pregunta.get_rta_correcta(), pregunta.get_tipo_pregunta(), pregunta.get_estado_pregunta(), pregunta.get_id_tema_pregunta())
            )
            indice_preg = cursor.execute ("SELECT MAX(id_pregunta) FROM preguntas ") #selecciona el maximo indice
            pregunta.set_id_pregunta (int(indice_preg)) #esto lo que hace es incrementar el indice porque los id son tipo serial
            self.__bd.commit()

    def actualizar_pregunta(self, pregunta):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                """UPDATE preguntas SET enunciado_pregunta = %s, rta_a = %s, rta_b = %s, rta_c = %s, rta_d = %s, rta_correcta = %s, tipo_pregunta = %s, estado_pregunta = %s , id_tema_pregunta = %s 
                WHERE id_pregunta = %s""",
                (pregunta.get_enunciado_pregunta(), pregunta.get_rta_a(), pregunta.get_rta_b(), pregunta.get_rta_c(), pregunta.get_rta_d(), pregunta.get_rta_correcta(), pregunta.get_tipo_pregunta(), pregunta.get_estado_pregunta(), pregunta.get_id_tema_pregunta(), pregunta.get_id_pregunta())
            )
            
            self.__bd.commit()

    def borrar_pregunta(self, id_pregunta):
        with self.__bd.cursor() as cursor:
            cursor.execute("UPDATE preguntas SET estado_pregunta FALSE WHERE id_pregunta = %s", (id_pregunta,))
            self.__bd.commit()
