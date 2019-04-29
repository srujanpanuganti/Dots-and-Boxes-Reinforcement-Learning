-# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:02:21 2019

@author: Srujan Panuganti
"""
import numpy as np
import itertools 
from operator import add
import random


class dots_and_boxes:
    def __init__(self,grid_size = (2,2)):
            
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
            boxes[i] = 0
        self.current_state = self.all_action[0]

    def possible_actions_(current_state):
        possible_actions = []
        for action in self.all_actions:
            if current_state & action == 0:
                possible_actions.append(action)
            

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
            num_of_boxes_complete + = 1
            #print(kk)
            box_created = True
        if self.boxes[2] == 0 and edges[str(all_actions[1])] == 1 and edges[str(all_actions[3])] == 1 and edges[str(all_actions[4])] == 1 and edges[str(all_actions[6])] == 1:
            boxes[2] = 1
            num_of_boxes_complete + = 1
            box_created = True
        if self.boxes[3] == 0 and edges[str(all_actions[5])] == 1 and edges[str(all_actions[7])] == 1 and edges[str(all_actions[8])] == 1 and edges[str(all_actions[10])] == 1:
            boxes[3] = 1
            num_of_boxes_complete + = 1
            box_created = True
        if self.boxes[4] == 0 and edges[str(all_actions[6])] == 1 and edges[str(all_actions[8])] == 1 and edges[str(all_actions[9])] == 1 and edges[str(all_actions[11])] == 1:
            boxes[4] = 1
            num_of_boxes_complete + = 1
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
            feedback = 1
        if game:
            feedback = 5
            #game_over = True
            
        return feedback, number_of_boxes_complete #, game_over

    def update_edge(self, action, edges):
        ### updating the edges where action took place
        edges[str(action)] = 1

    def do_action(self,  action):
    
        ### performing the action
        previous_state = self.current_state

        if self.is_action_possible(action):
            #current_state = list( map(add, self.current_state, action) )
            current_state = current_state | action
            print('cur',current_state)
        
        self.update_edge(action, self.edges) 
        
        ### obtain the reward for the performed action
        reward = self.reward_generate(self.boxes, self.edges, self.all_actions)

        return current_state,reward, previous_state #, game_over

    def game_over():
        return current_state == all_states[-1]
    
    


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


#%%
class random_agent:
    def __init__(self,total_actions):
        self.score = 0
        self.total_actions = grid_size[0]*(grid_size[1]+1) + grid_size[1]*(grid_size[0]+1)
        self.all_states = list(itertools.product([0, 1], repeat=self.total_actions))
        self.all_actions = []
        for i in self.all_states:
            if sum(i) == 1:
                self.all_actions.append(i)

        self.action = random.choice(all_actions)


class q_agent:
    
    def __init__(self):
        
        self.score = 0
        #self.q_table = Q.q_table
        #self.current_action = Q.current_action
    
#%%


class play:
    
    def __init__(self):
        
        
    def who_won_the_game(score1, score2):
        
        winner = None
        
        if score1 > score2:
            winner = str(player1)
        elif score1 == score2:
            winner = str(draw)
        else:
            winner = str(player2)
        
        return winner


    def turn(action):
        
        previous_state = game.current_state
        
        #current_action = player2.current_action
        old_state_action = [previous_state,current_action]
        
        _, possible_actions = game.possible_actions()
        
        current_state, reward, previous_state= game.do_action(current_action)
        
        action = Q_agent.q_update(old_state_action,current_state,reward,current_action,possible_actions)
        
        if turn_change == False:
            #turn(action)
        
        if reward == 1:
            turn_change = False
        elif reward == 5:
            turn_change = False
            game_over = True
        else:
            turn_change = True

        
    def play_game():
        
        #player1 = random_agent()
        player1 = q_agent()
        player2 = q_agent()

        current_action = epsilon_greedy()

        game = dots_and_boxes(grid_size = (2,2))

        x, y = turn(action)

        if game_over == True:
            winner = who_won_the_game()
        
        return winner, Q_agent.q_table


    def epsilon_greedy():
        
        if random.random() > epsilon:
            action = 
        else:
            action = 
            
        
        


 
#%%
# =============================================================================
# def do_action(old_state_action, action):
# 
#     print(old_state_action)
#     
#     old_state, old_action = old_state_action[0] , old_state_action[1]
# 
#     print(old_state)
# 
#     ### obtaining the old_q value
#     q_value = q_table[str(old_state_action)]
# 
#     print(q_value)
#     print('act',action)
#     
#     ### performing the action
#     if is_action_possible(action):
#         current_state = list( map(add, old_state, action) )
#         print('cur',current_state)
# 
#     ### updating the edges where action took place
#     edges[str(action)] = 1    
#     #print(edges)
# 
#     
#     ### calculation the maximum q_value for the possible actions for the current state    
#     _, pos_act = possible_actions(edges)
#     
#     max_q = 0
#     for act in pos_act:
#         if q_table[str([current_state,act])] >= max_q:
#             max_q = max_q
# 
#     ### obtain the reward for the performed action
#     
#     reward = reward_generate()
#     ### computing the new q-value to be updated into the q_table
#     new_q_val = compute_q_value(q_value,reward,max_q)
# 
#     ### updating the q_value to the q_table    
#     q_table[str(current_state,action)] = new_q_val
#     
#     return q_table
# 
# 
# x = do_action(state_action[500],all_actions[4])
# 
# 
# 
# =============================================================================