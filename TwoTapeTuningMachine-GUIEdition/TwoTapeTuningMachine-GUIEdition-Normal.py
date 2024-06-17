import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt

class TuringMachine(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tape1 = ['B', 'a', 'b', 'b', 'c', 'a', 'a', 'b', 'B']
        self.tape2 = ['B']
        self.head1 = 1
        self.head2 = 1
        self.simulation_started = False
        self.compare_mode = False

        self.initUI()

    def initUI(self):
        self.setFixedSize(200, 200) 
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)  
        self.label1 = QLabel("Tape 1: " + ' '.join(self.tape1))
        self.label2 = QLabel("Head 1: " + ' '.join(['  ']*self.head1) + '^')

        self.label3 = QLabel("Tape 2: " + ' '.join(self.tape2))
        self.label4 = QLabel("Head 2: " + ' '.join(['  ']*self.head2) + '^')

        self.result_label = QLabel("Result: ")
        self.result_label.setStyleSheet("color: black")

        self.start_button = QPushButton("Start Simulation", self)
        self.start_button.clicked.connect(self.startSimulation)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        layout.addWidget(self.result_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.quit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateSimulation)

    def startSimulation(self):
        if not self.simulation_started:
            self.simulation_started = True
            self.timer.start(500)
            self.start_button.setEnabled(False)  

    def updateSimulation(self):
        if not self.compare_mode:
            if self.head1 < len(self.tape1) and (self.tape1[self.head1] == 'a' or self.tape1[self.head1] == 'b'):
                self.tape2.append(self.tape1[self.head1])
                self.head1 += 1
                self.head2 += 1
                self.updateTapes()
            else:
                self.tape2.append('B')
                if self.head1 < len(self.tape1) and self.tape1[self.head1] == 'c':
                    self.head1 += 1
                    self.head2 = 1
                    self.compare_mode = True
                    self.updateTapes()
                else:
                    self.result_label.setText("Result: Language denied")
                    self.result_label.setStyleSheet("color: red")
                    self.timer.stop()
                    self.simulation_started = False
        else:
            if self.head1 < len(self.tape1) and self.head2 < len(self.tape2) and self.tape1[self.head1] == self.tape2[self.head2]:
                self.head1 += 1
                self.head2 += 1
                self.updateTapes()
                if self.tape1[self.head1] == 'B' and self.tape2[self.head2] == 'B':
                    self.result_label.setText("Result: Language Succeeded")
                    self.result_label.setStyleSheet("color: green")
                    self.timer.stop()
                    self.simulation_started = False
            else:
                self.result_label.setText("Result: Language Denied")
                self.result_label.setStyleSheet("color: red")
                self.timer.stop()
                self.simulation_started = False

    def updateTapes(self):
        self.label1.setText("Tape 1: " + ' '.join(self.tape1))
        self.label2.setText("Head 1: " + ' '.join(['  ']*self.head1) + '^')
        self.label3.setText("Tape 2: " + ' '.join(self.tape2))
        self.label4.setText("Head 2: " + ' '.join(['  ']*self.head2) + '^')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tm = TuringMachine()
    tm.show()
    sys.exit(app.exec_())
