#RATATATA EEEEEEUGGGGGGGGHHHHHHHHH
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QGroupBox, QButtonGroup, QRadioButton, QPushButton)
from random import *
#skibidi
APK = QApplication([])
WINDOW = QWidget()
WINDOW.setFixedSize(400,400)

#widget
SOAL = QLabel("CONTOH SOAL")
RADIO1 = QRadioButton("A")
RADIO2 = QRadioButton("B")
RADIO3 = QRadioButton("C")
RADIO4 = QRadioButton("D")
GROUPRADIO = QGroupBox("options")
BUTTON = QPushButton('ANSWER')

GRUPHASIL = QGroupBox('HASIL')
BENARSALAH = QLabel('BENAR/SALAH')
BENAR = QLabel('JAWABAN BENAR')

#grup hasil (miau :3)
garisgruphasil = QVBoxLayout()
garisgruphasil.addWidget(BENARSALAH)
garisgruphasil.addWidget(BENAR,alignment=Qt.AlignHCenter)
GRUPHASIL.setLayout(garisgruphasil)

#tata letak
garisv = QVBoxLayout()
garish1 = QHBoxLayout()
garish2 = QHBoxLayout()
garish1.addWidget(RADIO1)
garish1.addWidget(RADIO2)
garish2.addWidget(RADIO3)
garish2.addWidget(RADIO4)
garisv.addLayout(garish1)
garisv.addLayout(garish2)
GROUPRADIO.setLayout(garisv)

#tata letak jendela
garisutama = QVBoxLayout()
garisutama.addWidget(SOAL, alignment=Qt.AlignHCenter)
garisutama.addWidget(GROUPRADIO)
garisutama.addWidget(GRUPHASIL)
garisutama.addWidget(BUTTON)
WINDOW.setLayout(garisutama)

#sembunyi
GROUPRADIO.show()
GRUPHASIL.hide()

#kelompok radio button
group = QButtonGroup()
group.addButton(RADIO1)
group.addButton(RADIO2)
group.addButton(RADIO3)
group.addButton(RADIO4)

class Question:
    def __init__(self, soal, benar, salah1, salah2, salah3):
        self.soal = soal
        self.benar = benar
        self.salah1 = salah1
        self.salah2 = salah2
        self.salah3 = salah3
LISTSOAL = list()        
LISTSOAL.append(Question('2 x (5 - 3) =_______' , '4','3','10','7'))
LISTSOAL.append(Question('1 + 1 = _______' , '2','jendela','11','gak tau'))
LISTSOAL.append(Question('4 - 3 + 10 = _______' , '11','7','2','4'))
LISTSOAL.append(Question('13 x 11 = _______' , '143','333','112','133'))
LISTSOAL.append(Question('80 : 4 = _______' , '20','2','10','8'))
LISTSOAL.append(Question('2 + 2 =_______' , '4','44','444','4444'))
LISTSOAL.append(Question('3 x 4 - 2 = _______' , '10','12','11','13'))
LISTSOAL.append(Question('22 : 2 = _______' , '11','2','10','22'))
LISTSOAL.append(Question('100 : 5 = _______' , '20','21','5','2'))
LISTSOAL.append(Question('4 - 2 = _______' , '2','22','1','99999'))

WINDOW.total = 0
WINDOW.total_benar = 0
WINDOW.total_salah = 0

#event handling
def show_result():
    GROUPRADIO.hide()
    GRUPHASIL.show()
    BUTTON.setText('Next Question')

def show_question():
    GROUPRADIO.show()
    GRUPHASIL.hide()
    BUTTON.setText('ANSWER')
    #reset
    group.setExclusive(False)
    RADIO1.setChecked(False)
    RADIO2.setChecked(False)
    RADIO3.setChecked(False)
    RADIO4.setChecked(False)
    group.setExclusive(True)


def okokok():
    if BUTTON.text() == 'ANSWER':
        check()
    else:
        next()

LISTRADIO = [RADIO1,RADIO2,RADIO3,RADIO4]
def ask(objek_soal):
    shuffle(LISTRADIO)
    LISTRADIO[0].setText(objek_soal.benar)
    LISTRADIO[1].setText(objek_soal.salah1)
    LISTRADIO[2].setText(objek_soal.salah2)
    LISTRADIO[3].setText(objek_soal.salah3)
    SOAL.setText(objek_soal.soal)
    BENAR.setText(objek_soal.benar)
    show_question()

def check():
    if LISTRADIO[0].isChecked():
        BENARSALAH.setText('BENARR')
        WINDOW.total_benar += 1
    else:
        BENARSALAH.setText('SALAHH')
        WINDOW.total_salah += 1
    show_result()
    print('-----------------')
    print('BENAR =',WINDOW.total_benar)
    print('SALAH =',WINDOW.total_salah)
    print('PERSENTASE = ',(WINDOW.total_benar / WINDOW.total) * 100 , '%')

WINDOW.count = -1 
def next():
    WINDOW.total += 1
    print('-----------------')
    print('TOTAL SOAL =',WINDOW.total)
    count = randint(0, len(LISTSOAL)-1)
    ask(LISTSOAL[count])

next()

BUTTON.clicked.connect(okokok)

#window show, sigma
WINDOW.show()
APK.exec_()