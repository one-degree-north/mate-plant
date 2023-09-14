from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from threading import Thread

class MainWindow(QMainWindow):
    def __init__(self, comms):
        super().__init__()
        self.comms = comms

        self.box = QWidget()
        self.box.layout = QVBoxLayout()
        self.box.setLayout(self.box.layout)
        self.setCentralWidget(self.box)

        self.button = QPushButton("GIVE ME WATER")
        self.button.clicked.connect(self.button_event)
        self.button.setStyleSheet("""
            QPushButton {
                background: darkgreen;
                color: white;
                font-weight: 600;
                border-radius: 5px;
                padding: 5px;
            }
                                  
            QPushButton::hover {
                background: green;
            }
        """)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: darkgreen;
                font-size: 28px;
                font-weight: 600;
            }
        """)

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