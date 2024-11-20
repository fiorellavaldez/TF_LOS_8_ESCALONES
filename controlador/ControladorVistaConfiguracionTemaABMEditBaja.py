from controlador.ControladorVistaConfiguracionTemaABMEdit import ControladorVistaConfiguracionTemaABMEdit
from modelo.Tema import Tema

class ControladorVistaConfiguracionTemaABMEditBaja(ControladorVistaConfiguracionTemaABMEdit):
    def __init__(self, controlador_anterior=None, tema = None, temas = None):
        super().__init__(controlador_anterior, tema, temas)
        self._vista.label_Titulo.setText("Eliminar Tema")
        self._vista.label_Mensaje.setText("Confirme la eliminacion del Tema:")
        # Hacer que el campo de texto no sea editable
        self._vista.lineEdit_Tema.setReadOnly(True)
        
        self._vista.buttonBox_Confirmar.accepted.connect(self.__confirma)
        
        self.MainWindow.show()

    def __confirma(self):
    
        nuevo_nombre = self._vista.lineEdit_Tema.text()
        self._tema.set_nombreTema(nuevo_nombre)
        self._controlador_anterior.quitar_tema(self._tema)
        self._volver_configuracion()