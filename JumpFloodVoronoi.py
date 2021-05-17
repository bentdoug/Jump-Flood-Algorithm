# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:37:01 2021
Implementation of the Jump-Flood Algorithm (JFA) adapted to create Voronoi Diagrams
@author: bentdoug
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import random

def JFA_Voronoi(row, col, seedlist):
    """
    
    Create Voronoi Diagram Utalizing an implementation
    of the Jump Flood Algorithm that does not use GPU
    
    row:
        x-axis resolution (how many points desired in x-axis)
    col:
        y-axis resolution (how many points desired in y-axis)
    seedlist:
        list of seed points [[x-coord, ycoord]]
        
    """
    
    #Dictionary = Key: Value of a point in arr1 (Corresponding to Color) -> 
    #Value: Origin point of that color value (Original Voronoi Site)
    seeds = {}
    
    #graph to be filled in with Voronoi Diagram
    arr1 = np.zeros((row, col))
    
    #list of already filled points (Current Voronoi Sites)
    arrlisted = []
    
    #setting initial step length to half the dimensions of the grid
    step = col//2
    
    #divides the color limit of the graph by the number of intial seeds (Voronoi Sites)
    #this is the distance between each color value
    numseeds = len(seedlist)
    numasigncalc = 40/numseeds
    numpoint = 1
    
    #Filling arrlisted, calculates and assigns color value, inputs this data to
    #seeds and arr1
    for point in seedlist:
        arrlisted.append(point)
        value = (numasigncalc*numpoint)
        seeds.update({value: point})
        numpoint+=1
        arr1[point[0], point[1]] = value
    
    #counter used when naming each image to be saved (figure number)
    fignum = 0
    
    #array used to efficiently look at a points neighbors
    moves = [1, -1, 0]
    
    #Creates and saves initial image
    plt.imshow(arr1)
    plt.clim(0,40)
    plt.savefig("JFAVoronoi" + str(fignum)+ ".png", dpi = 300)
    fignum+=1
    plt.show()
    
    #JFA adapted to create Voronoi Diagrams
    while step > 0:
        
        #loop through each filled site (Voronoi Sites)
        for seed in arrlisted:
            x = seed[0]
            y = seed[1]
            val = arr1[x, y]
            
            #loop through each of this points 8 neighbors at a certain distance away
            for i in moves:
                for j in moves:
                    a = x+(step*i)
                    b = y+(step*j)
                    
                    #if this neighbor point is within the bounds of the graph
                    if 0 <= a < row and 0 <= b < col:
                        
                        #if this neighbor point is not equal to the Voronoi Site it is
                        #the neighbor of
                        if arr1[a,b] != val:
                            
                            #if this neighbor point is empty -> fill and add to arrlisted
                            if arr1[a, b] == 0:
                                arr1[a, b] = val
                                arrlisted.append([a, b])
                                
                            #else -> compute the distances from this neighbor point and
                            #its current origin point as well as from this neighbor point
                            #to the current Voronoi Site's origin point (in dictionary; seeds)
                            else:
                                ##location of seed associated with this points value
                                loc1 = seeds[arr1[a,b]]
                                ##location of the seed trying to replace this points value
                                loc2 = seeds[val]
                                ##Calculating Distances
                                ##distance from seed already connected to this point to the point
                                dist1 = math.sqrt( ((loc1[0]-a)**2)+((loc1[1]-b)**2) )
                                ##distance  from seed trying to replace previous to this point
                                dist2 = math.sqrt( ((loc2[0]-a)**2)+((loc2[1]-b)**2) )
                                ##if dist2 is less than dist1, change the points value to that new seeds value
                                ##else do nothing at this point
                                if dist2 < dist1:
                                    arr1[a,b] = val
                                        
                            #Saving each image
                            plt.imshow(arr1)
                            plt.clim(0,40)  
                            fignum+=1
                            plt.savefig("JFAVoronoi" + str(fignum)+ ".png", dpi = 300)
                            plt.show()
        
        step //= 2


