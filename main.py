# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:33:44 2022

@author: Thibaut Landrein
"""

KEY  = "jw3DGr4LVXclcsVm3IpG8RFnZfCHWWDMoNJqlHpe"

import requests
from urllib.request import urlretrieve, urlopen
from pprint import PrettyPrinter
from datetime import datetime
from qtpy.QtWidgets import QLabel, QApplication, QWidget
from qtpy.QtGui import QPixmap
pp = PrettyPrinter()



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap()
        data = data = urlopen(get_today_picture_url()).read()
        pixmap.loadFromData(data)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())


def get_picture_url(date):
    """
    :param date: The date you want the picture of (Format: year-month-day)
    :type date: str
    """
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key':KEY,
        'date':date,
        'hd':'True'
    }
    response = requests.get(URL_APOD,params=params).json()
    # pp.pprint(response)
    return response['url']

def get_today_picture_url():
    year, month, day, _hour, _min, _sec, _w, _y, _isdst = datetime.now().timetuple()
    return get_picture_url(f'{year}-{month}-{day}')

if __name__ == "__main__":

    app = QApplication([])
    displayer = App()
    displayer.show()
    app.exec_()
    
    

