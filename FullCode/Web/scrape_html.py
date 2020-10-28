# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:47:48 2020

@author: egayu
"""

import urllib.request

url = urllib.request.urlopen('https://www.yahoo.com')

print("Result code: ", str(url.getcode()))

print(url.read())