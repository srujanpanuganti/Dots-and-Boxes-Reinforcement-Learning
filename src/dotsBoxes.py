import numpy as np
import sys

class dotsBoxes:
    def __init__(self,
                  _size = (2,2)):
        self.size = _size
        self.numStates = ((_size+1)*_size)**2
        self.allStates = list(range(2 ** self.numStates))
        self.numActions = ((self.size+1) * self.size) * 2
        self.allActions = list(range(self.numActions))
        self.currState = self.allStates[0]
        
    def conv2bin(self, val):
        return bin(val)[2:].zfill(self.numActions)
    
    def doAction(self, action):
        self.currState = int(self.conv2bin(self.currState) | (self.conv2bin(1) << action), 2)
        # take care of reward here
        
    def possibleActions(self):
        possStates = list(~self.conv2bin(self.currState))
        return [len(possStates) - idx for idx, val in enumerate(possStates) if val == '1']
    
class display:
    def __init__(self):
        pass
    
    def genDisplay(self, state):
        pass
        
        