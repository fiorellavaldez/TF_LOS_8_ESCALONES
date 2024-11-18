from  modelo.PreguntasDAO import PreguntaDAO
from modelo.Pregunta import Pregunta
from modelo.preguntaDesempate import preguntaDesempate
from modelo.preguntaRonda import preguntaRonda
#REVISAR
class PreguntaABM:
    def __init__(self):
        #self.__lista_temas = TemasDAO().get_all_temas()
        self.__lista_preguntas_ronda = self.obtener_preguntas_ronda()
        self.__lista_preguntas_desempate = self.obtener_preguntas_desempate()
    
    @property
    def lista_preguntas_ronda(self):
        return self.__lista_preguntas_ronda
    
    @property
    def lista_preguntas_desempate(self):
        return self.__lista_preguntas_desempate
    
    def obtener_preguntas_ronda(self):
        lista=PreguntaDAO().devolver_all_ronda()   
        lista_preguntas=[]
        for id_pregunta, enunciado, rta_a, rta_b, rta_c, rta_d, rta_correcta, _, _, id_tema in lista:
            preg = preguntaRonda(id_tema,enunciado,rta_a, rta_b, rta_c, rta_d, rta_correcta) #en teoria estoy ignorando los campos que no necesito para crear la pregunta
            preg.set_idPregunta(id_pregunta)
            lista_preguntas.append(preg)
        return lista_preguntas

    def obtener_preguntas_desempate(self):
        lista=PreguntaDAO().devolver_all_desempate
        lista_preguntas= []
        for id_pregunta, enunciado, _, _, _, _, rta_correcta, _, _, id_tema in lista:
            preg = preguntaDesempate(id_tema,enunciado, rta_correcta)
            preg.set_idPregunta(id_pregunta)
        lista_preguntas.append(preg) #en teoria estoy ignorando los campos que no necesito para crear la pregunta
        return lista_preguntas # Lista de objetos pregunta

    def preguntas_ronda_tema(self, id_tema):
        lista=PreguntaDAO().devolver_preg_ronda(id_tema)    
        lista_preguntas=[]
        for id_pregunta, enunciado, rta_a, rta_b, rta_c, rta_d, rta_correcta, _, _, id_tema in lista:
            preg = preguntaRonda(id_tema,enunciado,rta_a, rta_b, rta_c, rta_d, rta_correcta) #en teoria estoy ignorando los campos que no necesito para crear la pregunta
            preg.set_idPregunta(id_pregunta)
            lista_preguntas.append(preg)
                                     
        return lista_preguntas # Lista de objetos pregunta
    
    def preguntas_desempate_tema(self, id_tema):
        lista=PreguntaDAO().devolver_pregunta_desempate(id_tema)
        lista_preguntas= []
        for id_pregunta, enunciado, _, _, _, _, rta_correcta, _, _, id_tema in lista:
            preg = preguntaDesempate(id_tema,enunciado, rta_correcta)
            preg.set_idPregunta(id_pregunta)
        lista_preguntas.append(preg) #en teoria estoy ignorando los campos que no necesito para crear la pregunta
        return lista_preguntas # Lista de objetos pregunta


    def actualizar_preguntas_ronda(self, pregunta:preguntaRonda):
        for p in range(0,len(self.lista_preguntas_ronda)):
            if self.lista_preguntas_ronda[p].get_idPregunta() == pregunta.get_idPregunta():
                self.lista_preguntas_ronda[p].set_enunciado(pregunta.get_enunciado())
                self.lista_preguntas_ronda[p].set_opcionA(pregunta.get_opcionA())
                self.lista_preguntas_ronda[p].set_opcionB(pregunta.get_opcionB())
                self.lista_preguntas_ronda[p].set_opcionC(pregunta.get_opcionC())
                self.lista_preguntas_ronda[p].set_opcionD(pregunta.get_opcionD())
                self.lista_preguntas_ronda[p].set_opcionCorrecta(pregunta.get_opcionCorrecta())
        PreguntaDAO().actualizar_pregunta_ronda(pregunta.get_enunciado(),pregunta.get_opcionA(),pregunta.get_opcionB(),pregunta.get_opcionC(),pregunta.get_opcionD()
                                                ,pregunta.get_opcionCorrecta(),pregunta.get_idPregunta())

            
    def actualizar_preguntas_desempate(self, pregunta:preguntaDesempate):
        for p in range(0,len(self.__lista_preguntas_desempate)):
            if self.lista_preguntas_desempate[p].get_idPregunta() == pregunta.get_idPregunta():
                self.lista_preguntas_desempate[p].set_enunciado(pregunta.get_enunciado())
                self.lista_preguntas_desempate[p].set_respuestaCorrecta(pregunta.get_respuestaCorrecta())
        PreguntaDAO().actualizar_pregunta_desempate(pregunta.get_enunciado(),pregunta.get_respuestaCorrecta(),pregunta.get_idPregunta())
           
    

    def agregar_pregunta_ronda(self, pregunta: preguntaRonda):
        self.__lista_preguntas_ronda.append(pregunta)
        PreguntaDAO().agregar_pregunta_ronda(pregunta.get_enunciado(),pregunta.get_opcionA(), pregunta.get_opcionB(), pregunta.get_opcionC(),
                                             pregunta.get_opcionD(), pregunta.get_opcionCorrecta(), pregunta.get_idtema())     
 

    def agregar_pregunta_desempate(self, pregunta: preguntaDesempate):
        self.__lista_preguntas_desempate.append(pregunta)
        PreguntaDAO().agregar_pregunta_desempate(pregunta.get_enunciado(), pregunta.get_respuestaCorrecta(), pregunta.get_idtema())
    


    def quitar_pregunta_ronda(self, pregunta: preguntaRonda):
        for p in self.lista_preguntas_ronda:
            if p.get_idPregunta() == pregunta.get_idPregunta():
                 PreguntaDAO().borrar_pregunta(pregunta.get_idPregunta())


    def quitar_pregunta_ronda(self, pregunta: preguntaDesempate):
        for p in self.lista_preguntas_desempate:
            if p.get_idPregunta() == pregunta.get_idPregunta():
               PreguntaDAO().borrar_pregunta(pregunta.get_idPregunta())