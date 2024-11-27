import psycopg2
from modelo.bd import Database
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
            cursor.execute("SELECT * FROM temas WHERE estado_tema = True ")
            return cursor.fetchall()

    def get_tema(self, id_tema): 
        with self.__bd.cursor() as cursor:
            cursor.execute(
                "SELECT id_tema, nombre_tema FROM temas WHERE id_tema = %s ", 
                (id_tema,)
                )
            return cursor.fetchone()
        
    def __contar_temas(self): ## cuento la cantidad de temas que hay 
        with self.__bd.cursor() as cursor:
            cursor.execute("SELECT MAX(t.id_tema) FROM temas AS t")
            contador = cursor.fetchone()[0]
        return contador

    #Valido el tema, si tiene 18 o mas preguntas de ronda y 2 o mas preguntas de desempate el tema es valido y se llama en el metodo temas_partida
    #de otro cuando se agreguen temas nuevos sin el minimo de preguntas estos igual podrian ser temas validos para la partida y eso creo que romperia el juego
    def __chequeo_preguntas_necesarias(self, cant_preguntas_tipo1, tipo_pregunta1, cant_preguntas_tipo2, tipo_pregunta2): 
        temas_validos = [] 
        cant_temas = self.__contar_temas() 
        with self.__bd.cursor() as cursor: 
            for i in range(1, cant_temas): # Asegurándote de contar desde 1 hasta cant_temas 
                cursor.execute("""SELECT (SELECT COUNT(p1.id_pregunta) FROM preguntas AS p1 
                                INNER JOIN temas AS t1 ON t1.id_tema = p1.id_tema WHERE p1.id_tema = %s AND p1.tipo_pregunta = %s AND t1.estado_tema = True AND p1.estado_pregunta = True) AS preguntas_m,
                                    (SELECT COUNT(p2.id_pregunta) FROM preguntas AS p2 
                                    INNER JOIN temas AS t2 ON t2.id_tema = p2.id_tema  WHERE p2.id_tema = %s AND p2.tipo_pregunta = %s AND t2.estado_tema = True AND p2.estado_pregunta = True) AS preguntas_d""", 
                            (i, tipo_pregunta1, i, tipo_pregunta2)) 
                preguntas_m, preguntas_d = cursor.fetchone() 
                if preguntas_m >= cant_preguntas_tipo1 and preguntas_d >= cant_preguntas_tipo2:
                    temas_validos.append(self.get_tema(i)) # Añadir el id_tema a la lista de temas válidos return temas_validos
        return temas_validos

    #def temas_partida (self): #Devuelve lista con 8 temas
    #    temas = self.get_all_temas()
    #    lista_temas_partida = []
    #    for i in range (0,8):
    #        random.shuffle(temas) #cambie de lugar el shuffle porque si no te podia devolver mas de una vez un tema de la misma id
    #        lista_temas_partida.append(temas.pop())
    #    return lista_temas_partida    
    
    def temas_partida(self): 
        temas_validos = self.__chequeo_preguntas_necesarias(18, 'M', 3, 'D') 
        random.shuffle(temas_validos) 
        return temas_validos

    ################################ CREAR ####################################
    def agregar_tema(self, tema):
        with self.__bd.cursor() as cursor:
            cursor.execute(
                "INSERT INTO temas (nombre_tema,estado_tema) VALUES (%s,'true')",
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
            cursor.execute(" UPDATE temas SET estado_tema = FALSE WHERE id_tema = %s", (id_tema,))
            #cursor.execute("DELETE FROM temas WHERE id_tema = %s", (id_tema,))
            cursor.connection.commit()