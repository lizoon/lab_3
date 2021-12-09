from PyQt5.QtWidgets import *


def about():
    QMessageBox.information(None, 'Про програму\n',
                            'Програма розроблена ученицею\n'
                            'групи К-24\n'
                            'Сучковою Єлизаветою')


def help_():
    QMessageBox.information(None, 'Допомога', 'fff')
    return 1


def lock():
    QMessageBox.information(None, 'Помилка доступу', 'Відмова в доступі')


