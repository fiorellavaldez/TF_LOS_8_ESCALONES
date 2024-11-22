from controlador.ControladorVistaConfiguracionTemaABMEdit import ControladorVistaConfiguracionTemaABMEdit
from modelo.Tema import Tema
from modelo.TemaABM import TemaABM

class ControladorVistaConfiguracionTemaABMEditAlta(ControladorVistaConfiguracionTemaABMEdit):
    def __init__(self, controlador_anterior=None, tema = None, temas = None):
        super().__init__(controlador_anterior, tema, temas)
        self._vista.label_Titulo.setText("Tema Nuevo")
        self._vista.label_Mensaje.setText("Ingrese nuevo Tema:")
        self._vista.buttonBox_Confirmar.accepted.connect(self.__confirma)
        
        self.MainWindow.show()

    '''
    def __confirma(self):
    
        nuevo_nombre = self._vista.lineEdit_Tema.text().strip().upper()
        aux_tema=Tema(self._tema.get_idTema(),nuevo_nombre)
        
        if self._temas.existe_tema(aux_tema):
            # AQUI HAY QUE INCLUIR UNA VEMTANA CON EL MENSAJE DE ERROR
            self._vista.aviso_tema_existe()
            print("Tema ya existe")
            return
        else:                
            if aux_tema.get_nombreTema() == "":
                self._vista.aviso_tema_creado_vacio()
                return
            self._tema.set_nombreTema(nuevo_nombre)
            self._controlador_anterior.agregar_tema(self._tema)
            self._volver_configuracion()
    '''
    
    def __confirma(self):
    
        nuevo_nombre = self._vista.lineEdit_Tema.text().strip().upper()

        if not nuevo_nombre:
            self._vista.aviso_tema_creado_vacio()  # Muestra un mensaje de error
            print("Error: El nombre del tema no puede estar vacío.")
            return  
        aux_tema=Tema(idTema=-1,nombreTema=nuevo_nombre)
        if self._temas.existe_tema(aux_tema):
            self._vista.aviso_tema_existe()  # Muestra un mensaje de error
            print(f"Error: El tema '{nuevo_nombre}' ya existe en el sistema.")
            return  
        try:
            self._temas.agregar_tema(aux_tema)  
            self._vista.informamos_tema_creado(nuevo_nombre)  # Muestra un mensaje de éxito
            print(f"Éxito: El tema '{nuevo_nombre}' se ha creado exitosamente.")
        except Exception as e:
            # En caso de error durante el proceso de alta, muestra un mensaje
            print(f"Error al crear el tema: {e}")
            self._vista. aviso_tema_existe() 
            return  
        self._volver_configuracion()

            