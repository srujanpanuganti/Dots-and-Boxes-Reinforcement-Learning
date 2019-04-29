# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:09:16 2019

@author: Srujan Panuganti
"""

import numpy as np
import itertools 
from operator import add
import random


class dots_and_boxes:
    def __init__(self,grid_size = (2,2)):
            
        m = grid_size[0]
        n = grid_size[1]
        self.total_actions = grid_size[0]*(grid_size[1]+1) + grid_size[1]*(grid_size[0]+1)
        self.all_states = list(itertools.product([0, 1], repeat=self.total_actions))
        self.all_actions = []
        for i in self.all_states:
            if sum(i) == 1:
                self.all_actions.append(i)
    
        self.edges = {}
        for edge in self.all_actions:
            self.edges[str(edge)] = 0
    
        self.boxes = {}
        for i in range(1,m*n+1):
            self.boxes[i] = 0
        self.current_state = self.all_states[0]
        self.game_over = False



    def possible_actions_(self):
        possible_actions = []
        for action in self.all_actions:
            print('act',action)
            if self.current_state & action == 0:
                possible_actions.append(action)
                
        return possible_actions
            

    def possible_actions(self, edges):            ### Tested and working
        pos_act_set = set([])
        pos_act_list = []
        for key,value in edges.items():
            if value == 0:
                pos_act_set.add(str(key))
                pos_act_list.append(key)
        return pos_act_set,pos_act_list

    def is_action_possible(self, action):         ### Tested and working
        possible_set, pos_act_list = self.possible_actions(self.edges)
        status = False
        
        if str(action) in possible_set:
            status = True
        
        return status

    def is_box_complete(self, boxes,edges, all_actions):     ### Tested and working
    
        box_created = False
        num_of_boxes_complete = 0
        
        if self.boxes[1] == 0 and edges[str(all_actions[0])] == 1 and edges[str(all_actions[2])] == 1 and edges[str(all_actions[3])] == 1 and edges[str(all_actions[5])] == 1:
            boxes[1] = 1
            num_of_boxes_complete += 1
            #print(kk)
            box_created = True
        if self.boxes[2] == 0 and edges[str(all_actions[1])] == 1 and edges[str(all_actions[3])] == 1 and edges[str(all_actions[4])] == 1 and edges[str(all_actions[6])] == 1:
            boxes[2] = 1
            num_of_boxes_complete += 1
            box_created = True
        if self.boxes[3] == 0 and edges[str(all_actions[5])] == 1 and edges[str(all_actions[7])] == 1 and edges[str(all_actions[8])] == 1 and edges[str(all_actions[10])] == 1:
            boxes[3] = 1
            num_of_boxes_complete += 1
            box_created = True
        if self.boxes[4] == 0 and edges[str(all_actions[6])] == 1 and edges[str(all_actions[8])] == 1 and edges[str(all_actions[9])] == 1 and edges[str(all_actions[11])] == 1:
            boxes[4] = 1
            num_of_boxes_complete += 1
            box_created = True
        return box_created, num_of_boxes_complete
    
        
    def is_game_complete(self, edges):            ### Tested and working
        status = False
        all_values = []
    
        for key,value in edges.items():
            all_values.append(value)
        #print(all_values)
        if sum(all_values) == len(edges):
            status = True
        else:
            status = False
            
        return status
    
    def reward_generate(self,boxes, edges, all_actions):          ### Tested and working
        box, number_of_boxes_complete = self.is_box_complete(boxes, edges, all_actions)  
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

    def update_edge(self, action, edges):
        ### updating the edges where action took place
        edges[str(action)] = 1

    def do_action(self,  action):
    
        ### performing the action
        previous_state = self.current_state

        if game_over(current_state):
            self.game_over = True

        if self.action in possible_actions_:
            current_state = current_state | action
            
        self.update_edge(action, self.edges) 
        
        ### obtain the reward for the performed action
        reward, number_of_boxes_complete, is_box_created = self.reward_generate(self.boxes, self.edges, self.all_actions)

        return current_state,reward, previous_state , number_of_boxes_complete #, game_over

    def game_over(current_state):
        return current_state == all_states[-1]
    
    def reset(self):
        self.current_state = self.all_states[0]
        self.done = False


