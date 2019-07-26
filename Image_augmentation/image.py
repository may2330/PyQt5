import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os.path import *
import imghdr
from PIL import Image

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.error = 1
        self.resize = -1
        self.rotate = -1
        self.hflip = -1
        self.vflip = -1
        self.name = -1

        self.initUI()

    def initUI(self):

        # 폴더
        self.line_folder = QLineEdit(self)
        button_folder = QPushButton("폴더선택")
        self.label_folder = QLabel()

        hbox_folder = QHBoxLayout()
        hbox_folder.addWidget(button_folder)
        hbox_folder.addWidget(self.line_folder)

        error_folder = QHBoxLayout()
        error_folder.addStretch(1)
        error_folder.addWidget(self.label_folder)
        error_folder.addStretch(1)

        vbox_folder = QVBoxLayout()
        vbox_folder.addLayout(hbox_folder)
        vbox_folder.addLayout(error_folder)

        button_folder.clicked.connect(self.clickFileButton)
        self.line_folder.textChanged[str].connect(self.checkFolderPath)

        # 옵션
        grid = QGridLayout()
        grid.addWidget(self.createOptionGroup())

        # 전송 버튼
        sendBtn = QPushButton("send")
        sendBtn.clicked.connect(self.makeImage)

        hbox_send = QHBoxLayout()
        hbox_send.addStretch(1)
        hbox_send.addWidget(sendBtn)

        # 전체 틀
        total_v = QVBoxLayout()
        total_v.addLayout(vbox_folder)
        total_v.setSpacing(20)
        total_v.addLayout(grid)
        total_v.setSpacing(10)
        total_v.addLayout(hbox_send)

        self.setLayout(total_v)

        # 윈도우 창
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def checkFolderPath(self, text):
        list = ['jpg', 'png', 'gif', 'jpeg']

        if(isfile(text)): # exists : 경로있는지 isfile : 파일인지
            ext = imghdr.what(text) # 확장명
            if(ext in list):
                self.label_folder.setText("<font color='green'>Path OK</font>")
                self.error = 0
                return 0

        self.label_folder.setText("<font color='red'>Path Error</font>")
        self.error = 1

    def clickFileButton(self):
        fileName = QFileDialog.getOpenFileName(self)
        self.line_folder.setText(fileName[0])

    def createOptionGroup(self):
        groupbox = QGroupBox('OPTION')

        H_Flip = QCheckBox('H_Flip')
        V_Flip = QCheckBox('V_Flip')

        # 함수
        H_Flip.clicked.connect(self.hFlipState)
        V_Flip.clicked.connect(self.vFlipState)

        # Flip 틀
        vbox = QVBoxLayout()
        vbox.addWidget(self.createResizeGroup())
        vbox.setSpacing(10)
        vbox.addWidget(self.createRotateGroup())
        vbox.setSpacing(10)
        vbox.addWidget(H_Flip)
        vbox.setSpacing(10)
        vbox.addWidget(V_Flip)
        vbox.addWidget(self.createNameGroup())
        groupbox.setLayout(vbox)

        return groupbox

    def createResizeGroup(self):
        groupbox = QGroupBox('Resize')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        groupbox.setFlat(True)

        groupbox.clicked.connect(self.resizeState)

        label_resize_w = QLabel('Width')
        label_resize_h = QLabel('Height')
        self.line_resize_w = QSpinBox(self)
        self.line_resize_h = QSpinBox(self)
        self.line_resize_w.setRange(1,1920)
        self.line_resize_h.setRange(1,1680)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label_resize_w)
        hbox.addWidget(self.line_resize_w)
        hbox.setSpacing(15)
        hbox.addWidget(label_resize_h)
        hbox.addWidget(self.line_resize_h)
        hbox.addStretch(1)
        groupbox.setLayout(hbox)

        return groupbox

    def createRotateGroup(self):
        groupbox = QGroupBox('Rotate')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        groupbox.setFlat(True)

        groupbox.clicked.connect(self.rotateState)

        label_rotate = QLabel('Angle Number', self)
        self.line_rotate = QSpinBox(self)
        self.line_rotate.setRange(0,360)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label_rotate)
        hbox.setSpacing(15)
        hbox.addWidget(self.line_rotate)
        hbox.addStretch(1)
        groupbox.setLayout(hbox)

        return groupbox

    def createNameGroup(self):
        groupbox = QGroupBox('Rename')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)
        groupbox.setFlat(True)

        groupbox.clicked.connect(self.renameState)

        front = QLabel('Prefix', self)
        back = QLabel('Suffix', self)
        self.line_front = QLineEdit(self)
        self.line_back = QLineEdit(self)

        hbox = QHBoxLayout()
        hbox.addWidget(front)
        hbox.addWidget(self.line_front)
        hbox.setSpacing(10)
        hbox.addWidget(back)
        hbox.addWidget(self.line_back)
        groupbox.setLayout(hbox)

        return groupbox

    # 체크박스 상태 확인
    def resizeState(self):
        self.resize *= -1
        print("resize",self.resize)

    def rotateState(self):
        self.rotate *= -1
        print("rotate",self.rotate)

    def hFlipState(self):
        self.hflip *= -1
        print("hFlip",self.hflip)

    def vFlipState(self):
        self.vflip *= -1
        print("vFlip",self.vflip)

    def renameState(self):
        self.name *= -1
        print("rename",self.name)

    def makeImage(self):
        print("Change Image")
        if(self.error==0):
            self.img = Image.open(self.line_folder.text())
            if(self.resize==1):
                self.makeResize()
            if(self.rotate==1):
                self.makeRotate()
            if(self.hflip==1):
                self.makeHFlip()
            if(self.vflip==1):
                self.makeVFlip()
            self.imageSave()
            return 0
        self.label_folder.setText("<font color='red'>Path Error</font>")

    def makeResize(self):
        print("Make Resize")
        print((self.line_resize_w.text(), self.line_resize_h.text()))
        self.img = self.img.resize((int(self.line_resize_w.text()), int(self.line_resize_h.text())))

    def makeRotate(self):
        print("Make Rotate")
        print(self.line_rotate)
        self.img = self.img.rotate(int(self.line_rotate.text()))

    def makeHFlip(self):
        print("Make H-Flip")
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)

    def makeHFlip(self):
        print("Make H-Flip")
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)

    def makeVFlip(self):
        print("Make V-Flip")
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)

    def imageSave(self):
        if(self.name == 1):
            print(imghdr.what(self.line_folder.text()))
            path = dirname(self.line_folder.text())+ "/"+self.line_front.text() + self.line_back.text()+"."+imghdr.what(self.line_folder.text())
        else:
            path = self.line_folder.text()
        print(path)
        self.img.save(path)
        self.showAlert()

    def showAlert(self):
        ok = QMessageBox()
        ok.setIcon(QMessageBox.Information)
        ok.setWindowTitle("OK")
        ok.about(self, "Message", "Save Success!!!!!!!!")

    def alertClose(self):
        print()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())