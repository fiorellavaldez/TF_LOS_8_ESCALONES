from  modelo.TemasDAO import TemasDAO
from modelo.Tema import Tema
from modelo.TemaABM import TemaABM
from modelo.PreguntasABM import PreguntaABM
from controlador.ControladorConfiguracionPreguntaNuevaDesempate import ControladorConfiguracionPreguntaNuevaDesempate
# abm = PreguntaABM().lista_preguntas_desempate

# for i in abm:
#     print(i.get_enunciado())
    
from PyQt6 import QtWidgets
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controlador = ControladorConfiguracionPreguntaNuevaDesempate(1)
    sys.exit(app.exec())
