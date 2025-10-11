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

import numpy as np
def floyd_alg(W, k, D, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


W = [[0, 1, np.inf, 1, 5],
     [9, 0, 3, 2, np.inf],
     [np.inf, np.inf, 0, 4, np.inf],
     [np.inf, np.inf, 2, 0, 3],
     [3, np.inf, np.inf, np.inf, 0]]
D = [row[:] for row in W] # D^0 = W
W = np.array(W)
print(floyd_alg(W, 5, D, 5))

Problem 10:
Can Floyd’s algorithm for the Shortest Paths problem 2 (Algorithm 3.4) be
used to find the shortest paths in a graph with some negative weights? Justify
your answer.

There can be negative weights in the graph because the algorithm is summing the weights of the path, but 
only if there isn't a negative cycle where the length of a path is negative and points back to the vertex
to then create an infinite cycle of finding a shortest length.

Problem 12:
List all of the different orders in which we can multiply five matrices A, B,
C, D, and E

A(B(C(DE)))
A(B((CD)E))
A((BC)(DE))
A((B(CD))E)
A(((BC)D)E)
(AB)(C(DE))
(AB)((CD)E)
(A(BC))(DE)
((AB)C)(DE)
(A(B(CD)))E
(A((BC)D))E
((AB)(CD))E
((A(BC))D)E
(((AB)C)D)E

Problem 28:

"""

