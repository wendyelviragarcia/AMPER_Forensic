#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:26:25 2018

@author: weg
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def printHeatMap(corrMatrix, labels, max_value, file1, file2):
    fig, ax = plt.subplots()
    im = ax.imshow(corrMatrix)
    
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(labels, fontsize=6)
    ax.set_yticklabels(labels, fontsize=6)
    
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    
    # Labels in each square.
#    for i in range(len(labels)):
#        for j in range(len(labels)):
#            text = ax.text(j, i, corrMatrix[i, j],
#                           ha="center", va="center", color="w")
    
    ax.set_title("Higher corr "+ str(max_value) + " in file "+ labels[file1] + " and " + labels[file2] )
    fig.tight_layout()
    plt.savefig('resultsForensic/corr.png', dpi=300)
    
