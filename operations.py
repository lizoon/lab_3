from PyQt5.QtWidgets import *


class NewWindow(QDialog):
    def __init__(self, file):
        super(NewWindow, self).__init__()
        self.content = QTextEdit(self)
        self.content.resize(600, 800)
        self.content.setWindowTitle('Файл')
        self.input(file)
        self.show()
        super(NewWindow, self).exec_()

    def input(self, file):
        f = open(file, "r")
        res = ''
        for s in f.readlines():
            res += s
        self.content.setText(res)


if __name__ == '__main__':
    app = QApplication([])
    gui = NewWindow('2.txt')
    gui.show()
    app.exec_()
