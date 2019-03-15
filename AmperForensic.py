#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 18:17:16 2018

@author: weg
"""


import os
from readAmperPitch import readAmperPitch
from visualResults import printHeatMap
#from visualResults_plotly import printHeatMap
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt


#cwd = os.getcwd()
#dataFolder = 'data'
#dataFolder= os.path.join(cwd,dataFolder)





#dataFolder = '/Users/weg/OneDrive - Universitat de Barcelona/ProDis/ProDisData'
#dataFolder = 'C:/Users/labfonub99/OneDrive - Universitat de Barcelona/2019_homenaje-trudel/forenseF0/data'
dataFolder = '../DBase_Amper_Forensic'


allPitches = list()
usedFiles = list()

for subdir, dirs, files in os.walk(dataFolder):
    for file in files:
        # analyse only one file pwt first repetition
        if file[4:7] == "pwp" and (file[7]=="i" or file[7]=="m") and file[8]=="1":
            myFile = os.path.join(subdir, file)
            pitch = readAmperPitch(myFile)
            allPitches.append(pitch)
            usedFiles.append(file)


allPitches= np.array(allPitches)

index = 0
labels = list()

for code in usedFiles:
    currentCode = str(code[0:4])
    labels.append(currentCode)
    
    
   


corr = np.corrcoef(allPitches)
table = np.column_stack((usedFiles,corr))
#meanCorrBetweenTwoSentences = np.mean(corr)
np.savetxt('resultsForensic/corrMatrix.txt',table, fmt="%s", delimiter = '\t', header = str(usedFiles))

#Get max corr without the diagonals (to which is more similar)
mask = np.ones(corr.shape, dtype=bool)
np.fill_diagonal(mask, 0)
max_value = corr[mask].max()


chosen = np.where(corr==max_value)
file1=int(chosen[0][1])
file2=int(chosen[1][1])



print ("Higher corr "+ str(max_value)+ " in file " + labels[file1] + " and " + labels[file2])

printHeatMap(corr, labels, max_value, file1, file2)

fig = plt.figure()
indexPlot = 1
for locale in labels:
    
    localeData =dict(zip(labels, corr[indexPlot-1]))
    sorted_localeData = sorted(localeData.items(), key=itemgetter(1), reverse=True)
    np.savetxt('resultsForensic/' + locale +'.txt',sorted_localeData, fmt="%s", delimiter = '\t')
    
    values = list(zip(*sorted_localeData))[1]
    labelsOrd = list(zip(*sorted_localeData))[0]
    ax = fig.add_subplot(len(labels)/3, 3, indexPlot)
    
    ax.imshow(np.asmatrix(values))
    ax.set_xticks(np.arange(len(labelsOrd)))
    ax.set_xticklabels(labelsOrd, fontsize=6)
    
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    indexPlot = indexPlot +1
    
#plt.show()
plt.savefig('resultsForensic/ordered.png', dpi=300)

################## imagen una a uno
indexPlot = 1
for locale in labels:
    fig = plt.figure()
    localeData =dict(zip(labels, corr[indexPlot-1]))
    sorted_localeData = sorted(localeData.items(), key=itemgetter(1), reverse=True)
    np.savetxt('resultsForensic/' + locale +'.txt',sorted_localeData, fmt="%s", delimiter = '\t')
    
    values = list(zip(*sorted_localeData))[1]
    labelsOrd = list(zip(*sorted_localeData))[0]
    ax = fig.add_subplot(1, 1, 1)
    
    ax.imshow(np.asmatrix(values))
    ax.set_xticks(np.arange(len(labelsOrd)))
    ax.set_xticklabels(labelsOrd, fontsize=6)
    
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    indexPlot = indexPlot +1
    plt.savefig('resultsForensic/ordered_'+labelsOrd[0]+'.png', dpi=300)
#plt.show()
