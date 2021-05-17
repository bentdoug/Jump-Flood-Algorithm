# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:03:33 2021
Naive Flood Fill Algorithm
@author: bentdoug
"""
import matplotlib.pyplot as plt
import numpy as np


def flood(seed, x, y):
    """
    
    Fills a graph utalizing Breadth-First Search
    
    Parameters
    ----------
    seed : Starting point to flood out from
    x : x-dimension (size) of grid
    y : y-dimension (size) of grid

    Returns
    -------
     None. Creates and saves a new image every time a point in the table; flood
    is filled. (Frame-by-frame)

    """
    
    #queue for BFS
    queue = []
    
    #graph to be filled
    flood = np.zeros((x, y))
    
    #appending initial seed to the queue
    queue.append(seed)
    
    #array used to efficiently look at a points neighbors
    moves = [-1, 0, 1]
    
    #counter used when naming each image to be saved
    count = 0
    
    #BFS Algorithm adapted to flood a graph
    while len(queue) > 0:
        current = queue.pop(0)
        flood[current] = 20
        
        #saving each image
        plt.imshow(flood)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.clim(0,20)
        plt.savefig("niaveflood"+ str(count)+".png", dpi = 300)
        plt.show()
        count+=1
        
        for i in moves:
            for j in moves:
                new = (current[0]+i, current[1]+j)
                if new[0] in range(0, x) and new[1] in range(0, y):
                    if flood[new] == 0 and new not in queue:
                        queue.append(new)
                        

flood((4,4), 10, 10)