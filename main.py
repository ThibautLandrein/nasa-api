# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:33:44 2022

@author: Thibaut Landrein
"""

KEY  = "jw3DGr4LVXclcsVm3IpG8RFnZfCHWWDMoNJqlHpe"

import requests
from urllib.request import urlopen
from pprint import PrettyPrinter
from datetime import datetime
from qtpy.QtWidgets import QLabel, QApplication, QWidget, QPushButton, QGridLayout, QDateEdit
from qtpy.QtGui import QPixmap

pp = PrettyPrinter()



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'NASA Picture of the day search'
        self.left = 300
        self.top = 200
        self.width = 1280
        self.height = 960
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.calendar = None
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.calendar = calendar = QDateEdit(self)
        calendar.setGeometry(100, 100, 10, 10)

        self.label = label = QLabel(self)
        static_label = QLabel(self)
        static_label.setText("Astronomy picture of the day : ")
        btn = QPushButton(self)
        btn.clicked.connect(self.display_picture)
        btn.setText("Lancer la recherche")
        
        self.layout.addWidget(calendar, 0, 0, 1, 1)
        self.layout.addWidget(btn, 0, 1, 1, 1)
        self.layout.addWidget(static_label, 1, 0, 1, 1)
        self.layout.addWidget(label, 2, 0, 1, 2)
    
    def _to_date(self):
        date = self.calendar.date()
        return f"{date.year()}-{date.month()}-{date.day()}"
    
    def display_picture(self):
        date = self._to_date()
        data = urlopen(get_picture_url(date)).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.label.setPixmap(pixmap)

def get_picture_url(date):
    """
    :param date: The date you want the picture of (Format: year-month-day)
    :type date: str
    """
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': KEY,
        'date': date,
        'hd':'True'
    }
    response = requests.get(URL_APOD,params=params).json()
    return response['url']

def get_today_picture_url():
    year, month, day, _hour, _min, _sec, _w, _y, _isdst = datetime.now().timetuple()
    return get_picture_url(f'{year}-{month}-{day}')

if __name__ == "__main__":

    app = QApplication([])
    displayer = App()
    displayer.show()
    app.exec_()
    
    

