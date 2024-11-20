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
            lista_preguntas_ronda = PreguntaABM().preguntas_ronda_tema(tema.get_idTema())#obtengo una lista de preguntas para la ronda relacionada con el tema:
            lista_preguntas_desempate = PreguntaABM().preguntas_desempate_tema(tema.get_idTema())#obtengo una lista de preguntas desempate
            escalones.append(Escalon(tema,lista_preguntas_ronda,lista_preguntas_desempate))#creo un nuevo escalon con el tema y las preguntas y los agg a la lista:
        return escalones
    
    def agrego_jugadores_layout (self, jugadores):
        
        match len(jugadores):#evaluo el num de jugadores
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
        nro=0
        lista_restantes = self.__lista_jugadores #Todos los jugadores al inicio
        for escalon in self.__lista_escalones:
            lista_suben = [] #los que avanzan al prox escalon
            perdedor = None #si no hago esto me sale error
            #separo ganadores y perdedor (lógica)

            for jugador in lista_restantes: #Lista de jugadores logicos del escalon
                if perdedor in None and not self.comparo(jugador): #Evaluo si el jugador avanza
                    perdedor = jugador
                else:
                    lista_suben.append(jugador)
        
        if perdedor is None:
            print("No se encontró un perdedor en este escalon")
            ####Esto es solo para verificar que funciona ### Despues se saca
        
            self.actualizar_layout_escalon(escalon, lista_suben, perdedor, nro)#actualizo layout visual del escalon actual
            lista_restantes = lista_suben
            nro += 1

    def actualizar_layout_escalon(self, escalon, lista_ganadores, perdedor, nro):
        layout_actual = getattr(self.__vista,f"ly_escalon{nro + 1}") #obtengo el actual
        layout_siguiente = getattr(self.__vista, f"ly_escalon{nro + 2}", None)
        ## getattr asegura que los layouts se manejan dinámicamente ##
        widget_perdedor = self.obtener_widget_por_jugador(perdedor)
        if perdedor:
            widget_perdedor = self.obtener_widget_por_jugador(perdedor)
            if widget_perdedor:
                layout_actual.addWidget(widget_perdedor)
            #jugador perdedor permanece en el layout actual
                print(f"{perdedor.get_nombre_jugador()} permanece en el escalon {nro + 1}")
        
        if layout_siguiente:
            for ganador in lista_ganadores:
                widget_ganador = self.obtener_widget_por_jugador(ganador)
                layout_siguiente.addWidget(widget_ganador)
                print(f"{ganador.get_nombre_jugador()} avanza al escalon {nro + 2}")

    def obtener_widget_por_jugador(self, jugador):
        for widget in self.__lista_jugadores_widget:
            if widget.get_nombre_visual() == jugador.get_nombre_jugador():
                return widget
        return None #si no se encuentra retorna none


    def comparo(self, jugador): #nombre jugador con lista widget #UNO SOLO
        for i in self.__lista_jugadores_widget:
            print(f"Comparando {jugador} con {i.get_nombre_visual()}")
            if isinstance(jugador, str): #si jugador es un string
                if jugador.get_nombre_jugador() == i.get_nombre_visual():
                    i.setParent(None) #Elimina el widget de su layout actual(sin el padre visual)
                    print("sin parent!")
                    return True
                else:        
                    return False
            elif hasattr(jugador, 'get_nombre_jugador'):#si es un objeto con el metodo
                if jugador.get_nombre_jugador() == i.get_nombre_visual():
                    i.setParent(None)
                    print("sin parent")
                    return True
        return False
                #asignarle un nuevo layout y antes verificar en que escalon esta
    # def comparo(self, jugador):
    #     for i in self.__lista_jugadores_widget:
    #         print(f"Comparando {jugador} con {i.get_nombre_visual()}")
    #         if hasattr(jugador, 'get_nombre_jugador'):
    #             print(f"Nombre del jugador lógico: {jugador.get_nombre_jugador()}")
    #         else:
    #             print("Jugador no tiene el método 'get_nombre_jugador'")

    #         # Comparación ajustada
    #         if isinstance(jugador, str) and jugador == i.get_nombre_visual():
    #             i.setParent(None)
    #             print("¡Sin parent!")
    #             return True
    #         elif hasattr(jugador, 'get_nombre_jugador') and jugador.get_nombre_jugador() == i.get_nombre_visual():
    #             i.setParent(None)
    #             print("¡Sin parent!")
    #             return True
    #     return False




    # def hacer_pregunta(jugador, preguntas):
    # # Aquí puedes hacer la lógica para elegir una pregunta y obtener una respuesta del jugador
    # # Por ahora, simulamos respuestas aleatorias:
    # import random
    # resultado = random.choice([1, 2])  # 1: acertó, 2: falló
    # print(f"{jugador.get_nombre_jugador()} responde {'bien' if resultado == 1 else 'mal'} en la ronda.")
    # return resultado