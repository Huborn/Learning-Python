import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton



























####     Блок окна     ####
def on_click():
    lable.setText("Твой статус: Гордый обладатель Poco!")

app = QApplication(sys.argv)
window = QWidget()

####     Текст       ####
lable = QLabel("Нажми на кнопку чтобы... чтобы что?", window)

####     Кнопки      ####
btn = QPushButton("Узнать ранг", window)

window.setWindowTitle("Qt6 Window Test")
window.resize(400, 300)

lable.move(50, 50)
btn.move(10, 250)

btn.clicked.connect(on_click)

window.show()
sys.exit(app.exec())