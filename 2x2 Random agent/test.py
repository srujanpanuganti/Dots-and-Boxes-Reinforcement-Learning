# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:06:40 2019

@author: Srujan Panuganti
"""


import numpy as np
from operator import add
from dots_and_boxes import dots_and_boxes as dbs
from q_algorithm import q_learn
from agent import q_agent
from agent import random_agent
from play import play as pl
from display import display
import pickle

total_games = 1000
game_count = 0
# =============================================================================
# env = dbs(grid_size = (2,2))
# =============================================================================
display_it = display(grid_size = (2,2))
# =============================================================================
# agent1 = q_agent()
# =============================================================================
# =============================================================================
# agent2 = random_agent()
# =============================================================================

pickle_in = open("dict10000_games_2x2.pickle","rb")
q_table = pickle.load(pickle_in)

q_class = q_learn(q_table)

# =============================================================================
# 
# game1 = pl(env,agent1,agent2,display_it)
# winner = game1.play_game(q_class)
# 
# =============================================================================



agent1_wins = 0
agent2_wins = 0
draws = 0


while(game_count < total_games):
    env = dbs(grid_size = (2,2))
    agent1 = q_agent()
    agent2 = random_agent()
    game1 = pl(env,agent1,agent2,display_it)
    winner = game1.play_game(q_class)
    game_count +=1
    
    if winner == 1:
        agent1_wins += 1
    elif winner ==2:
        agent2_wins += 1
    elif winner == 0:
        draws += 1

print('agent 1 wins = ',agent1_wins,'agent 2 wins = ',agent2_wins,'draws = ',draws)


# =============================================================================
# pickle_out = open("dict.pickle","wb")
# pickle.dump(q_class.q_table, pickle_out)
# pickle_out.close()
# 
# =============================================================================
# =============================================================================
# all_q_value = []
# for key,val in q_class.q_table.items():
#     all_q_value.append([(key),val])
# 
# 
# =============================================================================
