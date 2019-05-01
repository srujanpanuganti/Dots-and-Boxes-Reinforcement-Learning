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
                 total_actions,learning_rate = 0.6,discount_factor = 0.7,epsilon=0.6):

        self.total_actions = total_actions
        #self.all_states = list(itertools.product([0, 1], repeat=total_actions))
        #self.all_actions = []
        #for i in self.all_states:
        #    if sum(i) == 1:
        #        self.all_actions.append(i)
        self.number_of_states = 2** (self.total_actions)
        self.all_actions = [ 2**j for j in range(0,self.total_actions)]
        self.all_actions_arr = np.asarray([ 2**j for j in range(0,self.total_actions)]).reshape(self.total_actions,1).astype(int)
        self.zeros_action = np.zeros([self.total_actions,1]).astype(int)
        self.all_actions_with_q_vals = np.hstack((self.all_actions_arr,self.zeros_action))
                
        self.lin_space = list(range(0,self.total_actions))
        
        self.action_index = {}
        
        for key,val in zip(self.all_actions,self.lin_space ):
            self.action_index[key] = val


# =============================================================================
#         self.all_actions = list(range(1,self.total_actions+1))
#         self.all_actions_arr = np.asarray(range(1,self.total_actions+1)).reshape(self.total_actions,1).astype(int)
#         self.zeros_action = np.zeros([self.total_actions,1]).astype(int)
# 
#         self.all_actions_with_q_vals = np.hstack((self.all_actions_arr,self.zeros_action))
# 
# =============================================================================
        self.all_states = list(range(0,self.number_of_states))

        self.q_table = dict.fromkeys(self.all_states,self.all_actions_with_q_vals)

        #self.current_action = self.all_actions[0]
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor 
        self.epsilon =  epsilon


    def compute_q_value(self, old_q_val,reward,max_q):            
        new_q_val = old_q_val + self.learning_rate* (reward + self.discount_factor* max_q - old_q_val)        
        return new_q_val


    def maximum_q(self, current_state, possible_actions):
        max_q = 0
        index = 0
        max_i = 0
        optimal_action = 0
        #print('here',possible_actions)

        for act in possible_actions:
            
            #print('curr st',current_state,'act',act-1)
            #print('what the prob',self.q_table[current_state][act-1])
            if self.q_table[current_state][self.action_index[act]][1] >= max_q:
                max_q = max_q
                optimal_action = act
                
                max_i = index
            index +=1
            #print('papa')
        return max_q,optimal_action,max_i

# =============================================================================
# 
#         for act in possible_actions:
#             if self.q_table[str([current_state,act])] >= max_q:
#                 max_q = max_q
#                 optimal_action = act
#                 
#                 max_i = index
#             index +=1
#         return max_q,optimal_action,max_i
# 
# =============================================================================
    
# =============================================================================
#     def q_update(self, old_state_action, current_state ,reward, possible_actions):
#         ### obtaining the old_q value
#         #previous_state = old_state_action[0]
#         q_value = self.q_table[str(old_state_action)]
#         
# # =============================================================================
# #         if not possible_actions:
# #             self.q_table[str(old_state_action)] = new_q_val
# #             
# # =============================================================================
#         max_q,optimal_action,max_i = self.maximum_q(current_state, possible_actions)
#         
#         ### computing the new q-value to be updated into the q_table
#         new_q_val = self.compute_q_value(q_value,reward,max_q)
#         ### updating the q_value to the q_table    
#         self.q_table[str(old_state_action)] = new_q_val
# 
#         return optimal_action
# 
# =============================================================================

    def q_update(self, old_state_action, current_state ,reward):#, possible_actions):
        ### obtaining the old_q value
        #previous_state = old_state_action[0]
        q_value = self.q_table[old_state_action[0]][self.action_index[old_state_action[1]]][1]
        #q_value = self.q_table[old_state_action[0]][old_state_action[1]][1]
        
        #print('all_', self.all_actions)
        
        max_q,optimal_action,max_i = self.maximum_q(current_state, self.all_actions)
        
        ### computing the new q-value to be updated into the q_table
        new_q_val = self.compute_q_value(q_value,reward,max_q)
        ### updating the q_value to the q_table    
        self.q_table[old_state_action[0]][self.action_index[old_state_action[1]]][1] = new_q_val
        #self.q_table[old_state_action[0]][old_state_action[1]][1] = new_q_val


        return optimal_action



    def epsilon_greedy(self, current_state, possible_actions):
        
        
        pos_act = copy.deepcopy(possible_actions)
        
        max_q, optimal_action, max_i = self.maximum_q(current_state, pos_act)
        
        #print('posss',pos_act)
        #print(optimal_action)
        #print(max_i)
        if random.random() >=  self.epsilon:
            action = optimal_action
            #print('opt action',action)
        else:
            if max_i > 1:
                np.delete(pos_act,max_i)
                action = random.choice(pos_act)
            else:
                action = random.choice(pos_act)
        return action

