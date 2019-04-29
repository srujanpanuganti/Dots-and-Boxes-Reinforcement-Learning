# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:02:21 2019

@author: Srujan Panuganti
"""
import numpy as np
import itertools 
from operator import add




def compute_q_value(old_q_val,reward,max_q):
    
    learning_rate = 0.6
    discount_factor = 0.7

    new_q_val = old_q_val + learning_rate* (reward + discount_factor* max_q - old_q_val)
    
    return new_q_val


# =============================================================================
# def max_q_value(q_table):
#     
#     max_q = np.max(q_table[2])
#     
#     return max_q
# 
# 
# def next_states(current_state, action):
#     
#     next_st = action + current_state
#     
#     return next_st
# 
# =============================================================================


################  Algorthim  ##################
    
'''
create the dots and boxes game

define each state uniquely and based on each action  --done

create the q-table, with a value for each state and action pair -- done

start the game

for each state visited, check all the possible next states. -- done

find out which state action pair gives us the highest q value. and store it to the current q_value -- done

obtained the feedback for the selected state-action pair, whether it is positive or negative. --yet to be done

update the q_value of the selected state_action pair based on the feedback we got  -- done
defined a function to compute the new q_value based on the sutton and barto formula

keep going

'''

#%%


################### all states 
## binary encoding
###########  all states 
grid_size = [2,2] ## m,n

m = grid_size[0]
n = grid_size[1]

total_actions = m*(n+1) + n*(m+1)

#print(total_actions)

all_states = list(itertools.product([0, 1], repeat=total_actions))
#print(all_states)

#%%
################### all actions
all_actions = []
for i in all_states:
    if sum(i) == 1:
        all_actions.append(i)
#print(all_actions)

#%%
#################### to store the new edges 
edges = {}
for edge in all_actions:
    edges[str(edge)] = 0

#################### boxes for m x n grid
boxes = {}
for i in range(1,m*n+1):
    boxes[i] = 0
    
#%%
#################### state-action pairs

#%%
edges[str(all_actions[5])] = 1
#%%
    
state_action = []

for state in all_states:
    for action in all_actions:
        state_action.append([state,action])

#print(state_action[1])
 
#%%
##################### initializing the q-table
q_table = {}

for pair in state_action:
    q_table[str(pair)] = 0  ## initializing the q_values as zero  for every state-action pair

#%%
##################### finding the possible actions
def possible_actions(edges):            ### Tested and working
    pos_act_set = set([])
    pos_act_list = []
    for key,value in edges.items():
        if value == 0:
            pos_act_set.add(str(key))
            pos_act_list.append(key)
    return pos_act_set,pos_act_list

pos = possible_actions(edges)



#%%
def is_action_possible(action):         ### Tested and working
    possible_set, _ = possible_actions(edges)
    status = False
    
    if str(action) in possible_set:
        status = True
    
    return status
    
 
#%%
def do_action(old_state_action, action):

    print(old_state_action)
    
    old_state, old_action = old_state_action[0] , old_state_action[1]

    print(old_state)

    ### obtaining the old_q value
    q_value = q_table[str(old_state_action)]

    print(q_value)
    print('act',action)
    
    ### performing the action
    if is_action_possible(action):
        current_state = list( map(add, old_state, action) )
        print('cur',current_state)

    ### updating the edges where action took place
    edges[str(action)] = 1    
    #print(edges)

    
    ### calculation the maximum q_value for the possible actions for the current state    
    _, pos_act = possible_actions(edges)
    
    max_q = 0
    for act in pos_act:
        if q_table[str([current_state,act])] >= max_q:
            max_q = max_q

    ### obtain the reward for the performed action
    
    reward = reward_generate()
    ### computing the new q-value to be updated into the q_table
    new_q_val = compute_q_value(q_value,reward,max_q)

    ### updating the q_value to the q_table    
    q_table[str(current_state,action)] = new_q_val
    
    return q_table


x = do_action(state_action[500],all_actions[4])

#%%



#%%
def is_box_complete():     ### Tested and working


    box_created = False
    if boxes[1] == 0 and edges[str(all_actions[0])] == 1 and edges[str(all_actions[2])] == 1 and edges[str(all_actions[3])] == 1 and edges[str(all_actions[5])] == 1:
        boxes[1] = 1
        #print(kk)
        box_created = True
    if boxes[2] == 0 and edges[str(all_actions[1])] == 1 and edges[str(all_actions[3])] == 1 and edges[str(all_actions[4])] == 1 and edges[str(all_actions[6])] == 1:
        boxes[2] = 1
        box_created = True
    if boxes[3] == 0 and edges[str(all_actions[5])] == 1 and edges[str(all_actions[7])] == 1 and edges[str(all_actions[8])] == 1 and edges[str(all_actions[10])] == 1:
        boxes[3] = 1
        box_created = True
    if boxes[4] == 0 and edges[str(all_actions[6])] == 1 and edges[str(all_actions[8])] == 1 and edges[str(all_actions[9])] == 1 and edges[str(all_actions[11])] == 1:
        boxes[4] = 1
        box_created = True
    return box_created


#stat = is_box_complete(boxes)
#print(stat)

    
#%%
def is_game_complete():            ### Tested and working
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


#%% 

def reward_generate():          ### Tested and working
    box = is_box_complete()  
    #box = False
    game = is_game_complete()
    #game = False
    
    feedback = 0   
    
    if box and not game:
        feedback = 1
    if game:
        feedback = 5
        
    return feedback
