import sys
from PyQt5.QtWidgets import *
import widgets
import content
import pattern
import delete_tabs
from operations import NewWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.cmb_path = {'', '/home'}
        self.cmb_types = {'', 'All files [*.]',
                          'Text files [*.txt]',
                          'Doc files [*.doc]',
                          'Folder',
                          'Html files [*.html]',
                          'JPG files [*.jpg]',
                          'PDF files [*.pdf]',
                          'ZIP files [*.zip]',
                          'Py files [*.py]',
                          'Xsl files [*.xsl]',
                          'Mp3 files [*.mp3]'}
        self.path_name = ''
        self.s = ''

        self.resize(1200, 870)
        self.setWindowTitle('Файловий менеджер')

        self.left = QLabel('', self)
        self.left.move(100, 30)
        self.left.resize(1000, 630)
        self.left.setStyleSheet('border-style: inset; border-width: 2px; border-color: gray;')

        self.title1 = QLabel('Файл', self)
        self.title1.move(100, 670)

        self.title2 = QLabel('Операції', self)
        self.title2.move(100, 770)

        self.file = QLabel('', self)
        self.file.setText('\tВідкрити\t\tСтворити\t\tВидалити')
        self.file.move(120, 700)
        self.file.resize(500, 50)
        self.file.setStyleSheet('border-style: inset; border-width: 2px; border-color: gray;')

        self.actions = QLabel('', self)
        self.actions.setText('\tctrl+o Відкрити\t\t'
                             'ctrl+c Копіювати\t\t'
                             'ctrl+v Вставити\t\t'
                             'Delete Видалити\t')
        self.actions.move(120, 800)
        self.actions.resize(700, 50)
        self.actions.setStyleSheet('border-style: inset; border-width: 2px; border-color: gray;')

        self.choose1 = QComboBox(self)
        self.choose1.move(120, 560)
        self.choose1.setCurrentText('')

        self.path = QTextEdit('', self)
        self.path.setText('')
        self.path.move(120, 610)
        self.path.resize(350, 30)
        self.path.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        self.type = QComboBox(self)
        self.type.move(500, 560)
        self.type.resize(150, 30)

        self.fm_load()

        self.clear = QPushButton('Оновити', self)
        self.clear.move(980, 610)

        self.back = QPushButton('Повернутись', self)
        self.back.move(500, 610)
        self.back.clicked.connect(self.back_)

        self.catalog = QListWidget(self)
        self.catalog.setStyleSheet('font-size: 15px')
        self.catalog.move(120, 50)
        self.catalog.resize(350, 490)

        self.files = QListWidget(self)
        self.files.setStyleSheet('font-size: 15px')
        self.files.move(500, 50)
        self.files.resize(580, 490)

        self.choose1.currentTextChanged.connect(self.f_change)
        self.type.currentTextChanged.connect(self.build_files)
        self.catalog.itemDoubleClicked.connect(self.double_click)
        self.files.itemClicked.connect(self.chosen)
        self.files.doubleClicked.connect(self.open_)

        self.create_menubar()

    def open_(self):
        cur_file = self.files.currentItem().text()
        _new_win = NewWindow(cur_file)

    def create_menubar(self):
        menubar = self.menuBar()

        file_menu = QMenu("&Файл", self)
        menubar.addMenu(file_menu)
        open = file_menu.addAction('Відкрити')
        open.triggered.connect(pattern.open_)

        create = file_menu.addAction('Створити')
        create.triggered.connect(pattern.create)

        delete = file_menu.addAction('Видалити')
        delete.triggered.connect(pattern.delete)

        change_menu = QMenu("&Дії", self)
        menubar.addMenu(change_menu)

        change_menu.addAction('6.Пошук HTML')
        change_menu.addAction('10.')
        convert_menu = change_menu.addMenu('2.Конвертація')
        convert_menu.addAction('HTML до RTF')
        convert_menu.addAction('RTF до HTML')
        change_menu.addAction('10.Видалити пробіли та таб')

        change_menu.triggered.connect(self.del_)

        about_menu = menubar.addAction("&Про програму")
        about_menu.triggered.connect(widgets.about)

        help_menu = menubar.addMenu("&Допомога")
        help_menu.addAction('Основний функціонал')
        help_menu.addAction('В межах лабораторної')
        help_menu.triggered.connect(widgets.help_)

    def fm_load(self):
        self.choose1.addItems(self.cmb_path)
        self.type.addItems(self.cmb_types)

    def double_click(self):
        self.path_name = self.path_name + '/' + self.catalog.currentItem().text()
        self.build_fold('Folder')
        self.build_files()

    def f_change(self):
        self.path_name = self.choose1.currentText()
        self.type.setCurrentText('All files [*.]')
        self.build_fold('Folder')

    def back_(self):
        rem = ''
        for sym in self.path_name[::-1]:
            rem = rem + sym
            if sym == '/':
                rem = rem[::-1]
                if self.path_name == '/home':
                    pass
                else:
                    self.path_name = self.path_name.replace(rem, '')
                break
        self.build_fold('Folder')
        self.build_files()

    def build_fold(self, s):
        self.path.setText(self.path_name)
        catalogic = content.fill(self, self.path_name)
        if catalogic != ['x']:
            content.show(catalogic, s, self.catalog)

    def build_files(self):
        s = self.type.currentText()
        catalogic = content.fill_files(self, self.path_name, s)
        if catalogic != ['x']:
            content.show(catalogic, s, self.files)

    def chosen(self, item):
        self.s = item.text()
        print(self.s)

    def del_(self):
        delete_tabs.f(self.s)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(qApp.exec_())
