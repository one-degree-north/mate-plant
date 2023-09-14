from PyQt6.QtWidgets import QApplication

from gui import MainWindow
from comms import Comms

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow(Comms("/dev/cu.usbserial-B0005QMW"))
    window.show()

    app.exec()