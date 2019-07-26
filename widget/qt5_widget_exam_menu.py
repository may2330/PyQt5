import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class MyApp(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.c1 = QCheckBox('짜장', self)
		self.c1.stateChanged.connect(self.change)

		self.c2 = QCheckBox('짬뽕', self)
		self.c2.stateChanged.connect(self.change)

		self.c3 = QCheckBox('탕수육', self)
		self.c3.stateChanged.connect(self.change)
		
		self.display = QLineEdit('')
		self.display.setReadOnly(True)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setMaxLength(15)		

		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(self.c1)
		hbox.addWidget(self.c2)
		hbox.addWidget(self.c3)
		hbox.addStretch(1)

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		vbox.addStretch(1)
		vbox.addWidget(self.display)
		vbox.addStretch(1)

		self.setLayout(vbox)		
		self.setWindowTitle('QCheckBox')
		self.setGeometry(300, 300, 300, 200)
		self.show()

	def change(self,state):
		text = ''
		if self.c1.isChecked() == True:
			text += self.c1.text()
		if self.c2.isChecked() == True:
			text += self.c2.text()
		if self.c3.isChecked() == True:
			text += self.c3.text()
		self.display.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

