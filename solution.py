import sys
import datetime

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class DiaryEvent():
    def __init__(self, d_time, info):
        self.d_time = d_time
        self.info = info

    def to_str(self):
        return f'{self.d_time} - {self.info}'

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ml.ui', self)  # Загружаем дизайн
        self.setWindowTitle('Минипланировщик')
        self.events = []
        self.pushButton.clicked.connect(self.add)



    def add(self):
        if self.lineEdit.text():
            t = datetime.datetime(self.cal.selectedDate().year(), self.cal.selectedDate().month(),
                                  self.cal.selectedDate().day(), self.timeEdit.time().hour(),
                                  self.timeEdit.time().minute())
            my_event = DiaryEvent(t, self.lineEdit.text())
            self.events.append(my_event)
            self.listWidget.clear()
            self.events = sorted(self.events, key=lambda x: x.d_time)
            self.listWidget.addItems([e.to_str() for e in self.events])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())