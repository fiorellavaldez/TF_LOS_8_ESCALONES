from vista.VistaJuego import Ui_MainWindow
from vista.VistaPreguntaRonda import VistaPreguntaRonda
from PyQt6 import QtWidgets
#from modelo.TemasDAO import TemasDAO
from modelo.Escalon import Escalon
from vista.WidgetJugador import WidgetJugador
#from modelo.PreguntasDAO import PreguntaDAO
from modelo.Tema import Tema
from modelo.preguntaRonda import preguntaRonda
from modelo.preguntaDesempate import preguntaDesempate
from modelo.Jugador import Jugador
from modelo.TemaABM import TemaABM
from modelo.PreguntasABM import PreguntaABM

class ControladorVistaJuego:

    def __init__(self, controlador_anterior, lista_jugadores):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()  # Nueva ventana para la nueva partida
        self.__vista = Ui_MainWindow() #Aca se crea la vista 
        self.__temas = TemasDAO()
        self.__lista_temas = self.__temas.temas_partida() #trae 8 temas ya mezclados
        self.__escalon1 = Escalon(1)
        self.__lista_jugadores_widget = []
        self.__lista = lista_jugadores
        self.__asignar_jugadores(self.__escalon1)
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores_widget)
        self.__asignar_temas() #¿le pasamos la lista por parámetro?
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__atras)

    def __atras(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def __obtener_pregunta(self): #pasarlo a una vista y la llamamos acá
        vista_pregunta = VistaPreguntaRonda()
        vista_pregunta.exec()

    def setRespuestaCorrecta(self, boton):
        pass

    def __asignar_temas(self):
        lista_qlabels = []
        lista_qlabels = self.__vista.lista_nombres_escalon
        for i in range(0,8):
            lista_qlabels[i].setText((self.__lista_temas[i][1]).upper())

    def __asignar_jugadores(self, escalon): #Acá asigno al escalon
        self.__convertir_widget()
        # for i in self.__lista:
        #     layout.addWidget(i)
        escalon.set_jugadores(self.__lista)
        self.__escalon1.set_jugadores(self.__lista)

    def __convertir_widget(self, lista):
        for i in lista:
            self.__lista_jugadores_widget.append(WidgetJugador((i)[1],(i)[2]))
            #self.__vista.ly_escalon1.addWidget(self.__lista_jugadores_widget(i))
            
    # def agregar_ly1 (self):
    #     for i in self.__lista_jugadores_widget:
    #         self.__vista.ly_escalon1.addWidget(i)

    def devolver_objetos_tema(self):  #este lo podemos usar sin que sea un metodo y lo pasamos al constructor
        lista_temas = TemaABM().obtener_temas()
        return lista_temas

    def devolver_objetos_pregunta_ronda(self,id_tema):
        lista_preguntas_ronda = PreguntaABM()
        return lista_preguntas_ronda_partida

    def devolver_objetos_pregunta_desempate(self,id_tema):
        lista_preguntas_desempate = PreguntaDAO().devolver_preg_ronda (id_tema)
        lista_preguntas_desempate_partida = []
        for fila in lista_preguntas_desempate:
            enunciado = fila[1]
            resp_correcta = fila[6]
            lista_preguntas_desempate_partida.append(preguntaDesempate(id_tema,enunciado,resp_correcta))
        return lista_preguntas_desempate_partida

    def devolver_jugadores(self):
        lista_jugadores= self.__lista
        lista_jugadores_partida=[]
        for fila in lista_jugadores:
            nombre = fila[1]
            avatar = fila[2]
            lista_jugadores_partida.append(Jugador(nombre,avatar))
        return lista_jugadores_partida
    
    def __devolver_escalones(self,lista_temas_partida):
        escalones = []
        for i in range(1,8):
            tema = lista_temas_partida[i]
            nombre_tema = tema.get_nombreTema()
            lista_preguntas_ronda = self.devolver_objetos_pregunta_ronda(tema.get_idTema())
            lista_preguntas_desempate = self.devolver_objetos_pregunta_desempate(tema.get_idTema())
            escalones.append(Escalon(nombre_tema,lista_preguntas_ronda,lista_preguntas_desempate))
            #acá convertir a widget
        return escalones

    # def hacer_pregunta(jugador, preguntas):
    # # Aquí puedes hacer la lógica para elegir una pregunta y obtener una respuesta del jugador
    # # Por ahora, simulamos respuestas aleatorias:
    # import random
    # resultado = random.choice([1, 2])  # 1: acertó, 2: falló
    # print(f"{jugador.get_nombre_jugador()} responde {'bien' if resultado == 1 else 'mal'} en la ronda.")
    # return resultado