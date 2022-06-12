import numpy as np

#Bernoulli distribution - returns 1 with probability p, and 0 with probability 1-p
def bernoulli(p):
    return(int(np.random.random()<p))

class State:
    def __init__(self, Y, X, probability):
        self.Y = Y
        self.X = X
        self.probability = probability
        self.counter = 0
    def update(self):
        self.counter += 1

def getProbabilityOfY(probability_X, state_F_F, state_T_F):
    probability_y_true = (state_F_F.probability + state_T_F.probability) * probability_X
    return probability_y_true

def getInitialStates():
    T_T = State(True, True, 0.9)
    T_F = State(True, False, 0.2)
    F_T = State(False, True, 0.1)
    F_F = State(False, False, 0.8)
    return T_T, T_F, F_T, F_F

def createListOfStates():
    states = []
    T_T, T_F, F_T, F_F = getInitialStates()
    states.append(T_T)
    states.append(T_F)
    states.append(F_T)
    states.append(F_F)
    return states

def getState(states, Y, X):
    for s in states:
        if s.X == X and s.Y == Y:
            return s
    return None #error - no such state

def drawRandomState(states, p_y):
    Y = bernoulli(p_y)
    X = bernoulli(0.05)
    s = getState(states, Y, X)
    return s

def changeState(states, current_state, change_X, p_y):
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
    probability_of_y = getProbabilityOfY(0.95, states[2], states[3])
    current_state = drawRandomState(states, probability_of_y)
    current_state.update()
    for i in range(k):
        current_state = randomWalk(states, current_state, probability_of_y)

    suma = 0
    for s in states:
        print("Stan:", s.Y, s.X, " the counter: ", s.counter)
        suma += s.counter
    print("Stan:", s.Y, s.X, " the probability: ", s.counter / suma)
'''    
    



def XonConditionY(y_old):
    if y_old == 0: #previous y was 0 (test was negative)
        return bernoulli(0.05) #Probability of cancer is 0.05
    else:
        return bernoulli(0.85) #Probability of cancer is 0.85

def YonConditionX(x_old):
    # P(Y|X) = (P(X|Y))*P(Y))/P(X)
    # AND
    # P(0|X) + P(1|X) = 1
    if x_old == 0: #previous X was 0 (patient did not have cancer)
        # 😥 = to fill with real value
        #P(Y=1|X=0) = (P(X=0|Y=1) * P(Y=1)) / P(X=0)
        #P(Y=1|X=0) = (0.10 * P(Y=1)) / 0.95
        #P(Y=0|X=0) = (0.80 * P(Y=0)) / 0.95
        #P(Y=0) = 1 - P(Y=1)
        #P(Y=0|X=0) = (0.80 * [1 - P(Y=1)]) / 0.95
        #[(0.80 * [1 - P(Y=1)]) / 0.95] + [(0.10 * P(Y=1)) / 0.95] = 1
        #(16/19) * [1 - P(Y=1)] + (2/19) * P(Y=1) = 1
        #(16/19) - 14/19 P(Y=1) = 1
        # 
        #P(Y=1) = -0.04      P(Y=0) = 1.04  Nie mam pytań
        #P(Y=1|X=0) = (0.15 * 😥 ) / 0.99 = 😥
        return bernoulli(😥)
    else:
        #P(Y=1|X=1) = (P(X=1|Y=1) * P(Y=1)) / P(X=1)
        #P(Y=1|X=1) = (0.85 * P(Y=1)) / 0.01
        #P(Y=0|X=1) = (0.05 * P(Y=0)) / 0.01
        #[(0.05 * [1-P(Y=1)]) / 0.01] + [(0.85 * P(Y=1)) / 0.01] = 1
        #P(Y=1) = -0.05 
        return bernoulli(😥)


def GibbsSampling(old_state, mixture, stepsize):
    
    # x is cancer; y is test
    # Values swapped to make sense
    # P(X=1|Y=1) = 0.90
    # P(X=1|Y=0) = 0.20
    # P(X=0|Y=1) = 0.10
    # P(X=0|Y=0) = 0.80
    # P(X=0) = 0.95
    # P(X=1) = 0.05

    x_old, y_old = old_state
    x_old = np.array([x_old])

    # Draw new x conditioned on y
    x_new = XonConditionY(x_old)
'''
