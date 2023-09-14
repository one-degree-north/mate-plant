from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from threading import Thread

class MainWindow(QMainWindow):
    def __init__(self, comms):
        super().__init__()
        self.comms = comms

        self.box = QWidget()
        self.box.layout = QVBoxLayout()
        self.box.setLayout(self.box.layout)
        self.setCentralWidget(self.box)

        self.button = QPushButton("hola")
        self.button.clicked.connect(self.button_event)

        self.label = QLabel()

        self.box.layout.addWidget(self.label)
        self.box.layout.addWidget(self.button)

        t1 = Thread(target=self.beginRead)
        t1.start()

    def button_event(self):
        self.comms.send()

    def beginRead(self):
        while True:
            self.label.setText(self.comms.read())

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()