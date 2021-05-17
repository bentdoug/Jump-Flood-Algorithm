# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:42:11 2021
Niave Flood Fill Algorithm Adapted to create Voronoi Diagroms
@author: bentdoug
"""

import matplotlib.pyplot as plt
import numpy as np


def floodfillvoronoi():
    """
    
    Creates a Voronoi Diagram utalizing a niave Breadth-First Search
    type technique. Dimensions and seeds (Voronoi Sites) are hardcoded.

    Returns
    -------
    None. Creates and saves a new image every time a point in the table; flood
    is filled. (Frame-by-frame)

    """
    #A queue for Breadth First Search (point locations)
    queue = []
    
    #A queue that holds point value data in parallel with queue
    value = []
    
    #dimensions of graph
    x = 10
    y = 10
    
    #table to be filled in
    flood = np.zeros((x, y))
    
    #placing initial points and their values into the queue
    queue.append((0, 0))
    value.append(20)
    queue.append((9, 9))
    value.append(10)
    queue.append((9,0))
    value.append(5)
    
    #array used to efficiently look at a points neighbors
    moves = [-1, 0, 1]
    
    #counter used when naming each image to be saved
    count = 0
    
    #BFS adapted to create Voronoi Diagrams
    while len(queue) > 0:
        current = queue.pop(0)
        val = value.pop(0)
        flood[current] = val
        
        #Save each image
        plt.imshow(flood)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.clim(0,20)
        plt.savefig("niaveVoronoi"+ str(count)+".png", dpi = 300)
        plt.show()
        count+=1
        
        
        for i in moves:
            for j in moves:
                new = (current[0]+i, current[1]+j)
                if new[0] in range(0, x) and new[1] in range(0, y):
                    if flood[new] == 0 and new not in queue:
                        queue.append(new)
                        value.append(val)
    


floodfillvoronoi()