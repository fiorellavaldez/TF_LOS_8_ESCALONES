from modelo.PreguntasDAO import PreguntaDAO
from modelo.PreguntasABM import PreguntaABM

a = PreguntaABM().preguntas_ronda_tema(1)
for i in a:
    print(i.get_enunciado())
