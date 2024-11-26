# from PyQt6.QtGui import QScreen

# class ControladorVideo:
#     """Controlador para gestionar el estado de pantalla completa de ventanas."""
#     is_fullscreen = True  # Estado global de pantalla completa
#     ventanas_registradas = []  # Lista de ventanas registradas para sincronización

#     def __init__(self, ventana, vista):
#         """
#         Inicializa el controlador de video con una ventana principal y su vista asociada.
        
#         :param ventana: La ventana principal.
#         :param vista: La vista con la interfaz gráfica asociada.
#         """
#         self.__ventana = ventana
#         self.__vista = vista

#         # Conectar la señal del botón para alternar pantalla completa
#         self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)

#         # Registrar la ventana actual
#         self.registrar_ventana(self.__ventana)

#     @classmethod
#     def registrar_ventana(cls, ventana):
#         """
#         Registra una nueva ventana para sincronizar su estado de pantalla completa.
        
#         :param ventana: Instancia de la ventana a registrar.
#         """
#         # Asegurarse de que no haya ventanas redundantes
#         cls.__ocultar_y_eliminar_ventanas()

#         if ventana not in cls.ventanas_registradas:
#             cls.ventanas_registradas.append(ventana)

#         # Mostrar la ventana automáticamente en pantalla completa
#         cls.aplicar_pantalla_completa()
#         ventana.show()  # Asegura que la ventana se muestre inmediatamente

#     @classmethod
#     def __ocultar_y_eliminar_ventanas(cls):
#         """Cierra todas las ventanas registradas y vacía la lista."""
#         for ventana in cls.ventanas_registradas:
#             if ventana.isVisible():
#                 ventana.close()
#         cls.ventanas_registradas.clear()

#     @classmethod
#     def aplicar_pantalla_completa(cls):
#         """Aplica el estado de pantalla completa a las ventanas registradas."""
#         for ventana in cls.ventanas_registradas:
#             if ventana.isVisible():
#                 if cls.is_fullscreen:
#                     ventana.showFullScreen()
#                 else:
#                     ventana.showNormal()
#                     cls.centrar_ventana(ventana)

#     @staticmethod
#     def centrar_ventana(ventana):
#         """Centra la ventana en la pantalla activa."""
#         screen = QScreen.availableGeometry(ventana.screen())
#         window_size = ventana.size()
#         x = (screen.width() - window_size.width()) // 2
#         y = (screen.height() - window_size.height()) // 2
#         ventana.move(x, y)

#     def __alternar_pantalla_completa(self):
#         """Alterna entre pantalla completa y modo ventana normal."""
#         ControladorVideo.is_fullscreen = not ControladorVideo.is_fullscreen
#         ControladorVideo.aplicar_pantalla_completa()

#         # Cambiar el texto del botón en función del estado
#         if ControladorVideo.is_fullscreen:
#             self.__vista.get_screen_button().setText("Modo Ventana")
#         else:
#             self.__vista.get_screen_button().setText("Pantalla Completa")

#         # Limpieza de ventanas no visibles
#         self.__limpiar_ventanas_no_visibles()

#     def __limpiar_ventanas_no_visibles(self):
#         """Elimina las ventanas que ya no están visibles de la lista registrada."""
#         ControladorVideo.ventanas_registradas = [
#             ventana for ventana in ControladorVideo.ventanas_registradas if ventana.isVisible()
#         ]



#------------------------------------------------------------------------------------------------
# from PyQt6.QtGui import QScreen

# class ControladorVideo:
#     """Controlador para la configuración de video."""

#     is_fullscreen = True  # Estado global de pantalla completa
#     ventanas_registradas = []  # Lista de referencias a ventanas visibles

#     def __init__(self, ventana, vista):
#         """
#         Inicializa el controlador de video con una instancia de la ventana principal y la vista.
#         """
#         self.__ventana = ventana
#         self.__vista = vista

#         # Conectar señales de video
#         self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)

#         # Registrar la ventana al iniciar
#         self.registrar_ventana(self.__ventana)

#     @classmethod
#     def registrar_ventana(cls, ventana):
#         """
#         Registra una ventana para sincronizar el estado de pantalla completa.
#         Oculta y elimina correctamente las ventanas previas.
#         """
#         # Ocultar y eliminar ventanas anteriores
#         cls.__ocultar_y_eliminar_ventanas()

#         # Registrar la nueva ventana
#         if ventana not in cls.ventanas_registradas:
#             cls.ventanas_registradas.append(ventana)

#         # Aplicar el estado actual de pantalla completa
#         cls.aplicar_pantalla_completa()

#     @classmethod
#     def __ocultar_y_eliminar_ventanas(cls):
#         """Oculta y elimina todas las ventanas previamente registradas."""
#         for ventana in cls.ventanas_registradas:
#             if ventana.isVisible():  # Solo manejar ventanas visibles
#                 ventana.close()
#         # Vaciar la lista de ventanas registradas
#         cls.ventanas_registradas.clear()

