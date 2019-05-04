# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:06:40 2019

@author: Srujan Panuganti
"""


import numpy as np
#from operator import add
from dots_and_boxes import dots_and_boxes as dbs
from q_algorithm import q_learn
from agent import q_agent
from play import play as pl
from display import display
import pickle
import time
#from approximation import Estimator
import tensorflow as tf
from neural_network import neural

start = time.time()

total_games = 1
game_count = 0
env = dbs(grid_size = (3,3))
display_it = display(grid_size = (3,3))
agent1 = q_agent()
agent2 = q_agent()
#estm = Estimator()
#q_class = q_learn(24,estm)
game1 = pl(env,agent1,agent2,display_it)
#winner, q_class = game1.play_game(q_class)

agent1_wins = 0
agent2_wins = 0
draws = 0





# =============================================================================
# 
# while(game_count < total_games):
#     env = dbs(grid_size = (3,3))
#     agent1 = q_agent()
#     agent2 = q_agent()
#     game1 = pl(env,agent1,agent2,display_it)
#     winner, q_class = game1.play_game(q_class)
#     game_count +=1
#     print('game number = ',game_count)
#     
#     if winner == 1:
#         agent1_wins += 1
#     elif winner ==2:
#         agent2_wins += 1
#     elif winner == 0:
#         draws += 1
# 
# 
# 
# print('agent 1 wins = ',agent1_wins,'agent 2 wins = ',agent2_wins,'draws = ',draws)
# 
# =============================================================================
end = time.time()
print('time taken = ',end - start)
# =============================================================================
# 
# pickle_out = open("dict1000_games.pickle","wb")
# pickle.dump(q_class.q_table, pickle_out)
# pickle_out.close()
# 
# =============================================================================

# =============================================================================
# agent1_wins = 0
# agent2_wins = 0
# draws = 0
# 
# while(game_count < total_games):
#     env = dbs(grid_size = (2,2))
#     agent1 = q_agent()
#     agent2 = q_agent()
#     game1 = pl(env,agent1,agent2,display_it)
#     winner, q_class = game1.play_game(q_class)
#     game_count +=1
#     
#     if winner == 1:
#         agent1_wins += 1
#     elif winner ==2:
#         agent2_wins += 1
#     elif winner == 0:
#         draws += 1
# 
# print('agent 1 wins = ',agent1_wins,'agent 2 wins = ',agent2_wins,'draws = ',draws)
# 
# 
# all_q_value = []
# for key,val in q_class.q_table.items():
#     all_q_value.append([(key),val])
#     
# 
# =============================================================================
