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