#     @classmethod
#     def aplicar_pantalla_completa(cls):
#         """Aplica el estado de pantalla completa a la ventana activa."""
#         for ventana in cls.ventanas_registradas:
#             if ventana.isVisible():  # Asegurarse de trabajar solo con ventanas visibles
#                 if cls.is_fullscreen:
#                     ventana.showFullScreen()
#                 else:
#                     ventana.showNormal()
#                     cls.centrar_ventana(ventana)

#     @staticmethod
#     def centrar_ventana(ventana):
#         """Centra la ventana en la pantalla principal."""
#         screen = QScreen.availableGeometry(ventana.screen())
#         window_size = ventana.size()
#         x = (screen.width() - window_size.width()) // 2
#         y = (screen.height() - window_size.height()) // 2
#         ventana.move(x, y)

#     def __alternar_pantalla_completa(self):
#         """Alterna entre pantalla completa y modo ventana normal."""
#         ControladorVideo.is_fullscreen = not ControladorVideo.is_fullscreen
#         ControladorVideo.aplicar_pantalla_completa()

#         # Cambiar el texto del botón
#         if ControladorVideo.is_fullscreen:
#             self.__vista.get_screen_button().setText("Modo Ventana")
#         else:
#             self.__vista.get_screen_button().setText("Pantalla Completa")

#         # Limpiar ventanas no visibles
#         self.__limpiar_ventanas_no_visibles()

#     def __limpiar_ventanas_no_visibles(self):
#         """Limpia ventanas que ya no están visibles."""
#         ControladorVideo.ventanas_registradas = [
#             ventana for ventana in ControladorVideo.ventanas_registradas if ventana.isVisible()
#         ]
#__________________________________________________________________________________

##########################################################################
########FUNCIONA PERO GENERA MULTIPLES VENTANAS

from PyQt6.QtGui import QScreen

class ControladorVideo:
    """Controlador para la configuración de video."""

    is_fullscreen = True  # Estado global de pantalla completa
    ventanas_registradas = []

    def __init__(self, ventana, vista):
        """
        Inicializa el controlador de video con una instancia de la ventana principal y la vista.
        """
        self.__ventana = ventana
        self.__vista = vista

        # Conectar señales de video
        self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)

        # Registrar la ventana al iniciar
        self.registrar_ventana(self.__ventana)

    @classmethod
    def registrar_ventana(cls, ventana):
        """
        Registra una nueva ventana para sincronizar su estado de pantalla completa.
        
        :param ventana: Instancia de la ventana a registrar.
        """
        # Asegurarse de que no haya ventanas redundantes
        cls.__ocultar_y_eliminar_ventanas()

        if ventana not in cls.ventanas_registradas:
            cls.ventanas_registradas.append(ventana)

        # Mostrar la ventana automáticamente en pantalla completa
        cls.aplicar_pantalla_completa()
        ventana.show()  # Asegura que la ventana se muestre inmediatamente

    @classmethod
    def __ocultar_y_eliminar_ventanas(cls):
        """Cierra todas las ventanas registradas y vacía la lista."""
        for ventana in cls.ventanas_registradas:
            if ventana.isVisible():
                ventana.close()
        cls.ventanas_registradas.clear()

    @classmethod
    def aplicar_pantalla_completa(cls):
        """Aplica el estado de pantalla completa a las ventanas registradas."""
        for ventana in cls.ventanas_registradas:
            if ventana.isVisible():
                if cls.is_fullscreen:
                    ventana.showFullScreen()
                else:
                    ventana.showNormal()
                    cls.centrar_ventana(ventana)

    @staticmethod
    def centrar_ventana(ventana):
        """Centra la ventana en la pantalla activa."""
        screen = QScreen.availableGeometry(ventana.screen())
        window_size = ventana.size()
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        ventana.move(x, y)

    def __alternar_pantalla_completa(self):
        """Alterna entre pantalla completa y modo ventana normal."""
        ControladorVideo.is_fullscreen = not ControladorVideo.is_fullscreen
        ControladorVideo.aplicar_pantalla_completa()

        # Cambiar el texto del botón en función del estado
        if ControladorVideo.is_fullscreen:
            self.__vista.get_screen_button().setText("Modo Ventana")
        else:
            self.__vista.get_screen_button().setText("Pantalla Completa")

        # Limpieza de ventanas no visibles
        self.__limpiar_ventanas_no_visibles()

    def __limpiar_ventanas_no_visibles(self):
        """Elimina las ventanas que ya no están visibles de la lista registrada."""
        ControladorVideo.ventanas_registradas = [
            ventana for ventana in ControladorVideo.ventanas_registradas if ventana.isVisible()
        ]



