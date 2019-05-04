# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:37:59 2019

@author: Srujan Panuganti
"""

import sklearn.pipeline
import sklearn.preprocessing
from sklearn.linear_model import SGDRegressor
from sklearn.kernel_approximation import RBFSampler
import pickle
import numpy as np
from dots_and_boxes import dots_and_boxes
import tensorflow as tf
#from q_algorithm import q_learn
import random

env = dots_and_boxes()
#q_class = q_learn(12)
pickle_in = open("dict10000_games.pickle","rb")
q_table = pickle.load(pickle_in)

obs = []

iter1 = 0
#%%

for pair in q_table.items():
    iter1+=1
    for i in pair[1]:
        if i[1] != 0:
            obs.append([pair[0],i[0],i[1]])
 #       obs.append([pair[0],i[0]])
     
 #%%
feat = []

for i in range(1000):
    feat.append(random.choice(obs))
    
 
#%%

   
#%%

observations_array = np.asarray() 


#%%
observations = np.asarray(obs)

scaler = sklearn.preprocessing.StandardScaler()
scaler.fit(observations)

featurizer = sklearn.pipeline.FeatureUnion([
        ("rbf1", RBFSampler(gamma=5.0, n_components=100)),
        ("rbf2", RBFSampler(gamma=2.0, n_components=100)),
        ("rbf3", RBFSampler(gamma=1.0, n_components=100)),
        ("rbf4", RBFSampler(gamma=0.5, n_components=100))
        ])
featurizer.fit(scaler.transform(observations))


class Estimator():
    """
    Value Function approximator. 
    """
    
    def __init__(self):
        # We create a separate model for each action in the environment's
        # action space. Alternatively we could somehow encode the action
        # into the features, but this way it's easier to code up.
        self.models = []
        for _ in range(env.total_actions):
            
            model = SGDRegressor(learning_rate="constant")
            # We need to call partial_fit once to initialize the model
            # or we get a NotFittedError when trying to make a prediction
            # This is quite hacky.
            model.partial_fit([self.featurize_state(env.reset())], [0])
            self.models.append(model)
    
    def featurize_state(self, state):
        """
        Returns the featurized representation for a state.
        """
        print(state)
        scaled = scaler.transform([state])
        featurized = featurizer.transform(scaled)
        return featurized[0]
    
    def predict(self, s, a=None):
        """
        Makes value function predictions.
        
        Args:
            s: state to make a prediction for
            a: (Optional) action to make a prediction for
            
        Returns
            If an action a is given this returns a single number as the prediction.
            If no action is given this returns a vector or predictions for all actions
            in the environment where pred[i] is the prediction for action i.
            
        """
        features = self.featurize_state(s)
        if not a:
            return np.array([m.predict([features])[0] for m in self.models])
        else:
            return self.models[a].predict([features])[0]
    
    def update(self, s, a, y):
        """
        Updates the estimator parameters for a given state and action towards
        the target y.
        """
        features = self.featurize_state(s)
        self.models[a].partial_fit([features], [y])

