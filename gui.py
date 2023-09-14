from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, comms):
        super().__init__()
        self.comms = comms

        self.box = QWidget()
        self.box.layout = QVBoxLayout()
        self.box.setLayout(self.box.layout)

        self.button = QPushButton("hola")
        self.button.clicked.connect(self.button_event)

        self.box.layout.addWidget(self.button)

        self.setCentralWidget(self.box)

    def button_event(self):
        self.comms.send()

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()