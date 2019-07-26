import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

# 비율적으로 배치
# stretch(유연) 함
class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

	# 수평박스
        hbox = QHBoxLayout()
        hbox.addStretch(1) # 왼쪽비율
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1) # 오른쪽비율

	# 수직박스
        vbox = QVBoxLayout()
        vbox.addStretch(3) # 위쪽비율
        vbox.addLayout(hbox)
        vbox.addStretch(1) # 아래쪽비율

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