def face(x, y):
    """

    Calculates points to fill in order to plot a smiley-face on a graph of
    x and y dimensions
    
    Parameters
    ----------
    
    x:
        x-axis resolution (how many points desired in x-axis)
    y:
        y-axis resolution (how many points desired in y-axis)

    Returns
    -------
    seedlist : the neccessary points in a shuffled order as to ensure most points
    do not get assigned the same color value as their neighbor

    """
    
    #list of seed locations to be filled and returned
    seedlist = []
    
    #calculates a the value of a third and a sixth of the dimensions of the grid
    #to be used in calculating location of points
    third = x//3
    sixth = x//6
    
    #calculates points that will create two lines to represent eyes and adds those
    #points to seedlist
    for x in range(third):
        seedlist.append([third+x, third])
        seedlist.append([third+x, 2*third])
    #calculates points that will create the vertical sides of the face's mouth
    # and adds those points to seedlist
    for x in range(sixth):
        seedlist.append([x + 5*sixth, sixth])
        seedlist.append([x + 5*sixth, sixth*5])
    
    #calculates points that will create the horizontal portion of the face's mouth
    #and adds those points to seedlist
    for x in range(2*third):
        seedlist.append([47, sixth+x])
    
    #shuffles the order of these seeds in seedlist
    random.shuffle(seedlist)
    
    return seedlist
    
def square(x, y):
    """
    Calculates points to fill in order to plot a square on a graph of
    x and y dimensions

    Parameters
    ----------
    
    x:
        x-axis resolution (how many points desired in x-axis)
    y:
        y-axis resolution (how many points desired in y-axis)

    Returns
    -------
    seedlist : the neccessary points for the square

    """
    seedlist = []
    third = x//3
    sixth = x//6
    for x in range(third):
        seedlist.append([third+x, third])
        seedlist.append([third+x, 2*third])
    for x in range(third):
        seedlist.append([third, third+x])
        seedlist.append([2*third, third+x])
        
    return seedlist

def thankyou(x, y):
    """
    Calculates points to fill in order to plot "thank you" on a graph of
    x and y dimensions

    Parameters
    ----------
    
    x:
        x-axis resolution (how many points desired in x-axis)
    y:
        y-axis resolution (how many points desired in y-axis)

    Returns
    -------
    seedlist : the neccessary points to write "thank you"

    """
    seedlist = []
    ##T
    for x in range(400):
        seedlist.append([50+x, 100])
        
    for x in range(100):
        seedlist.append([50, x+50])
        
    ##H
    
    for x in range(400):
        seedlist.append([50+x, 200])
        seedlist.append([50+x, 300])
        
    for x in range(100):
        seedlist.append([250, 200+x])
        
    ##A
    
    x = 450
    x2 = 450
    y = 50
    ctr = 0
    while y <=450:
        seedlist.append([y, x])
        seedlist.append([y, x2])
        y += 1
        ctr+=1
        if ctr%4 == 0:
            x+=1
            x2-=1
    
    for x in range(100):
        seedlist.append([250, 400+x])
        
    ##N
    
    for x in range(400):
        seedlist.append([50+x, 600])
        seedlist.append([50+x, 700])
        
    y = 600
    x = 50
    ctr = 0
    while x <=450:
        seedlist.append([x, y])
        x+=1
        ctr+=1
        if ctr%4 == 0:
            y += 1
            
    ##K
    
    for x in range(400):
        seedlist.append([50+x, 750])
        
    x = 200
    y = 750
    ctr = 0
    while x >= 50:
        seedlist.append([x,y])
        x-=1
        ctr+=1
        if ctr%2 == 0:
            y+=1
    
    x = 200
    y = 750
    ctr = 0
    while x <= 450:
        seedlist.append([x,y])
        x+=1
        ctr+=1
        if ctr%3 == 0:
            y+=1
    
    ##S
    
    for x in range(100):
        seedlist.append([50, 880+x])
        seedlist.append([250, 880+x])
        seedlist.append([450, 880+x])
    
    for x in range(200):
        seedlist.append([50+x, 880])
        seedlist.append([250+x, 980])
    
    return seedlist




seedlist = [[2,2], [4,1], [0,4]]
JFA_Voronoi(5, 5, seedlist)
