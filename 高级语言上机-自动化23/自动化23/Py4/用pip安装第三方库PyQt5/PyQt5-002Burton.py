#PyQt5,windwos风格应用程序

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)
exp = QWidget()
qtn = QPushButton('退出Q',exp)
qtn.resize(qtn.sizeHint())
qtn.clicked.connect(QCoreApplication.quit)
qtn.move(70,40)

exp.setGeometry(600,600,200,100)
exp.setWindowTitle('Hello PyQt5-002 按钮=退出窗体')
exp.show()
sys.exit(app.exec_())

