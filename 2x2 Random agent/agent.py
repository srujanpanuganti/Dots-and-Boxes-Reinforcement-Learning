# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:10:16 2019

@author: Srujan Panuganti
"""
import numpy as np
import itertools 
from operator import add
import random
from q_algorithm import q_learn


# =============================================================================
# class random_agent:
#     def __init__(self,grid_size):
#         self.score = 0
#         self.total_actions = grid_size[0]*(grid_size[1]+1) + grid_size[1]*(grid_size[0]+1)
#         self.all_states = list(itertools.product([0, 1], repeat=self.total_actions))
#         self.all_actions = []
#         for i in self.all_states:
#             if sum(i) == 1:
#                 self.all_actions.append(i)
# 
#         self.action = random.choice(self.all_actions)
# 
# =============================================================================

class q_agent:
    
    def __init__(self):
        self.score = 0
        #self.q_table = Q.q_table
        #self.current_action = Q.current_action
    def get_action(self, 
                  q_class : q_learn,
                  current_state,
                  possible_actions):
        act = q_class.epsilon_greedy(current_state,possible_actions)
        #print('act',act)
        return act
    
class random_agent:
    def __init__(self):
        self.score = 0
    def get_action(self, possible_actions):
        
        act = random.choice(possible_actions)
        return act
    