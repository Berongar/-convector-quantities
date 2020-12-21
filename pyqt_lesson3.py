from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import math

# pyuic5 mydesign.ui -o mydesign.py
# pyinstaller -w --onefile pyqt_lesson3.py


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button_Sechenie.clicked.connect(self.btnClicked_sechenie)
        self.ui.Button_Diametr.clicked.connect(self.btnClicked_diametr)
        self.ui.Button_Rashod.clicked.connect(self.btnClicked_rashod)

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
    def btnClicked_rashod(self):
        M3InHour = float(self.ui.Rashod_input_m3.text())
        LiterInHour = str(round(((M3InHour*1000)/60), 2))
        self.ui.Rashod_out_LinH.setText(LiterInHour)
        self.ui.Rashod_out_LinH.adjustSize()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())