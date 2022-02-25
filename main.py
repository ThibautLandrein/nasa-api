# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:33:44 2022

@author: Thibaut Landrein
"""

KEY  = "jw3DGr4LVXclcsVm3IpG8RFnZfCHWWDMoNJqlHpe"

import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
from datetime import datetime
pp = PrettyPrinter()


def get_picture(date):
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
    pp.pprint(response)

def get_today_picture():
    year, month, day, _hour, _min, _sec, _w, _y, _isdst = datetime.now().timetuple()
    get_picture(f'{year}-{month}-{day}')
    
get_today_picture()