from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import l3_modul
# import aff_modul


class ButtonBlock(Qwidget):
    super(QtGui.QWidget, self).__init__()
    def __init__(self):

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
x_line = QLineEdit('0')
y_line = QLineEdit('0')
r_line = QLineEdit()
x, y = 0, 0
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
saveButton.clicked.connect(l3_modul.saveImage)
def p():
    print('x =', int(x_line.text()), 'y = ', y_line.text(), 'r = ', r_line.text())

def set_x(text):
    global x
    x = int(x_line.text())

def set_y(text):
    global y
    print(text)
    y = int(y_line.text())
# translateButton.clicked.connect(p)
x_line.textChanged.connect(set_x)
y_line.textChanged.connect(set_y)
translateButton.clicked.connect(l3_modul.translation(x, y))
window.show()
# app.setStyle("Fusion")
app.exec_()