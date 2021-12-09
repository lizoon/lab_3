import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def fill(win, cur_dir):
    win.catalog.clear()
    for dirs, folder, files in os.walk(cur_dir):
        return folder


def fill_files(win, cur_dir, s):
    if s == 'Folder':
        return ['x']
    win.files.clear()
    for dirs, folder, files in os.walk(cur_dir):
        index = s.find('.')
        s = s[index:-1]
        res = []
        for f in files:
            if s in f:
                res.append(f)
        return res


def show(list_dir, s, catalog):
    os.chdir('/home/liza/PycharmProjects/lab_3')
    for i in list_dir:
        item = QListWidgetItem(i)
        icon = QIcon(ico(s))
        item.setIcon(icon)
        catalog.addItem(item)


def ico(s):
    if s == 'All files [*.]':
        return 'icons/txt.jpg'
    if s == 'Folder':
        return 'icons/folder.jpg'
    if s == 'Doc files [*.doc]':
        return 'icons/doc.jpg'
    if s == 'Html files [*.html]':
        return 'icons/html.jpg'
    if s == 'JPG files [*.jpg]':
        return 'icons/jpeg.jpg'
    if s == 'Mp3 files [*.mp3]':
        return 'icons/mp3.jpg'
    if s == 'PDF files [*.pdf]':
        return 'icons/pdf.jpg'
    if s == 'Py files [*.py]':
        return 'icons/py.jpg'
    if s == 'Text files [*.txt]':
        return 'icons/txt.jpg'
    if s == 'Xsl files [*.xsl]':
        return 'icons/xsl.jpg'
    if s == 'ZIP files [*.zip]':
        return 'icons/zip.jpg'


