from vista.VistaJuego import Ui_MainWindow
from vista.VistaPreguntaRonda import VistaPreguntaRonda
from vista.VistaPreguntaAproximacion import VistaPreguntaAproximacion
from vista.VistaDialogGanador import VistaDialogGanador
from vista.VistaDialogRonda import DialogRonda
from vista.VistaDialogDesempate import DialogDesempate
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication, QDialog, QLabel, QPushButton
from modelo.Escalon import Escalon
from vista.WidgetJugador import WidgetJugador
from modelo.Jugador import Jugador
from modelo.TemaABM import TemaABM
from modelo.PreguntasABM import PreguntaABM
from controlador.Sonido import Sonido
from controlador.ControladorVideo import ControladorVideo
from controlador.ControladorAudio import ControladorAudio
import random

class ControladorVistaJuego:

    def __init__(self, controlador_anterior, lista_jugadores):
        self.__controlador_anterior = controlador_anterior
        self.MainWindow = QtWidgets.QMainWindow()
        self.__vista = Ui_MainWindow()
        self.__lista_jugadores = self.__convertir_obj_jugador(lista_jugadores)
        #self.__lista_jugadores_widget = self.__convertir_widget(self.__lista_jugadores)
        self.__lista_escalones = self.__devolver_escalones(self.devolver_objetos_tema()) #TemaABM().lista_temas
        self.__lista_jugadores_widget = self.__convertir_widget(self.__lista_jugadores) 
        self.__vista.setupUi(self.MainWindow, self.__lista_jugadores_widget) #le paso widgets
        self.asignar_temas(self.__lista_escalones)
        self.MainWindow.show()
        # Registrar la ventana en el controlador de audio y video
        ControladorVideo.registrar_ventana(self.MainWindow)
        # Inicializa un controlador de audio con una ruta inicial
        self.__audio_controller = ControladorAudio(ruta_inicial="musica\\menu_2.mp3")
        # Cambia la música
        self.__audio_controller.cambiar_musica(r"musica\\acorralado.mp3")
        
        with open("vista/estilos.qss") as f:
            self.MainWindow.setStyleSheet(f.read())
        
        self.__en_partida = False  # Controla si se puede avanzar al siguiente escalón
        self.__nro_escalon_actual = 0  # Índice del escalón actual
        self.__lista_restantes = self.__lista_jugadores  # Jugadores que continúan en el juego
        
        self.__vista.get_button_atras().clicked.connect(self.__atras)
        self.__vista.get_comenzar_partida().clicked.connect(self.__habilitar_jugar)

    def __atras(self):
        self.MainWindow.close()
        audio_controller = ControladorAudio(ruta_inicial="musica\\menu_2.mp3")
        audio_controller.cambiar_musica(r"musica\\menu_2.mp3")
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
        lista_temas = TemaABM().obtener_temas_para_jugar()
        return lista_temas

    def devolver_objetos_pregunta_ronda(self,id_tema):
        lista_preguntas_ronda = PreguntaABM().devolver_preg_ronda(id_tema)
        return lista_preguntas_ronda

    def devolver_objetos_pregunta_desempate(self,id_tema):
        lista_preguntas_desempate = PreguntaABM().devolver_preg_desempate (id_tema)
        return lista_preguntas_desempate
    
    def asignar_temas(self,escalones):
        Qlabels = self.__vista.get_lista_escalones()
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
    
    def __habilitar_jugar(self):
        """
        Habilita el avance al próximo escalón cuando se presiona el botón Jugar.
        """
        if not self.__en_partida and self.__nro_escalon_actual < len(self.__lista_escalones):
            self.__en_partida = True
            self.jugar_escalon()

    def jugar_escalon(self):
        """
        Juega el escalón actual con la lógica definida, y luego espera al botón para avanzar.
        """
        escalon = self.__lista_escalones[self.__nro_escalon_actual]
        print(f"--- Comenzando escalón {self.__nro_escalon_actual + 1} con tema {escalon.get_tema().get_nombreTema()} ---")
        
        # Reinicia los atributos ronda1 y ronda2
        for jugador in self.__lista_restantes:
            jugador.set_ronda1(0)
            jugador.set_ronda2(0)

        # Primera ronda
        posicion=0
        for jugador in self.__lista_restantes:
            preguntas_ronda1= escalon.get_preguntasRonda()
            pregunta_actual= preguntas_ronda1[posicion]
            opciones = [pregunta_actual.get_opcionA(), pregunta_actual.get_opcionB(), pregunta_actual.get_opcionC(), pregunta_actual.get_opcionD()]
            correcta = pregunta_actual.get_opcionCorrecta()
            self.hacer_pregunta(jugador,self.__nro_escalon_actual,escalon.get_tema().get_nombreTema(), pregunta_actual.get_enunciado(), opciones, correcta,ronda=1)
            posicion += 1
        # Segunda ronda
        for jugador in self.__lista_restantes:
            preguntas_ronda2= escalon.get_preguntasRonda()
            pregunta_actual= preguntas_ronda2[posicion]
            opciones = [pregunta_actual.get_opcionA(), pregunta_actual.get_opcionB(), pregunta_actual.get_opcionC(), pregunta_actual.get_opcionD()]
            correcta = pregunta_actual.get_opcionCorrecta()
            self.hacer_pregunta(jugador,self.__nro_escalon_actual,escalon.get_tema().get_nombreTema(), pregunta_actual.get_enunciado(), opciones, correcta,ronda=2)
            posicion += 1
        
        # Evaluar resultados
        jugadores_a_desempatar = self.evaluar_jugadores(self.__lista_restantes)
        
        # Manejar desempates si es necesario
        if len(jugadores_a_desempatar) > 1:
            print("Empate detectado. Comenzando ronda de desempate...")
            preguntas_desempate = escalon.get_preguntasDesempate()
            pregunta_desempate = preguntas_desempate[0]
            perdedor = self.hacer_desempate(jugadores_a_desempatar, pregunta_desempate)
        else:
            perdedor = jugadores_a_desempatar[0]

        # Determinar jugadores que avanzan
        lista_suben = [jugador for jugador in self.__lista_restantes if jugador != perdedor]
        
        if len(lista_suben) == 1:
            jugador_ganador = lista_suben[0]
            widget_jugador_ganador = self.obtener_widget_por_jugador(jugador_ganador)
            dialogo = VistaDialogGanador(jugador=widget_jugador_ganador)
            dialogo.exec()
        
        for jugador in lista_suben:
            jugador_widget = self.obtener_widget_por_jugador(jugador)
            jugador_widget.reset_rondas()

        # Actualizar la vista
        self.actualizar_layout_escalon(escalon, lista_suben, perdedor, self.__nro_escalon_actual)

        # Preparar para el próximo escalón
        self.__lista_restantes = lista_suben
        self.__nro_escalon_actual += 1
        self.__en_partida = False  # Esperar a que el usuario presione "Jugar" nuevamente

    # Otros métodos permanecen sin cambios...
    
    def hacer_pregunta(self, jugador, escalon, tematica, pregunta, respuestas, correcta, ronda=1):
        """
        Hace una pregunta de ronda a un jugador.
        Muestra un diálogo en pantalla para que el jugador seleccione su respuesta.
        Actualiza el estado de la ronda del jugador dependiendo de si la respuesta es correcta o incorrecta.

        :param jugador: Instancia del jugador.
        :param escalon: Número del escalón actual.
        :param tematica: Temática de la pregunta.
        :param pregunta: Texto de la pregunta.
        :param respuestas: Lista de posibles respuestas (4 opciones).
        :param ronda: Número de ronda (1 o 2).
        :return: Índice de la respuesta seleccionada (0-3) o None si el jugador no responde.
        """
        # Crear y configurar la ventana de la pregunta
        dialogo = VistaPreguntaRonda()
        dialogo.actualizar_pregunta(
            jugador=jugador.get_nombre_jugador(),  # Suponiendo que 'jugador' tiene un atributo 'nombre'
            escalon=escalon+1,
            tematica=tematica,
            ronda_actual=ronda,
            pregunta=pregunta,
            respuestas=respuestas
        )

        # Mostrar el diálogo y esperar la respuesta
        resultado = dialogo.exec()
        if resultado:  # Si el jugador selecciona una respuesta
            jugador_widget = self.obtener_widget_por_jugador(jugador)
            respuesta_seleccionada = resultado  # Ajustar índice (1-4 a 0-3)
            print(f"{jugador.get_nombre_jugador()} seleccionó la respuesta {chr(64 + respuesta_seleccionada)}: {respuestas[respuesta_seleccionada-1]}")
            
            # Verificar si la respuesta es correcta
            if respuesta_seleccionada == (ord(correcta.upper())-64): #es para la posicion ASCII de las letras ABCD
                if ronda == 1:
                    jugador.set_ronda1(1)  # Respuesta correcta en la ronda 1
                    jugador_widget.actualizar_r1(estado=True)
                elif ronda == 2:
                    jugador.set_ronda2(1)  # Respuesta correcta en la ronda 2
                    jugador_widget.actualizar_r2(estado=True)
                print(f"{jugador.get_nombre_jugador()} ha respondido correctamente.")
            else:
                if ronda == 1:
                    jugador.set_ronda1(2)  # Respuesta incorrecta en la ronda 1
                    jugador_widget.actualizar_r1(estado=False)
                elif ronda == 2:
                    jugador.set_ronda2(2)  # Respuesta incorrecta en la ronda 2
                    jugador_widget.actualizar_r2(estado=False)
                print(f"{jugador.get_nombre_jugador()} ha respondido incorrectamente.")
            es_correcta = respuesta_seleccionada == correcta
            dialog = DialogRonda(jugador.get_nombre_jugador(), es_correcta, correcta)
            dialog.exec()
            return respuesta_seleccionada
        else:  # Si el diálogo se cierra sin seleccionar
            QMessageBox.warning(self, "Advertencia", f"{jugador.get_nombre_jugador()} no respondió a la pregunta.")
            return None

    
    def evaluar_jugadores(self, jugadores):
        jugadores_errados = {}

        for jugador in jugadores:
            errores = 0
            if jugador.get_ronda1() == 2:  # Contestó mal en ronda1
                errores += 1
            if jugador.get_ronda2() == 2:  # Contestó mal en ronda2
                errores += 1
            if errores > 0:
                jugadores_errados[jugador] = errores

        if not jugadores_errados:
            print("Todos los jugadores acertaron todas las preguntas.")
            return jugadores  # Todos empatados

        max_errores = max(jugadores_errados.values())
        jugadores_a_desempatar = [jugador for jugador, errores in jugadores_errados.items() if errores == max_errores]
        return jugadores_a_desempatar
    
    def hacer_desempate(self, jugadores, pregunta_desempate):
        """
        Realiza una ronda de desempate donde todos los jugadores responden la misma pregunta.
        :param jugadores: list, lista de objetos de la clase Jugador que van al desempate
        :param pregunta_desempate: objeto preguntaDesempate, contiene el enunciado y la respuesta correcta
        :return: objeto Jugador que será eliminado
        """
        # Obtener datos de la pregunta
        enunciado = pregunta_desempate.get_enunciado()
        respuesta_correcta = pregunta_desempate.get_respuestaCorrecta()
        respuestas = {}
        for jugador in jugadores:
            # Crear y mostrar el diálogo
            dialog = VistaPreguntaAproximacion(enunciado, jugador.get_nombre_jugador())
            if dialog.exec() == QDialog.DialogCode.Accepted:
                respuestas[jugador] = dialog.get_respuesta()
            else:
                print(f"{jugador.get_nombre_jugador()} no respondió.")
        # Calcular distancias a la respuesta correcta
        distancias = {jugador: pregunta_desempate.responder(respuestas[jugador]) for jugador in jugadores}
        # Determinar el jugador eliminado
        jugador_eliminado = max(distancias, key=distancias.get)
        dialog = DialogDesempate(jugadores, jugador_eliminado, distancias, respuesta_correcta)
        dialog.exec()
        return jugador_eliminado

    def obtener_widget_por_jugador(self, jugador):
        """
        Obtiene el widget asociado a un jugador específico.
        :param jugador: objeto Jugador
        :return: WidgetJugador asociado al jugador, o None si no se encuentra
        """
        for widget in self.__lista_jugadores_widget:
            if widget.get_nombre_visual() == jugador.get_nombre_jugador():
                return widget
        print(f"Widget no encontrado para el jugador: {jugador.get_nombre_jugador()}")
        return None

    def actualizar_layout_escalon(self, escalon, lista_ganadores, perdedor, nro):
        """
        Actualiza los layouts de los escalones: mueve a los ganadores al siguiente escalón
        y deja al perdedor en el escalón actual, sin afectar los dos primeros elementos (QLabel y widget).
        """
        # Obtén los layouts actuales y el siguiente
        layout_actual = getattr(self.__vista, f"ly_escalon{nro + 1}")  # Layout del escalón actual
        layout_siguiente = getattr(self.__vista, f"ly_escalon{nro + 2}", None)  # Layout del próximo escalón
        if len(lista_ganadores) > 1:
            layout_siguiente.parent().parent().setStyleSheet("") #"Vacía" el StyleSheet para que use el color del .qss

        # Limpia el layout actual desde el tercer elemento en adelante
        for i in range(2, layout_actual.count()):  # Saltar los primeros dos elementos
            item = layout_actual.takeAt(2)  # Siempre tomar desde el índice 2 (después de QLabel y widget)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # Actualiza el layout actual con el jugador perdedor
        if perdedor:
            widget_perdedor = self.obtener_widget_por_jugador(perdedor)
            if widget_perdedor:
                layout_actual.addWidget(widget_perdedor)
            print(f"{perdedor.get_nombre_jugador()} permanece en el escalón {nro + 1}")

        # Si hay un siguiente escalón, mueve a los ganadores
        if layout_siguiente:
            for ganador in lista_ganadores:
                widget_ganador = self.obtener_widget_por_jugador(ganador)
                if widget_ganador:
                    layout_siguiente.addWidget(widget_ganador)
                    print(f"{ganador.get_nombre_jugador()} avanza al escalón {nro + 2}")

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