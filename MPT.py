import numpy as np

#Example
R = np.array([0.0101, 0.0135, 0.0151, 0.0095, 0.0054])

cov = np.array([    [0.0018,	0.0017,	0.0019,	0.0021,	0.0000],
                    [0.0017,	0.0037,	0.0027,	0.0022,	0.0002],
                    [0.0019,	0.0027,	0.0035,	0.0020,	0.0000],
                    [0.0021,	0.0022,	0.0020,	0.0026,	0.0000],
                    [0.0000,	0.0002,	0.0000,	0.0000,	0.0032]])

s = 0.0037

lambda1 = 1
lambda2 = -1

I = 1000000
epsilon = 1e-3

for i in range(I): 
    if(i%100000==0):  
        print(i)     
    w = np.dot(np.linalg.pinv(2*lambda1*cov), R-lambda2)
    
    lambda1 = lambda1 + epsilon*(np.dot(np.dot(w.T, cov), w) - s)
    lambda2 = lambda2 + epsilon*(np.sum(w) - 1)
    
    if np.sum(w) > 0.99999 and np.sum(w) < 1.00001 and np.dot(np.dot(w.T, cov), w) > s - 0.00009 and np.dot(np.dot(w.T, cov), w) < s + 0.00009:
        print(np.dot(np.dot(w.T, cov), w), np.dot(w.T, R))
        break