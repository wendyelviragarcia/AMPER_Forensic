#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 14:57:26 2018

@author: weg
"""

#import numpy as np



def readAmperPitch(txt_path):
    with open(txt_path) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    
    content = content[5:len(content)-3]
    
    pitch=[]
    for line in range(0,len(content)-1):
        tmp= str.split(content[line], "\t")
        tmp= tmp[6:]
        pitch.extend(tmp)
        
    #all tmp were str transform into floats
    #necesario para python 2
    #pitch= map(float, pitch)
    #version py 3
    pitch= list(map(float, pitch))
    
    return pitch
