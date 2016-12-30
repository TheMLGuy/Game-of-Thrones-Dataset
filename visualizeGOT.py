# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 05:48:45 2016

@author: Ashwin
"""

import pandas as pd
import numpy as np
import matplotlib as plt
battlesdf=pd.read_csv('battles.csv')
chardeathdf=pd.read_csv('character-deaths.csv')
charpredictiondf=pd.read_csv('character-predictions.csv')

print(str(battlesdf.shape)+" "+str(chardeathdf.shape)+" "+str(charpredictiondf.shape))
print(battlesdf.keys())
print(chardeathdf.keys())
print(charpredictiondf.keys())