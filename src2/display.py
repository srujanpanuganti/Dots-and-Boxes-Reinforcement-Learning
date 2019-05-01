# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:55:29 2019

@author: Srujan Panuganti
"""

import numpy as np


class display:
    def __init__(self, grid_size = (2,2)):
        self.grid_size = grid_size
        self.display_array = np.zeros([grid_size[0]+ grid_size[1]+1,grid_size[0]+ grid_size[1]+1]).astype(int)
        
    def update_display(self,edges):
        only_values = []
        for key,value in edges.items():
            only_values.append(value)
        
        self.display_array [0,1] = only_values[0]
        self.display_array [0,3] = only_values[1]
        self.display_array [1,0] = only_values[2]
        self.display_array [1,2] = only_values[3]
        self.display_array [1,4] = only_values[4]
        self.display_array [2,1] = only_values[5]
        self.display_array [2,3] = only_values[6]
        self.display_array [3,0] = only_values[7]
        self.display_array [3,2] = only_values[8]
        self.display_array [3,4] = only_values[9]
        self.display_array [4,1] = only_values[10]
        self.display_array [4,3] = only_values[11]
        
        return self.display_array