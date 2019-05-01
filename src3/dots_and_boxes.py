# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:09:16 2019

@author: Srujan Panuganti
"""

import numpy as np
#import itertools 
from operator import add
#import random


class dots_and_boxes:
    def __init__(self,grid_size = (3,3)):
            
        m = grid_size[0]
        n = grid_size[1]
        self.total_actions = grid_size[0]*(grid_size[1]+1) + grid_size[1]*(grid_size[0]+1)

        #self.all_actions = list(range(1,self.total_actions+1))
        self.all_actions = [ 2**j for j in range(0,self.total_actions)]
        self.number_of_states = 2**(self.total_actions)
        
        self.all_states = list(range(0,self.number_of_states))
        self.possible_actions_ = [ 2**j for j in range(0,self.total_actions)]
        
# =============================================================================
#         self.lin_space = list(range(0,self.total_actions))
#         
#         pos_dict = {}
#         
#         for key,val in zip(self.possible_actions_,self.lin_space ):
#             pos_dict[key] = val
# 
# =============================================================================
# =============================================================================
#         self.all_actions_array = np.asarray(range(1,self.total_actions+1)).reshape(self.total_actions,1).astype(int)
# =============================================================================


# =============================================================================
#         self.zeros_action = np.zeros([self.total_actions,1]).astype(int)
# 
#         self.all_actions_with_q_vals = np.hstack((self.all_actions_array,self.zeros_action))
# 
# =============================================================================
# =============================================================================
#         for i in self.all_states:
#             if sum(i) == 1:
#                 self.all_actions.append(i)
#     
# =============================================================================
        self.edges = dict.fromkeys(self.all_actions,0)
    
        self.boxes = dict.fromkeys(list(range(1,m*n+1)),0)

        self.current_state = self.all_states[0]
        self.game_over = False
        self.boxes_filled = False

    def convert_to_binary(self,number):
        return bin(number)[2:].zfill(self.total_actions)
# =============================================================================
# 
#     def possible_actions_(self):
#         possible_actions = []
#         #print('all',self.all_actions)
#         for action in self.all_actions:
#             #print('act',action)
#             andList = [ x and y for x,y in zip(self.current_state,action)]
#             #print(andList)
#             if andList == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
#                 possible_actions.append(action)
#         return possible_actions
#             
# =============================================================================
# =============================================================================
#     def possible_actions_(self):
#         possible_actions = []
#         #print('all',self.all_actions)
#         for action in self.all_actions:
#             #print('act',action)
#             andList = [ x and y for x,y in zip(np.array(list(self.convert_to_binary(self.current_state))).astype(int),np.array(list(self.convert_to_binary(action))).astype(int))]
#             #print(andList)
#             if andList == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
#                 possible_actions.append(action)
#         return possible_actions
# 
# =============================================================================
# =============================================================================
#     def possible_actions(self, edges):            ### Tested and working
#         pos_act_set = set([])
#         pos_act_list = []
#         for key,value in edges.items():
#             if value == 0:
#                 pos_act_set.add(str(key))
#                 pos_act_list.append(key)
#         return pos_act_set,pos_act_list
# 
#     def is_action_possible(self, action):         ### Tested and working
#         possible_set, pos_act_list = self.possible_actions(self.edges)
#         status = False
#         
#         if str(action) in possible_set:
#             status = True
#         
#         return status
# 
# =============================================================================
    def is_box_complete(self, boxes,edges):#, all_actions):     ### Tested and working
    
        box_created = False
        num_of_boxes_complete = 0
        
        #print(boxes)
        
        if self.boxes[1] == 0 and edges[self.all_actions[0]] == 1 and edges[self.all_actions[3]] == 1 and edges[self.all_actions[4]] == 1 and edges[self.all_actions[7]] == 1:
            self.boxes[1] = 1
            num_of_boxes_complete += 1
            #print(kk)
            box_created = True
        if self.boxes[2] == 0 and edges[self.all_actions[1]] == 1 and edges[self.all_actions[4]] == 1 and edges[self.all_actions[5]] == 1 and edges[self.all_actions[8]] == 1:
            self.boxes[2] = 1
            num_of_boxes_complete += 1
            box_created = True
        if self.boxes[3] == 0 and edges[self.all_actions[2]] == 1 and edges[self.all_actions[5]] == 1 and edges[self.all_actions[6]] == 1 and edges[self.all_actions[9]] == 1:
            self.boxes[3] = 1
            num_of_boxes_complete += 1
            box_created = True
        if self.boxes[4] == 0 and edges[self.all_actions[7]] == 1 and edges[self.all_actions[10]] == 1 and edges[self.all_actions[14]] == 1 and edges[self.all_actions[11]] == 1:
            self.boxes[4] = 1
            num_of_boxes_complete += 1
            box_created = True

        if self.boxes[5] == 0 and edges[self.all_actions[8]] == 1 and edges[self.all_actions[11]] == 1 and edges[self.all_actions[12]] == 1 and edges[self.all_actions[15]] == 1:
            self.boxes[5] = 1
            num_of_boxes_complete += 1
            box_created = True

        if self.boxes[6] == 0 and edges[self.all_actions[9]] == 1 and edges[self.all_actions[12]] == 1 and edges[self.all_actions[13]] == 1 and edges[self.all_actions[16]] == 1:
            self.boxes[6] = 1
            num_of_boxes_complete += 1
            box_created = True

        if self.boxes[7] == 0 and edges[self.all_actions[14]] == 1 and edges[self.all_actions[17]] == 1 and edges[self.all_actions[18]] == 1 and edges[self.all_actions[21]] == 1:
            self.boxes[7] = 1
            num_of_boxes_complete += 1
            box_created = True

        if self.boxes[8] == 0 and edges[self.all_actions[15]] == 1 and edges[self.all_actions[18]] == 1 and edges[self.all_actions[19]] == 1 and edges[self.all_actions[22]] == 1:
            self.boxes[8] = 1
            num_of_boxes_complete += 1
            box_created = True
            
        if self.boxes[9] == 0 and edges[self.all_actions[16]] == 1 and edges[self.all_actions[19]] == 1 and edges[self.all_actions[20]] == 1 and edges[self.all_actions[23]] == 1:
            self.boxes[9] = 1
            num_of_boxes_complete += 1
            box_created = True

        return box_created, num_of_boxes_complete
            
        
    def is_game_complete(self):            ### Tested and working
        status = False
        all_values = []
    
        for key,value in self.edges.items():
            all_values.append(value)
        #print(all_values)
        if sum(all_values) == len(self.edges):
            status = True
            self.boxes_filled = True
        else:
            status = False
            
        return status
    
    def reward_generate(self,boxes, edges):#, all_actions):          ### Tested and working
        box, number_of_boxes_complete = self.is_box_complete(boxes, edges)#, all_actions)  
        #box = False
        game = self.is_game_complete()
        #game = False
        feedback = 0   
        
        if box and not game:
            feedback = 1*number_of_boxes_complete
        if game:
            feedback = 5
            #game_over = True
            
        return feedback, number_of_boxes_complete, box #, game_over


    def game_done(self):
# =============================================================================
#         if self.current_state == self.all_states[-1]:
#             self.game_over = True
# =============================================================================
        return self.current_state == self.all_states[-1]

# =============================================================================
#     def bin_to_dec(self,x):
#         conv = 0
#         for i in range(0,len(x)):
#             conv = conv + 2**i    
#         return conv
# 
# =============================================================================
    

    def update_edge(self, action, edges):
        ### updating the edges where action took place
        edges[action] = 1

    def do_action(self,  action):            #break

        ### performing the action
        previous_state = self.current_state

        #print('selected',bin(action))

        #print('before action',bin(self.current_state))

        if action in self.possible_actions_:
            
            self.current_state = self.current_state + action
            self.possible_actions_.remove(action)
            
            #self.current_state = tuple( map(add, self.current_state, action))
            #self.current_state = self.current_state | action
        #print('after action done',self.current_state)

        self.update_edge(action, self.edges) 
        
        ### obtain the reward for the performed action
        reward, number_of_boxes_complete, is_box_created = self.reward_generate(self.boxes, self.edges)#, self.all_actions)

# =============================================================================
#         if self.current_state == self.all_states[-1]:
#             self.game_over = True
#             
# =============================================================================
    

        return self.current_state,reward, previous_state , number_of_boxes_complete, is_box_created #, game_over

    def reset(self):
        self.current_state = self.all_states[0]
        self.possible_actions_ = [ 2**j for j in range(0,self.total_actions)]
        self.edges = dict.fromkeys(self.all_actions,0)
        self.boxes = dict.fromkeys(list(range(1,m*n+1)),0)
        self.boxes_filled = False



