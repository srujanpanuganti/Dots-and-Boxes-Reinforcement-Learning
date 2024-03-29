# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:09:53 2019

@author: Srujan Panuganti
"""

import numpy as np
import itertools 
from operator import add
import random


class Q:
    def __init__(self, total_actions):

        self.all_states = list(itertools.product([0, 1], repeat=total_actions))
        self.all_actions = []
        for i in self.all_states:
            if sum(i) == 1:
                self.all_actions.append(i)
        
        self.state_action = []
        
        for state in self.all_states:
            for action in self.all_actions:
                self.state_action.append([state,action])

        self.q_table = {}

        for pair in self.state_action:
            self.q_table[str(pair)] = 0  ## initializing the q_values as zero  for every state-action pair

        self.current_action = self.all_actions[0]
        
    def compute_q_value(self, old_q_val,reward,max_q):
        
        learning_rate = 0.6
        discount_factor = 0.7
    
        new_q_val = old_q_val + learning_rate* (reward + discount_factor* max_q - old_q_val)
        
        return new_q_val

    def maximum_q(self, current_state, possible_actions):
        max_q = 0
        for act in possible_actions:
            if self.q_table[str([current_state,act])] >= max_q:
                max_q = max_q
                optimal_action = act
        return max_q,optimal_action

    
    def q_update(self, old_state_action, current_state ,reward, action, possible_actions):
        ### obtaining the old_q value  
        previous_state = old_state_action[0]
        q_value = self.q_table[str(old_state_action)]
        
        max_q,optimal_action = self.maximum_q(self, current_state, possible_actions)
        
        ### computing the new q-value to be updated into the q_table
        new_q_val = self.compute_q_value(self, q_value,reward,max_q)
        ### updating the q_value to the q_table    
        self.q_table[str(previous_state,action)] = new_q_val

        return optimal_action
