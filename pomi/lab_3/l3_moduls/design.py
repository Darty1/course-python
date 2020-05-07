from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import l3_modul
# import aff_modul


def on_affine_button_click():
    AffineLayout = QVBoxLayout()
    translateButton = QPushButton("Перемещение")
    rotateButton = QPushButton("Поворот")
    scalingButton = QPushButton("Масштабирование")
    sdvigButton = QPushButton("Сдвиг")
    AffineLayout.addWidget(translateButton, alignment=Qt.AlignCenter)
    AffineLayout.addWidget(rotateButton, alignment=Qt.AlignCenter)
    AffineLayout.addWidget(scalingButton, alignment=Qt.AlignCenter)
    AffineLayout.addWidget(sdvigButton, alignment=Qt.AlignCenter)
    window.setLayout(AffineLayout)
    window.show()

app = QApplication([])
window = QWidget()
label = QLabel()
#pix = QPixap('b.jpg')
#pix.width = 200
#pix.height = 200
#label.setPixmap(pix)
window.setWindowTitle("Lab_3")
window.resize(800, 600)
openButton = QPushButton("Загрузить изображение")
showButton = QPushButton("Открыть изображение")
grayButton = QPushButton("Преобразовать изображение в gray")
showChannelButton = QPushButton("Показать каждый канал изображения")
saveButton = QPushButton("Сохранить преобразованное изображение")
saveChannelButton = QPushButton("Сохранить изображение каждого канала")
AffineButton = QPushButton("Аффинные преобразования")
exitButton = QPushButton("Выход")
translateButton = QPushButton("Перемещение")
rotateButton = QPushButton("Поворот")
scalingButton = QPushButton("Масштабирование")
sdvigButton = QPushButton("Сдвиг")
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
AffinaLabelLayout = QHBoxLayout()
AffineFormLayout = QHBoxLayout()
AffineForm = QFormLayout()
global x, y, r
x_line = QLineEdit()
y_line = QLineEdit()
r_line = QLineEdit()
AffineForm.addRow(QLabel('x: '), x_line)
AffineForm.addRow(QLabel('y: '), y_line)
AffineForm.addRow(QLabel('r: '), r_line)
layoutV = QVBoxLayout()
AffineLabel = QLabel()
AffineLabel.setText('Аффинные преобразования:')
AffinaLabelLayout.addWidget(AffineLabel, alignment=Qt.AlignCenter)
layout1.addWidget(openButton, alignment=Qt.AlignCenter)
layout1.addWidget(showButton, alignment=Qt.AlignCenter)
layout2.addWidget(grayButton, alignment=Qt.AlignCenter)
layout4.addWidget(translateButton, alignment=Qt.AlignCenter)
layout4.addWidget(rotateButton, alignment=Qt.AlignCenter)
layout4.addWidget(scalingButton, alignment=Qt.AlignCenter)
layout4.addWidget(sdvigButton, alignment=Qt.AlignCenter)
layout3.addWidget(showChannelButton, alignment=Qt.AlignCenter)
layout1.addWidget(saveButton, alignment=Qt.AlignCenter)
layout3.addWidget(saveChannelButton, alignment=Qt.AlignCenter)
layout5.addWidget(exitButton, alignment=Qt.AlignCenter)
layoutV.addLayout(layout1)
layoutV.addLayout(layout2)
layoutV.addLayout(layout3)
layoutV.addLayout(AffinaLabelLayout)
layoutV.addLayout(AffineForm)
layoutV.addLayout(layout4)
layoutV.addLayout(layout5)
window.setLayout(layoutV)
exitButton.clicked.connect(app.exit)
openButton.clicked.connect(l3_modul.loadImage)
showButton.clicked.connect(l3_modul.viewImage)
grayButton.clicked.connect(l3_modul.gray)
showChannelButton.clicked.connect(l3_modul.show_chanel)
saveChannelButton.clicked.connect(l3_modul.save_channel)
saveButton.clicked.connect(l3_modul.save_image)
x = str(x_line.text())
y = str(y_line.text())
r = str(r_line.text())
translateButton.clicked.connect(l3_modul.translation(x, y))
window.show()
# app.setStyle("Fusion")
app.exec_()