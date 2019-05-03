# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:10:35 2019

@author: Srujan Panuganti
"""

import numpy as np
#import itertools 
#from operator import add
#import random
from dots_and_boxes import dots_and_boxes as dbs
#import q_algorithm
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
        
        #print('boxes',self.env.boxes)

        agent1_tot_boxes = 0
        agent2_tot_boxes = 0
        
        turn = 0

        while not self.env.game_done():

            my_turn1 = True

            while my_turn1 == True and not self.env.game_done():
                
                reward1 = 0
                 
                agent1_act = self.agent1.get_action(q_class,self.env.current_state,self.env.possible_actions_)
                
                current_state1,reward1, previous_state1 , number_of_boxes_complete1, is_box_created1  = self.env.do_action(agent1_act)
                
                agent1_tot_boxes += number_of_boxes_complete1
                
                my_turn1 = is_box_created1
                
                turn+=1
                
            
            my_turn2 = True

            while my_turn2 == True and not self.env.game_done():

                reward2 = 0
                                 
                agent2_act = self.agent2.get_action(self.env.possible_actions_)
                 
                current_state2,reward2, previous_state2 , number_of_boxes_complete2, is_box_created2   = self.env.do_action(agent2_act)
                
                agent2_tot_boxes += number_of_boxes_complete2
                my_turn2 = is_box_created2
                
                turn+=1
 
        
        if agent1_tot_boxes == agent2_tot_boxes:
            winner = 0
        elif agent1_tot_boxes > agent2_tot_boxes:
            winner = 1
        elif agent1_tot_boxes < agent2_tot_boxes:
            winner = 2
        
        if winner == 1:
            print('agent 1 won', agent1_tot_boxes, agent2_tot_boxes)

        elif winner == 2:
            print('agent 2 won',agent1_tot_boxes, agent2_tot_boxes)

        else:
            print('draw',agent1_tot_boxes, agent2_tot_boxes)
         
        return winner#, q_class

