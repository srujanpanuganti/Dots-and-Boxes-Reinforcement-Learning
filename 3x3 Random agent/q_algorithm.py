# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:09:53 2019

@author: Srujan Panuganti
"""

import numpy as np
#import itertools 
from operator import add
import random
import copy


class q_learn:
    def __init__(self,
                 total_actions,q_table,learning_rate = 0.6,discount_factor = 0.7,epsilon=0.6):

        self.total_actions = total_actions
        self.q_table = q_table
        
        self.number_of_states = 2** (self.total_actions)
        self.all_actions = [ 2**j for j in range(0,self.total_actions)]
        self.lin_space = list(range(0,self.total_actions))
        
        self.action_index = {}
        
        for key,val in zip(self.all_actions,self.lin_space ):
            self.action_index[key] = val


        self.learning_rate = learning_rate
        self.discount_factor = discount_factor 
        self.epsilon =  epsilon

    def maximum_q(self, current_state, possible_actions):
        max_q = 0
        index = 0
        max_i = 0
        optimal_action = 0
        #print('here',possible_actions)

        for act in possible_actions:
            if self.q_table[current_state][self.action_index[act]][1] >= max_q:
                max_q = max_q
                optimal_action = act
                
                max_i = index
            index +=1
            #print('papa')
        return max_q,optimal_action,max_i


    def epsilon_greedy(self, current_state, possible_actions):
        
        
        pos_act = copy.deepcopy(possible_actions)
        
        max_q, optimal_action, max_i = self.maximum_q(current_state, pos_act)
        
        return optimal_action
