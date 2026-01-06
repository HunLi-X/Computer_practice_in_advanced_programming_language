#PyQt5,windwos风格应用程序

import sys
from PyQt5.QtWidgets import *
app =QApplication(sys.argv)
mywidget = QWidget()
mywidget.setGeometry(200,200,600,300)
mywidget.setWindowTitle('Hello PyQt5 !')
mywidget.show()
sys.exit(app.exec_())

