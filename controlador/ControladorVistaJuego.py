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
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores_widget) #le paso widgets
        self.asignar_temas(self.__lista_escalones)
        self.MainWindow.show()
        
        self.__vista.get_button_atras().clicked.connect(self.__atras)
        self.__vista.get_comenzar_partida().clicked.connect(self.iniciar_partida)

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
    
    def asignar_temas(self,escalones):
        Qlabels = self.__vista.get_lista_escalones()
        esc = escalones
        for i in range(8):
            Qlabels[i].setText(escalones[i].get_tema().get_nombreTema().upper())

    def __devolver_escalones(self,lista_temas):
        escalones = []
        for tema in lista_temas:
            #nombre_tema = tema.get_nombreTema()
            lista_preguntas_ronda = PreguntaABM().preguntas_ronda_tema(tema.get_idTema())
            lista_preguntas_desempate = PreguntaABM().preguntas_desempate_tema(tema.get_idTema())
            escalones.append(Escalon(tema,lista_preguntas_ronda,lista_preguntas_desempate))
        return escalones
    
    def agrego_jugadores_layout (self, jugadores):
        
        match len(jugadores):
            case 9:
                for i in self.__lista_jugadores_widget: #esta lista debe variar
                    self.__vista.ly_escalon1.addWidget(i)
                    print("los añadi al layout escalon 1!!!!")
            case 8:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon2.addWidget(i)
            case 7:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon3.addWidget(i)
            case 6:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon4.addWidget(i)
            case 5:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon5.addWidget(i)
            case 4:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon6.addWidget(i)
            case 3:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon7.addWidget(i)
            case 2:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon8.addWidget(i)
            case 1:
                for i in self.__lista_jugadores_widget:
                    self.__vista.ly_escalon8.addWidget(i)
    
    def iniciar_partida(self):
        lista_suben = []
        nro=0
        for i in self.__lista_escalones:
            self.__lista_escalones[nro].set_jugadores(self.__lista_jugadores)
            jugadores = i.get_jugadores()
            for i in jugadores: #Lista de jugadores logicos del escalon
                if self.comparo(i) == True:
                    lista_suben.append(i)
            self.agrego_jugadores_layout(lista_suben)
            nro += 1


    def comparo(self, jugador): #nombre jugador con lista widget #UNO SOLO
        for i in self.__lista_jugadores_widget:
            if jugador.get_nombre_jugador() == i.get_nombre_visual():
                i.setParent(None) #Le saco el parent
                print("sin parent!")
                return True
            else:        
                return False
                #asignarle un nuevo layout y antes verificar en que escalon esta



 
    # def hacer_pregunta(jugador, preguntas):
    # # Aquí puedes hacer la lógica para elegir una pregunta y obtener una respuesta del jugador
    # # Por ahora, simulamos respuestas aleatorias:
    # import random
    # resultado = random.choice([1, 2])  # 1: acertó, 2: falló
    # print(f"{jugador.get_nombre_jugador()} responde {'bien' if resultado == 1 else 'mal'} en la ronda.")
    # return resultado