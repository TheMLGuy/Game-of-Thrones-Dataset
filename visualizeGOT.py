# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 05:48:45 2016

@author: Ashwin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
battlesdf=pd.read_csv('battles.csv')
chardeathdf=pd.read_csv('character-deaths.csv')
charpredictiondf=pd.read_csv('character-predictions.csv')

print(str(battlesdf.shape)+" "+str(chardeathdf.shape)+" "+str(charpredictiondf.shape))
print("Lets observe the keys and first rows of each csv file")
print(battlesdf.keys())
print(chardeathdf.keys())
print(charpredictiondf.keys())
print("------------------------------------------------------------------------------")
print(battlesdf.head(1))
print("------------------------------------------------------------------------------")
print(chardeathdf.head(1))
print("------------------------------------------------------------------------------")
print(charpredictiondf.head(1))
print("------------------------------------------------------------------------------")
#How many battles/year-plot battles/year
plt.xlabel('Year')
plt.ylabel('Number of battles')
plt.title('Battles/Year')
plt.ylim([1,25])
plt.margins(0.01)
plt.hist(battlesdf['year'],10)
plt.show()

#How many times has each defending king been attacked and by whom
print("Stronghold defenses")
print(battlesdf['defender_1'].value_counts())

plt.xlabel('Names of kings')
plt.ylabel('No of times attacked')
plt.title('Stronghold defenses')
defenderDF=pd.DataFrame(battlesdf['defender_1'].value_counts().reset_index())
defenderDF.columns=['king','defenseCount']
defenderDF['ind']=range(1,len(defenderDF)+1)
print(defenderDF)
plt.bar(defenderDF['ind'],defenderDF['defenseCount'],alpha=0.4)
plt.xticks(defenderDF['ind'],defenderDF['king'],rotation='vertical')
plt.tight_layout()
plt.show()

#Attacker combo vs Defense King
battlesdf['attackCombo']=battlesdf[['attacker_1','attacker_2','attacker_3','attacker_4']].apply(lambda x: '/'.join(x.dropna()),axis=1)
whichKingGotAttacked=[(x,y) for x,y in battlesdf[['attackCombo','defender_king']].values if(pd.isnull(x)==False) and pd.isnull(y)==False]
print(whichKingGotAttacked) 
defvsatt=pd.DataFrame(whichKingGotAttacked)
defvsatt.columns=['Attack Combination','Defender King']
#attacker combinations
plt.bar(range(1,len(defvsatt['Attack Combination'].value_counts().index)+1),defvsatt['Attack Combination'].value_counts())
plt.xticks(range(1,len(defvsatt['Attack Combination'].value_counts().index)+1),defvsatt['Attack Combination'].value_counts().index.tolist(),rotation='vertical')
plt.show()
#defender combinations
plt.bar(range(1,len(defvsatt['Defender King'].value_counts().index)+1),defvsatt['Defender King'].value_counts())
plt.xticks(range(1,len(defvsatt['Defender King'].value_counts().index)+1),defvsatt['Defender King'].value_counts().index.tolist(),rotation='vertical')
plt.show()