from PySide6.QtWidgets import QApplication, QMainWindow
from ui_principal import Ui_MainWindow


app = QApplication([])
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

nome = ui.textEdit.text()
print(nome)

window.show()
app.exec()