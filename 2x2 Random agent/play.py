# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:10:35 2019

@author: Srujan Panuganti
"""

import numpy as np
#import itertools 
from operator import add
#import random
from dots_and_boxes import dots_and_boxes as dbs
import q_algorithm
from agent import q_agent
from agent import random_agent
from display import display

class play:
    
    def __init__(self, 
                 env:dbs,
                 agent1:q_agent,
                 agent2 : random_agent,
                 display_it:display):
        
        self.env = env
        self.agent1 = agent1
        self.agent2 = agent2
        self.display_it = display_it
        
    def play_game(self, q_class):

        #agent1_act = 0
        #agent1_prev_state = self.env.current_state
        agent1_tot_boxes = 0

        #agent2_act = 0
        #agent2_prev_state = self.env.current_state
        agent2_tot_boxes = 0
        
        #pos_act  = []
        turn = 0

        while not self.env.game_done():

            my_turn1 = True

# =============================================================================
#             if self.env.game_done():
#                 break
#             
# =============================================================================
# =============================================================================
#             print('num of boxes agent 1',agent1_tot_boxes,
#                   'num of boxes agent 2',agent2_tot_boxes)
#             
# =============================================================================
            while my_turn1 == True and not self.env.game_done():

                #print('333')
                #print('in 1',self.env.game_done())
                
                
                reward1 = 0
                 
                #pos_act = self.env.possible_actions_
                #print('curr',self.env.current_state)
                #previous_state1 = self.env.current_state
                #print('pos',self.env.possible_actions_())
                #previous_state = self.env.current_state
                #agent1_act = self.agent1.get_action(q_class,self.env.current_state,self.env.possible_actions_())
                agent1_act = self.agent1.get_action(q_class,self.env.current_state,self.env.possible_actions_())
                #print(agent1_act)
                
                current_state1,reward1, previous_state1 , number_of_boxes_complete1, is_box_created1  = self.env.do_action(agent1_act)
                
                agent1_tot_boxes += number_of_boxes_complete1
                
                
# =============================================================================
#                 prev_state_action1 = [previous_state1,agent1_act]
#                 #print('agent1 ','\n',self.display_it.update_display(self.env.edges))
# 
#                 q_class.q_update(prev_state_action1, self.env.current_state ,reward1 )#,self.env.possible_actions_())
# 
# =============================================================================
                my_turn1 = is_box_created1
                
                print('agent1 turn',my_turn1)
                
                turn+=1
                #print('turn',turn)
                
            
            my_turn2 = True

            while my_turn2 == True and not self.env.game_done():

                #print('in 2',self.env.game_done())

                
                reward2 = 0
                 
                #previous_state2 = self.env.current_state
                #print('curr',self.env.current_state)
                
                agent2_act = self.agent2.get_action(self.env.possible_actions_())
                 
                current_state2,reward2, previous_state2 , number_of_boxes_complete2, is_box_created2   = self.env.do_action(agent2_act)
                
                agent2_tot_boxes += number_of_boxes_complete2
                
# =============================================================================
#                 prev_state_action2 = [previous_state2,agent2_act]
# 
#                 #print('agent2 ','\n',self.display_it.update_display(self.env.edges))
# 
#                     
#                 q_class.q_update(prev_state_action2, self.env.current_state ,reward2)#, self.env.possible_actions_())
#                 
# =============================================================================
                my_turn2 = is_box_created2

                print('agent2 turn',my_turn2)
                
                turn+=1
                #print('turn',turn)

        
        if agent1_tot_boxes == agent2_tot_boxes:
            winner = 0
        elif agent1_tot_boxes > agent2_tot_boxes:
            winner = 1
        elif agent1_tot_boxes < agent2_tot_boxes:
            winner = 2
        
        if winner == 1:
# =============================================================================
#             q_class.q_update(prev_state_action1, self.env.current_state ,reward1)#, self.env.possible_actions_())
# =============================================================================
            print('agent 1 won', agent1_tot_boxes, agent2_tot_boxes)

        elif winner == 2:
# =============================================================================
#             q_class.q_update(prev_state_action2, self.env.current_state ,reward2)#, self.env.possible_actions_())
# =============================================================================
            print('agent 2 won',agent1_tot_boxes, agent2_tot_boxes)

        else:
            print('draw',agent1_tot_boxes, agent2_tot_boxes)
         
        return winner #, q_class

# =============================================================================
#                 
#     def who_won_the_game(score1, score2):
#         
#         winner = None
#         
#         if score1 > score2:
#             winner = str(player1)
#         elif score1 == score2:
#             winner = str(draw)
#         else:
#             winner = str(player2)
#         
#         return winner
# 
# 
# 
#     def turn(action):
#         
#         previous_state = game.current_state
#         
#         #current_action = player2.current_action
#         old_state_action = [previous_state,current_action]
#         
#         _, possible_actions = game.possible_actions()
#         
#         current_state, reward, previous_state= game.do_action(current_action)
#         
#         action = Q_agent.q_update(old_state_action,current_state,reward,current_action,possible_actions)
#         
#         if turn_change == False:
#             turn(action)
#         
#         if reward == 1:
#             turn_change = False
#         elif reward == 5:
#             turn_change = False
#             game_over = True
#         else:
#             turn_change = True
# 
#         
#     def play_game():
#         reward = 0
#         
#         previous_state = env.
#         current_action = epsilon_greedy()
# 
#         game = dots_and_boxes(grid_size = (2,2))
# 
#         x, y = turn(action)
# 
#         if game_over == True:
#             winner = who_won_the_game()
#         
#         return winner, Q_agent.q_table
# 
#             
# 
# =============================================================================
