from PyQt5.QtWidgets import QApplication, QWidget

import sys

def application():
    app = QApplication(sys.argv)
    window = QWidget()

    window.setWindowTitle("Умные заметки")
    window.setGeometry(300, 250, 350, 200)

    window.show()
    sys.exit(app.exec_())


application()
