

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
        #self.__vista.get_screen_button().clicked.connect(self.__alternar_pantalla_completa)

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

    # def __alternar_pantalla_completa(self):
    #     """Alterna entre pantalla completa y modo ventana normal."""
    #     ControladorVideo.is_fullscreen = not ControladorVideo.is_fullscreen
    #     ControladorVideo.aplicar_pantalla_completa()

        # # Cambiar el texto del botón en función del estado
        # if ControladorVideo.is_fullscreen:
        #     self.__vista.get_screen_button().setText("Modo Ventana")
        # else:
        #     self.__vista.get_screen_button().setText("Pantalla Completa")

    #     # Limpieza de ventanas no visibles
    #     self.__limpiar_ventanas_no_visibles()

    # def __limpiar_ventanas_no_visibles(self):
    #     """Elimina las ventanas que ya no están visibles de la lista registrada."""
    #     ControladorVideo.ventanas_registradas = [
    #         ventana for ventana in ControladorVideo.ventanas_registradas if ventana.isVisible()
    #     ]


