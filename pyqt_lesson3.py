from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import math


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button_Sechenie.clicked.connect(self.btnClicked_sechenie)
        self.ui.Button_Diametr.clicked.connect(self.btnClicked_diametr)

    def btnClicked_sechenie(self):
        Diametr = float(self.ui.Diametr_input.text())
        Sechenie = str(round((0.785*Diametr*Diametr), 2))

        self.ui.Sechenie_Out.setText(Sechenie)
        self.ui.Sechenie_Out.adjustSize()

    def btnClicked_diametr(self):
        Sechenie = float(self.ui.Sechenie_input.text())
        Diametr = str(round(math.sqrt(Sechenie/0.785), 2))
        self.ui.Diametr_out.setText(Diametr)
        self.ui.Diametr_out.adjustSize()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())