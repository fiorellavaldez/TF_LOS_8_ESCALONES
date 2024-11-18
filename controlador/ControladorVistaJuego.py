from vista.VistaJuego import Ui_MainWindow
from vista.VistaPreguntaRonda import VistaPreguntaRonda
from PyQt6 import QtWidgets
from modelo.Escalon import Escalon
from vista.WidgetJugador import WidgetJugador
from modelo.Jugador import Jugador
from modelo.TemaABM import TemaABM
from modelo.PreguntasABM import PreguntaABM

class ControladorVistaJuego:

    def __init__(self, controlador_anterior, lista_jugadores):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__lista_jugadores = self.__convertir_obj_jugador(lista_jugadores)
        self.__lista_jugadores_widget = self.__convertir_widget(self.__lista_jugadores)
        self.__lista_escalones = self.__devolver_escalones(self.devolver_objetos_tema()) #TemaABM().lista_temas
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores_widget)
        self.asignar_temas(self.__lista_escalones)
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__atras)

    def __atras(self):
        self.MainWindow.close()
        self.__controlador_anterior.MainWindow.show()

    def __obtener_pregunta(self): #pasarlo a una vista y la llamamos acá
        vista_pregunta = VistaPreguntaRonda() #DIALOG
        vista_pregunta.exec()

    def __convertir_obj_jugador(self, lista_jugadores): #lista_jugadores es una lista de tuplas 
        lista = []
        for i in lista_jugadores:
            lista.append(Jugador((i)[1], (i)[2]))
        return lista

    def __convertir_widget(self, lista_jugadores): #lista_jugadores es una de objetos
        lista = []
        for i in lista_jugadores:
            lista.append(WidgetJugador((i).get_nombre_jugador(),(i).get_avatar()))
        return lista

    def devolver_objetos_tema(self):  #este lo podemos usar sin que sea un metodo y lo pasamos al constructor
        lista_temas = TemaABM().lista_temas
        return lista_temas

    def devolver_objetos_pregunta_ronda(self,id_tema):
        lista_preguntas_ronda = PreguntaABM().devolver_preg_ronda(id_tema)
        return lista_preguntas_ronda

    def devolver_objetos_pregunta_desempate(self,id_tema):
        lista_preguntas_desempate = PreguntaABM().devolver_preg_desempate (id_tema)
        return lista_preguntas_desempate

    # def devolver_jugadores(self):
    #     lista_jugadores= self.__lista
    #     lista_jugadores_partida=[]
    #     for fila in lista_jugadores:
    #         nombre = fila[1]
    #         avatar = fila[2]
    #         lista_jugadores_partida.append(Jugador(nombre,avatar))
    #     return lista_jugadores_partida
    
    def asignar_temas(self,escalones):
        Qlabels = self.__vista.get_lista_escalones()
        esc = escalones
        for i in range(8):
            #print(esc[i].get_tema().get_nombreTema().upper())
            Qlabels[i].setText(escalones[i].get_tema().get_nombreTema().upper())

    def __devolver_escalones(self,lista_temas):
        escalones = []
        for tema in lista_temas:
            #nombre_tema = tema.get_nombreTema()
            lista_preguntas_ronda = PreguntaABM().preguntas_ronda_tema(tema.get_idTema())
            lista_preguntas_desempate = PreguntaABM().preguntas_desempate_tema(tema.get_idTema())
            escalones.append(Escalon(tema,lista_preguntas_ronda,lista_preguntas_desempate))
        return escalones
    


    # def hacer_pregunta(jugador, preguntas):
    # # Aquí puedes hacer la lógica para elegir una pregunta y obtener una respuesta del jugador
    # # Por ahora, simulamos respuestas aleatorias:
    # import random
    # resultado = random.choice([1, 2])  # 1: acertó, 2: falló
    # print(f"{jugador.get_nombre_jugador()} responde {'bien' if resultado == 1 else 'mal'} en la ronda.")
    # return resultado