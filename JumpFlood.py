# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:06:18 2021
Implementation of the Jump Flood Algorithm (JFA)
@author: bentdoug
"""

import matplotlib.pyplot as plt
import numpy as np
import math

## x and y dimensions of the table being filled
row = 10
col = 10

##Color value of the starting point
color1 = 20

##graph to be filled in
arr1 = np.zeros((row, col))

##list of already filled points
arrlisted = []

##Assigning the value of the original point
arr1[5,5] = 20


limx = row
limy = col

##Starting step length
step = 5

##Adding initial point to arrlisted
arrlisted.append([5,5])

##array used to efficiently look at a points neighbors
moves = [1, -1, 0]

##counter used when naming each image to be saved (figure number)
fignum = 0

##Creating and saving figure
plt.imshow(arr1)
plt.xlabel("X")
plt.ylabel("Y")
plt.clim(0,20)
plt.savefig(str(fignum)+ "jfa.png", dpi = 300)
plt.show()
fignum+=1


while step > 0:
    
    ##loop through each filled site 
    for seed in arrlisted:
        x = seed[0]
        y = seed[1]
        
        ##loop through each of this points 8 neighbors at a certain distance away
        for i in moves:
            for j in moves:
                
                a = x+(step*i)
                b = y+(step*j)
                
                ##if this neighbor point is within the bounds of the graph
                if 0 <= a < limx and 0 <= b < limy:
                    
                    ##if this neighbor point is empty -> fill and add to arrlisted
                    if arr1[a, b] == 0:
                        arr1[a, b] = 20
                        arrlisted.append([a, b])
                        
                        ##create and save image
                        plt.imshow(arr1)
                        plt.xlabel("X")
                        plt.ylabel("Y")
                        plt.clim(0,20)  
                        fignum+=1
                        plt.savefig(str(fignum)+ "jfa.png", dpi = 300)
                        plt.show()
        
        fignum+=1               
                        
    step //= 2
    

    
