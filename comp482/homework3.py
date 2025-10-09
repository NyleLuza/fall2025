"""
Problem 4:
def bin_coeff(n, k):
    memo = [0 for j in range(k + 1)]
    memo[0] = 1
    
    for i in range(n+1): # inclusive because we need n
        for j in range(min(i,k),0,-1): # need to go backwards to preserve data
            memo[j] = memo[j] + memo[j-1]
    return memo[k]
print(bin_coeff(4, 2))

Problem 7:
This is linear time complexity because you can visit at most n-1 vertices

Problem 8:
"""
import numpy as np
def floyd_alg(W, k, D, n=5):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                

W = [[0, 1, np.inf, 1, 5],
     [9, 0, 3, 2, np.inf],
     [np.inf, np.inf, 0, 4, np.inf],
     [np.inf, np.inf, 2, 0, 3],
     [3, np.inf, np.inf, np.inf, 0]]
D = [row[:] for row in W] # D^0 = W
W = np.array(W)


