from PyQt6.QtWidgets import QApplication, QMainWindow

from Baitap45.ui.MainWindow45Ext import MainWindow45Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow45Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
