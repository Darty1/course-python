from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import PyQt5
from


app = QApplication([])
window = QWidget()
window.setWindowTitle("Lab_3")
window.resize(800, 600)
openButton = QPushButton("Открыть изображение")
showButton = QPushButton("Показать изображение")
grayButton = QPushButton("Преобразовать изображение в RGB")
showChannelButton = QPushButton("Показать каждый канал изображения")
saveButton = QPushButton("Сохранить преобразованное изображение")
saveChannelButton = QPushButton("Сохранить изображение каждого канала")
exitButton = QPushButton("Выход")
layout = QVBoxLayout()
layout.addWidget(openButton, alignment=Qt.AlignCenter)
layout.addWidget(showButton, alignment=Qt.AlignCenter)
layout.addWidget(grayButton, alignment=Qt.AlignCenter)
layout.addWidget(showChannelButton, alignment=Qt.AlignCenter)
layout.addWidget(saveButton, alignment=Qt.AlignCenter)
layout.addWidget(saveChannelButton, alignment=Qt.AlignCenter)
layout.addWidget(exitButton, alignment=Qt.AlignCenter)
window.setLayout(layout)
window.show()
app.exec_()