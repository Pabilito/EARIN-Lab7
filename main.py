import numpy as np

#Bernoulli distribution - returns 1 with probability p, and 0 with probability 1-p
def Bernoulli(p):
    return(int(np.random.random()<p))

def X_Y(y_old):
    if y_old == 0: #previous y was 0 (test was negative)
        return Bernoulli(0.05) #Probability of cancer is 0.05
    else:
        return Bernoulli(0.85) #Probability of cancer is 0.85

def Y_X(x_old):
    # P(Y|X) = (P(X|Y))*P(Y))/P(X)
    # AND
    # P(0|X) + P(1|X) = 1
    if x_old == 0: #previous x was 0 (patient did not have cancer)
        # 😥 = to fill with real value
        #P(Y=1|X=0) = (P(X=0|Y=1) * P(Y=1)) / P(X=0)
        #P(Y=1|X=0) = (0.15 * P(Y=1)) / 0.99
        #P(Y=0|X=0) = (0.95 * P(Y=0)) / 0.99
        #P(Y=0) = 1 - P(Y=1)
        #P(Y=0|X=0) = (0.95 * [1 - P(Y=1)]) / 0.99
        #[(0.95 * [1 - P(Y=1)]) / 0.99] + [(0.15 * P(Y=1)) / 0.99] = 1
        #P(Y=1) = -0.04      P(Y=0) = 1.04  Nie mam pytań
        #P(Y=1|X=0) = (0.15 * 😥 ) / 0.99 = 😥
        return Bernoulli(😥)
    else:
        #P(Y=1|X=1) = (P(X=1|Y=1) * P(Y=1)) / P(X=1)
        #P(Y=1|X=1) = (0.85 * P(Y=1)) / 0.01
        #P(Y=0|X=1) = (0.05 * P(Y=0)) / 0.01
        #[(0.05 * [1-P(Y=1)]) / 0.01] + [(0.85 * P(Y=1)) / 0.01] = 1
        #P(Y=1) = -0.05 
        return Bernoulli(😥)


def GibbsSampling(old_state, mixture, stepsize):
    
    # x is cancer; y is test
    # Values swapped to make sense
    # P(X=1|Y=1) = 0.85
    # P(X=1|Y=0) = 0.05
    # P(X=0|Y=1) = 0.15
    # P(X=0|Y=0) = 0.95
    # P(X=0) = 0.99
    # P(X=1) = 0.01

    x_old, y_old = old_state  
    x_old = np.array([x_old])

    # Draw new x conditioned on y
    x_new = X_Y(x_old)
