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
from play import play as pl
from display import display

env = dbs(grid_size = (2,2))
display_it = display(grid_size = (2,2))
agent1 = q_agent()
agent2 = q_agent()
q_class = q_learn(total_actions = 12)
game1 = pl(env,agent1,agent2,display_it)
winner, q_class = game1.play_game(q_class)