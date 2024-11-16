from TemasDAO import TemasDAO
import random

temas = TemasDAO()

lista_temas = temas.get_all_temas()
tema=temas.get_tema(14)

print(lista_temas)
print(tema)

#temas.agregar_tema("Tema Nuevo" + str(random.randint(50,100)) )
#temas.agregar_tema("Tema Nuevo")
#temas.actualizar_tema(33,"Tema actualizado 33")

lista_temas = temas.temas_partida()

print(lista_temas)