#######################################################################
# ##FUNCIONA TODO MENOS LA CONFIGURACION DE AUDIO Y VIDEO
# from vista.VistaAudioVideo import Ui_ConfigWindow
# from PyQt6.QtWidgets import QMainWindow
# from PyQt6.QtGui import QScreen

# class ControladorVideo:
#     """Controlador para la configuración de video."""

#     is_fullscreen = True  # Estado global de pantalla completa
#     ventanas_registradas = []

#     def __init__(self, vista):
#         """Inicializa el controlador de video con una instancia de la vista."""
#         if not isinstance(vista, QMainWindow):
#             raise TypeError("La vista debe ser una instancia de QMainWindow o una subclase.")
        
#         self.__vista = vista

#         # Registrar la ventana inicial
#         ControladorVideo.registrar_ventana(self.__vista)

#         # Configurar pantalla completa inicial
#         ControladorVideo.aplicar_pantalla_completa()

#         # Conectar señales de la vista
#         self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)

#     @classmethod
#     def registrar_ventana(cls, ventana):
#         """Registra una ventana para sincronizar el estado de pantalla completa."""
#         if ventana not in cls.ventanas_registradas:
#             cls.ventanas_registradas.append(ventana)
#             # Aplicar el estado actual a la nueva ventana
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()
#                 cls.centrar_ventana(ventana)

#     @classmethod
#     def aplicar_pantalla_completa(cls):
#         """Aplica el estado de pantalla completa a todas las ventanas registradas."""
#         for ventana in cls.ventanas_registradas:
#             try:
#                 if cls.is_fullscreen:
#                     ventana.showFullScreen()
#                 else:
#                     ventana.showNormal()
#                     cls.centrar_ventana(ventana)
#             except Exception as e:
#                 print(f"Error al aplicar pantalla completa a la ventana: {e}")

#     @staticmethod
#     def centrar_ventana(ventana):
#         """Centra la ventana en la pantalla principal."""
#         try:
#             screen = QScreen.availableGeometry(ventana.screen())
#             window_size = ventana.size()
#             x = (screen.width() - window_size.width()) // 2
#             y = (screen.height() - window_size.height()) // 2
#             ventana.move(x, y)
#         except Exception as e:
#             print(f"Error al centrar la ventana: {e}")

#     def __alternar_pantalla_completa(self):
#         """Alterna entre pantalla completa y modo ventana normal."""
#         # Alternar el estado global de pantalla completa
#         ControladorVideo.is_fullscreen = not ControladorVideo.is_fullscreen

#         # Aplicar el nuevo estado a todas las ventanas registradas
#         ControladorVideo.aplicar_pantalla_completa()

#         # Cambiar el texto del botón
#         nuevo_texto = "Modo Ventana" if ControladorVideo.is_fullscreen else "Pantalla Completa"
#         self.__vista.get_screen_button().setText(nuevo_texto)


# from vista.VistaAudioVideo import Ui_ConfigWindow
# from PyQt6.QtWidgets import QMainWindow
# from PyQt6.QtGui import QScreen

# class ControladorVideo:
#     """Controlador para la configuración de video."""

#     is_fullscreen = True  # Estado global de pantalla completa
#     ventanas_registradas = []

#     def __init__(self, vista):
#         """Inicializa el controlador de video con una instancia de la vista."""
#         self.__vista = vista

#         # Conectar señales de video
#         self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)

#     @classmethod
#     def registrar_ventana(cls, ventana):
#         """Registra una ventana para sincronizar el estado de pantalla completa."""
#         if ventana not in cls.ventanas_registradas:
#             cls.ventanas_registradas.append(ventana)
#             cls.aplicar_pantalla_completa()

#     @classmethod
#     def aplicar_pantalla_completa(cls):
#         """Aplica el estado de pantalla completa a todas las ventanas registradas."""
#         for ventana in cls.ventanas_registradas:
#             if cls.is_fullscreen:
#                 ventana.showFullScreen()
#             else:
#                 ventana.showNormal()
#                 cls.centrar_ventana(ventana)

#     @staticmethod
#     def centrar_ventana(ventana):
#         """Centra la ventana en la pantalla principal."""
#         screen = QScreen.availableGeometry(ventana.screen())
#         window_size = ventana.size()
#         x = (screen.width() - window_size.width()) // 2
#         y = (screen.height() - window_size.height()) // 2
#         ventana.move(x, y)

#     def __alternar_pantalla_completa(self):
#         """Alterna entre pantalla completa y modo ventana normal."""
#         ControladorVideo.is_fullscreen = not ControladorVideo.is_fullscreen
#         ControladorVideo.aplicar_pantalla_completa()

#         # Cambiar el texto del botón
#         if ControladorVideo.is_fullscreen:
#             self.__vista.get_screen_button().setText("Modo Ventana")
#         else:
#             self.__vista.get_screen_button().setText("Pantalla Completa")


