from modelo.PreguntasDAO import PreguntaDAO
from modelo.PreguntasABM import PreguntaABM
from modelo.TemaABM import TemaABM

a = TemaABM().obtener_temas_para_jugar()
for i in a:
    print(i.get_nombreTema())
