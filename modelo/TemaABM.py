from  modelo.TemasDAO import TemasDAO
from modelo.Tema import Tema

class TemaABM:
    def __init__(self):
        #self.__lista_temas = TemasDAO().get_all_temas()
        self.__lista_temas = self.obtener_temas()
    
    @property
    def lista_temas(self):
        return self.__lista_temas
    
    def obtener_temas(self):
        #self.__lista_temas = TemasDAO().get_all_temas()
        lista=TemasDAO().get_all_temas()
        lista_temas=[]
        for id_tema, nombre_tema, estado_tema in lista: 
            lista_temas.append(Tema(id_tema,nombre_tema)) 
        return lista_temas # Lista de objetos Tema
    
    def actualizar_tema(self, tema:Tema):
        #print("Actualizar Temas!")
        for t in range(0,len(self.lista_temas)):
            if self.lista_temas[t].get_idTema() == tema.get_idTema():
                self.lista_temas[t].set_nombreTema(tema.get_nombreTema())
        
        TemasDAO().actualizar_tema(tema.get_idTema(), tema.get_nombreTema())
    

    def existe_tema(self, tema:Tema):
        tope =len(self.lista_temas)
        id = 0
        encontrado = False
        while id < tope and not encontrado:
            if self.lista_temas[id].get_nombreTema() == tema.get_nombreTema():
                encontrado = True
            id +=1
        return encontrado

    def agregar_tema(self, tema:Tema):
        self.__lista_temas.append(tema)
        TemasDAO().agregar_tema(tema.get_nombreTema())

    def quitar_tema(self, tema:Tema):
        lista_aux=[]
        for t in self.lista_temas:
            if t.get_idTema() != tema.get_idTema():
                lista_aux.append(t)

        self.__lista_temas = lista_aux
        TemasDAO().borrar_tema(tema.get_idTema())





    



    
