from  modelo.TemasDAO import TemasDAO
from modelo.Tema import Tema

class TemaABM:
    def __init__(self):
        self.__lista_temas = self.obtener_temas()
    
    @property
    def lista_temas(self):
        return self.__lista_temas
    
    def obtener_temas(self):
        lista=TemasDAO().get_all_temas()
        lista_temas=[]
        for id_tema, nombre_tema, estado_tema in lista: 
            lista_temas.append(Tema(id_tema,nombre_tema)) 
        return lista_temas # Lista de objetos Tema
    
    def actualizar_tema(self, tema:Tema):
        for t in range(0,len(self.__lista_temas)):
            if self.__lista_temas[t].get_idTema() == tema.get_idTema():
                self.__lista_temas[t].set_nombreTema(tema.get_nombreTema())
        
        TemasDAO().actualizar_tema(tema.get_idTema(), tema.get_nombreTema())
     
    def existe_tema(self, tema:Tema):
        # Iteramos sobre todos los temas
        for t in self.__lista_temas:
            # Comparamos los nombres de los temas ignorando mayúsculas/minúsculas y espacios adicionales
            if t.get_nombreTema().strip().upper() == tema.get_nombreTema().strip().upper():
                return True  # Si encontramos un tema con el mismo nombre, devolvemos True
        return False  # Si no lo encontramos, devolvemos False

    def agregar_tema(self, tema:Tema):
        TemasDAO().agregar_tema(tema.get_nombreTema())
        self.__lista_temas = self.obtener_temas() # Vuelvo a cargar toda la lista para obtener el ID

    def quitar_tema(self, tema:Tema):
        lista_aux=[]
        for t in self.lista_temas:
            if t.get_idTema() != tema.get_idTema():
                lista_aux.append(t)

        self.__lista_temas = lista_aux
        TemasDAO().borrar_tema(tema.get_idTema())

        #agregado el 20-11, lo probe y funciona
    def obtener_temas_para_jugar(self):
        temas_para_jugar = []
        lista_aux = TemasDAO().temas_partida()
    # solo quiero 8 elementos en la lista
        for id_tema, nombre_tema in lista_aux[:8]:
            temas_para_jugar.append(Tema(id_tema, nombre_tema))
        return temas_para_jugar



    



    
