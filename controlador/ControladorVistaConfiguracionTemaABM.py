from vista.VistaConfiguracionTemaABM import Ui_MainWindow
from controlador.ControladorVistaTemaNuevo import ControladorVistaTemaNuevo
#from controlador.ControladorVistaConfiguracinTemaABMEdit import ControladorVistaConfiguracionTemaABMEdit
from controlador.ControladorVistaConfiguracionTemaABMEditModifica import ControladorVistaConfiguracionTemaABMEditModifica
from controlador.ControladorVistaConfiguracionTemaABMEditAlta import ControladorVistaConfiguracionTemaABMEditAlta
from controlador.ControladorVistaConfiguracionTemaABMEditBaja import ControladorVistaConfiguracionTemaABMEditBaja
from vista.VistaConfiguracionTemaABMEdit import Ui_Widget
from modelo.Tema import Tema
from modelo.TemaABM import TemaABM
from controlador.ControladorVideo import ControladorVideo
from controlador.ControladorVentanaMain import ControladorVentanaMain

from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from  modelo.TemasDAO import TemasDAO
from PyQt6.QtCore import QStringListModel
from PyQt6.QtCore import QEvent

class ControladorVistaConfiguracionTemaABM:
    #def __init__(self):
    def __init__(self, controlador_anterior=None):
        self.__controlador_anterior = controlador_anterior
        #self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow = ControladorVentanaMain()
        self.WindowEdit = QtWidgets.QWidget()
        self.__vista = Ui_MainWindow()
        self.__vista.setupUi(self.MainWindow)
        self.__vistaEdit = Ui_Widget()
        self.__vistaEdit.setupUi(self.WindowEdit)
        
        # Registrar la ventana en el controlador de audio y video
        ControladorVideo.registrar_ventana(self.MainWindow)
        
        self.__filtered_temas = []
        self.model = QStringListModel()

        # Conexion Botones
        self.__vista.pushButton_Volver.clicked.connect(self.__volver_configuracion)
        self.__vista.pushButton_Modificar.clicked.connect(self.__modificarTema)
        self.__vista.pushButton_Nuevo.clicked.connect(self.__nuevoTema)
        self.__vista.pushButton_Eliminar.clicked.connect(self.__eliminarTema)
        self.__vista.QTable_Temas.doubleClicked.connect(self.__modificarTema)

        # Formateo Tabla
        self.__vista.QTable_Temas.setColumnCount(2)
        self.__vista.QTable_Temas.setColumnHidden(0,True)
        self.__vista.QTable_Temas.setColumnWidth(1,400)
        self.__vista.QTable_Temas.setHorizontalHeaderLabels(["Id_tema","Tema"]) #El parametro para los nombres de los encabezados debe ser un iterable
        self.__vista.QTable_Temas.setVerticalHeaderLabels([""])
        self.__vista.QTable_Temas.verticalHeader().hide()

        self.__vista.QLine_Buscar.textChanged.connect(self.__buscar_temas)

        self.__temas=TemaABM()

        self.MainWindow.show()

        self.__llenar_tabla(self.__temas.lista_temas)


    def __llenar_tabla(self, lista_temas):
        self.__vista.QTable_Temas.setRowCount(len(lista_temas))
        for linea, tema in enumerate(lista_temas):
            ##SELECCIONO EL ID Y EL TEMA
            item_id = QTableWidgetItem(str(tema.get_idTema()))
            item_nombre = QTableWidgetItem(tema.get_nombreTema())
            
            #Desactivo la edicion en esa linea
            item_id.setFlags(item_id.flags() & ~Qt.ItemFlag.ItemIsEditable)
            item_nombre.setFlags(item_nombre.flags() & ~Qt.ItemFlag.ItemIsEditable)
            
            self.__vista.QTable_Temas.setItem(linea, 0, item_id)
            self.__vista.QTable_Temas.setItem(linea, 1, item_nombre)
            
            #self.__vista.QTable_Temas.setItem(linea, 0, QTableWidgetItem(str(tema.get_idTema())))  
            #self.__vista.QTable_Temas.setItem(linea, 1, QTableWidgetItem(tema.get_nombreTema()))  
    
    def actualizar_lista_temas(self, tema):
        #self.__temas.actualizar_tema(tema)
        self.__llenar_tabla(self.__temas.lista_temas)
    
    """def agregar_tema(self, tema):
        tema.set_disponible(True)
        self.__temas.agregar_tema(tema)
        self.__llenar_tabla(self.__temas.lista_temas)
    """
    """def quitar_tema(self,tema):
        tema.set_disponible(False)
        self.__temas.quitar_tema(tema)
        self.__llenar_tabla(self.__temas.lista_temas)
    """
    def __volver_configuracion(self):
        self.MainWindow.hide()
        self.__controlador_anterior.MainWindow.show()

    def __modificarTema(self):
        
        fila_actual = self.__vista.QTable_Temas.currentRow()
        if fila_actual == -1:  # Ninguna fila seleccionada
            self.__vista.aviso_seleccionar_tema()
            return
        #self.MainWindow.hide()
        tema_s=self.__obtener_tema_seleccionado()
        try: # --> DAO
        # Aquí llamas al método de ABM para realizar la modificación
            #self.__temas.actualizar_tema(tema_s)  # Lógica de actualización de tema --> Tiene que ir en el EditModifica

            self.ControladorVistaTemaNuevo = ControladorVistaConfiguracionTemaABMEditModifica(self,tema_s,self.__temas)
            self.ControladorVistaTemaNuevo.MainWindow.show()
        except Exception as e:
        # Si hay algún error en la modificación, lo manejas
            print(f"Error al modificar el tema: {e}")
            return
        
        
    def __nuevoTema(self):
        tema_s=Tema(0,"")
        self.ControladorVistaTemaNuevo = ControladorVistaConfiguracionTemaABMEditAlta(self,tema_s,self.__temas)
        self.ControladorVistaTemaNuevo.MainWindow.show()

    def __eliminarTema(self):
        fila_actual = self.__vista.QTable_Temas.currentRow()
        if fila_actual == -1:  # Ninguna fila seleccionada
            self.__vista.aviso_seleccion_tema()
            return
        tema=self.__obtener_tema_seleccionado()
        respuesta=self.__vista.aviso_eliminar_tema(tema)
        if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
        #tema_s=self.__obtener_tema_seleccionado()
            self.__temas.quitar_tema(tema)
            self.__temas.actualizar_tema(tema)
            self.__llenar_tabla(self.__temas.lista_temas)
            # self.__temas.actualizar_tema(tema)
            QtWidgets.QMessageBox.information(None, "Tema eliminado", f"El tema '{tema.get_nombreTema()}' fue eliminado con éxito.")
            #self.ControladorVistaTemaNuevo = ControladorVistaConfiguracionTemaABMEditBaja(self,tema,self.__temas)
            #self.ControladorVistaTemaNuevo.MainWindow.show()
        else:
            return

    """def __obtener_celda_seleccionada(self):  
        item = self.__vista.QTable_Temas.currentItem()  
        if item is not None:  
            print("Contenido de la celda seleccionada:", item.text())  
        else:  
            print("No hay ninguna celda seleccionada.") 
        """
    
    def __buscar_temas(self):
        """Filtra los temas según el texto ingresado en la caja de búsqueda y actualiza la tabla."""
        texto = self.__vista.QLine_Buscar.text().strip().lower()
        # Filtrar temas que coincidan con el texto ingresado
        self.__filtered_temas = [
            tema for tema in self.__temas.lista_temas
            if tema.get_nombreTema().lower().startswith(texto)
            ]
        # Llenar la tabla con los temas filtrados
        self.__llenar_tabla(self.__filtered_temas)

    def __obtener_tupla_seleccionada(self):
        fila_actual = self.__vista.QTable_Temas.currentRow()  # Obtiene la fila seleccionada  
        if fila_actual != -1:  # Verifica que haya una fila seleccionada  
            datos_tupla = []  
            for columna in range(self.__vista.QTable_Temas.columnCount()):  
                item = self.__vista.QTable_Temas.item(fila_actual, columna)  
                if item is not None:  
                    datos_tupla.append(item.text())  
            return datos_tupla
        else:
            return [0,""]

    
    def __obtener_tema_seleccionado(self):
        tupla=self.__obtener_tupla_seleccionada()
        tema_s=Tema(int(tupla[0]),tupla[1])
        return tema_s
    