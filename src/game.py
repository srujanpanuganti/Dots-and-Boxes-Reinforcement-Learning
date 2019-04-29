from dotsBoxes import dotsBoxesEnv
from dotsBoxes import reward
from agent import qAgent
from qLearning import qLearn
class game:
    def __init__(self, 
                 _env: dotsBoxesEnv, 
                 _agent1:qAgent, 
                 _agent2:qAgent,
                 _qClass:qLearn):
        self.env = _env
        self.agent1 = _agent1
        self.agent2 = _agent2
        self.reward = reward()
        # Q Class that will get updated by both agents
        self.qClass = _qClass
    
    def resetGame(self):
        # only reset environment
        self.env.reset()
    
    def playGame(self):
        agent1action = []
        prevState1 = self.env.currState
        agent1action = 0
        totalAgent1Boxes = 0
        agent2action = []
        prevState2 = self.env.currState
        agent2action = 0
        totalAgent2Boxes = 0
        winner = 0 # draw0
        
        # agents take turns
        while not self.env.isDone:
            # agent1 move
            R1 = 0
            # store previous state
            prevState1 = self.env.currState
            # get agent action from policy
            agent1action = self.agent1.getAction(self.qClass,
                                                 self.env.currState,
                                                 self.env.possibleActions())
            # do action and calculate reward
            boxesCompleted1 = self.env.doAction(agent1action)
            R1 = self.reward.reward4box(boxesCompleted1)
            totalAgent1Boxes += boxesCompleted1
            # learn
            print("game currState1: ", self.env.currState)
            self.qClass.updateTable(prevState1,
                      agent1action,
                      self.env.currState,
                      R1)
            
            # if game finished then exit while loop
            if self.env.isDone:
                break
            
            # agent2 move
            R2 = 0
            # store previous state
            prevState2 = self.env.currState
            # get agent action from policy
            agent2action = self.agent2.getAction(self.qClass,
                                                 self.env.currState,
                                                 self.env.possibleActions())
            # do action and calculate reward
            boxesCompleted2 = self.env.doAction(agent2action)
            R2 = self.reward.reward4box(boxesCompleted2)
            totalAgent2Boxes += boxesCompleted2
            # learn
            print("game currState2: ", self.env.currState)
            self.qClass.updateTable(prevState2,
                              agent2action,
                              self.env.currState,
                              R2)
        # learn from the win
        if boxesCompleted1 == boxesCompleted2:
            winner = 0
        elif boxesCompleted1>boxesCompleted2:
            winner = 1
        else: # boxesCompleted1>boxesCompleted2
            winner = 2
        
        if winner == 1:
            R1 = self.reward.reward4win()
            # learn
            self.qClass.updateTable(prevState1,
                              agent1action,
                              self.env.currState,
                              R1)
            print("Winner Agent 1")
        elif winner == 2:
            self.qClass.updateTable(prevState2,
                          agent2action,
                          self.env.currState,
                          R2)
            print("Winner Agent 2")
        else:
            print("Draw")
            