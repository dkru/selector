# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import ctypes
from PyQt4 import QtGui, QtCore
import selector_form

def appIcon():
    appIcon = QtGui.QIcon()
    appIcon.addFile('icons/student_512.png', QtCore.QSize(512,512))
    appIcon.addFile('icons/student_256.png', QtCore.QSize(256,256))
    appIcon.addFile('icons/student_128.png', QtCore.QSize(128,128))
    appIcon.addFile('icons/student_64.png', QtCore.QSize(64,64))
    appIcon.addFile('icons/student_32.png', QtCore.QSize(32,32))
    appIcon.addFile('icons/student_24.png', QtCore.QSize(24,24))
    appIcon.addFile('icons/student_16.png', QtCore.QSize(16,16))
    return appIcon

def main():
    myappid = 'EOG.deepblue.selector.1_1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()    
    mainWindow.setWindowIcon(appIcon())

    form = selector_form.Ui_Dialog()
    form.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
