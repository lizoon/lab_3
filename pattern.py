from PyQt5.QtWidgets import *


def open_():
    file = QFileDialog.getOpenFileName(None, 'OPen', '/home')[0]
    f = open(file, 'r')


def create():
    layout = QStackedLayout()
    w = QWidget()
    w.move(500, 300)
    w.resize(400, 400)
    w.setWindowTitle('Новий файл')
    layout.addWidget(w)
    text = QTextEdit('', w)
    text.setText('ffpfppfpfpfpf')


def delete():
    pass

