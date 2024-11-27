from controlador.ControladorVistaConfiguracionTemaABMEdit import ControladorVistaConfiguracionTemaABMEdit
from modelo.Tema import Tema

class ControladorVistaConfiguracionTemaABMEditModifica(ControladorVistaConfiguracionTemaABMEdit):
    def __init__(self, controlador_anterior=None, tema = None, temas = None):
        super().__init__(controlador_anterior, tema, temas)
        self._vista.label_Titulo.setText("Modificar Tema")
        self._vista.label_Mensaje.setText("Modifique el Tema:")
        self._vista.buttonBox_Confirmar.accepted.connect(self.__confirma)
        
        self.MainWindow.show()

    def __confirma(self):
    
        nuevo_nombre = self._vista.lineEdit_Tema.text()
        aux_tema=Tema(self._tema.get_idTema(),nuevo_nombre)
        if self._temas.existe_tema(aux_tema):
            self._vista.aviso_tema_existe()
            print("Tema ya existe")
            return
        else:  
            if aux_tema.get_nombreTema() == "":
                self._vista.aviso_tema_creado_vacio()
                return
            self._tema.set_nombreTema(nuevo_nombre)
            self._temas.actualizar_tema(self._tema) # Actualiza BD
            self._controlador_anterior.actualizar_lista_temas(self._tema) # Usado para actualizar la lista en el controlador llamador
            self._volver_configuracion()