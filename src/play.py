# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:10:35 2019

@author: Srujan Panuganti
"""

import numpy as np
import itertools 
from operator import add
import random
import dots_and_boxes
import q_algorithm
import agent 

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
            
