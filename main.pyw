# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import selector_form


def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()    
    form = selector_form.Ui_Dialog()
    form.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
