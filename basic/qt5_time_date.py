# 현재 날짜 출력
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate() # 현재 날짜 반환
print(now.toString())

# 날짜 형식 설정
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))


# 시간 표시
from PyQt5.QtCore import QTime

time = QTime.currentTime() # 현재 시간 반환
print(time.toString())

# 시간 형식 설정
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))


# 날짜와 시간 표시
from PyQt5.QtCore import QDateTime

datetime = QDateTime.currentDateTime()
print(datetime.toString())

# 날짜와 시간 형식 설정
print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))
