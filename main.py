import numpy as np

def bernoulli(p):
    #Bernoulli distribution - returns 1 with probability p, and 0 with probability 1-p
    return(int(np.random.random()<p))

class State:
    #Class to store count of occurrances of a particular state (combination of result of X and Y)
    def __init__(self, Y, X, probability):
        self.Y = Y
        self.X = X
        self.probability = probability
        self.counter = 0
    def update(self):
        self.counter += 1

def getProbabilityOfY(probability_X, state_T_T, state_T_F):
    #Retruns probability of test being positive
    probability_y_true = state_T_T.probability  * probability_X + state_T_F.probability * (1-probability_X)
    return probability_y_true

def getInitialStates():
    #Test_Cancer
    #We have slightly modified values, because the ones in the task did not add up to 1 properly
    T_T = State(True, True, 0.9)
    T_F = State(True, False, 0.2)
    F_T = State(False, True, 0.1)
    F_F = State(False, False, 0.8)
    return T_T, T_F, F_T, F_F

def createListOfStates():
    #We define 4 states (confusion matrix)
    states = []
    T_T, T_F, F_T, F_F = getInitialStates()
    states.append(T_T)
    states.append(T_F)
    states.append(F_T)
    states.append(F_F)
    return states

def getState(states, Y, X):
    #Returns one of four states
    for s in states:
        if s.X == X and s.Y == Y:
            return s
    return None #error - no such state

def drawRandomState(states, p_y):
    #Within the first iteration we want to perform a random choice of the first step
    Y = bernoulli(p_y)
    X = bernoulli(0.05)
    s = getState(states, Y, X)
    return s

def changeState(states, current_state, change_X, p_y):
    #Get a new state within our random walk
    s = current_state
    if change_X:
        new_X = bernoulli(0.05)
        s = getState(states, current_state.Y, new_X)
    else:
        new_Y = bernoulli(p_y)
        s = getState(states, new_Y, current_state.X)
    return s

def randomWalk(states, current_state, p_y):
    current_state = changeState(states, current_state, bernoulli(0.5), p_y)
    current_state.update()
    return current_state

def main(k):
    states = createListOfStates()
    probability_of_y = getProbabilityOfY(0.05, states[0], states[1])
    #We start with selecting a ranndom state based on probabilities
    current_state = drawRandomState(states, probability_of_y)
    #Then we save its result
    current_state.update()
    #Further, we perform k steps of random walk
    for _ in range(k):
        current_state = randomWalk(states, current_state, probability_of_y)

    for s in states:
        print("State (Test, Cancer):", s.Y, s.X, "the counter: ", s.counter)

    for s in states:
        print("State (Test, Cancer):", s.Y, s.X, "the probability: ", round(s.counter / (k+1), 5))

main(int(input("Please select number of steps: ")))