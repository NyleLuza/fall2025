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
Find an optimal circuit for the weighted, direct graph represented by the
following matrix W. Show the actions step by step.

D[1][{v2, v3, v4, v5}] = min(W[1][j] + D[j][{v2, v3, v4, v5} - {vj}]
         = min(W[1][2] + D[2][{v3, v4, v5}],
               W[1][3] + D[3][{v2, v4, v5}],
               W[1][4] + D[4][{v2, v3, v5}],
               W[1][5] + D[5][{v2, v3, v4}]) = min(8 + 21, 13 + 17, 18 + 22, 20 + 18) = 29

D[2][{v3, v4, v5}] = min(W[2][3] + D[3][{v4, v5}],
                          W[2][4] + D[4][{v3, v5}],
                          W[2][5] + D[5][{v2, v3}]) = min(7 + 14, 8 + 17, 10 + 16) = 21

    D[3][{v4, v5}] = min(W[3][4] + D[4][{v5}],
                          W[3][5] + D[5][{v4}]) = min(10 + 21, 7 + 7) = 14
        D[4][{v5}] = min(W[4][5] + D[5][{}]) = 11 + 10 = 21
        D[5][{v4}] = min(W[5][4] + D[4][{}]) = 6 + 1 = 7
    
    D[4][{v3, v5}] = min(W[4][3] + D[3][{v5}],
                          W[4][5] + D[5][{v3}]) = min(7 + 17, 11 + 6) = 17
        D[3][{v5}] = min(W[3][5] + D[5][{}]) = 7 + 10 = 17
        D[5][{v3}] = min(W[5][3] + D[3][{}]) = 2 + 4 = 6

    D[5][{v2, v3}] = min(W[5][2] + D[2][{v3}],
                          W[5][3] + D[3][{v2}]) = min(6 + 11, 2 + 14) = 16
        D[2][{v3}] = min(W[2][3] + D[3][{}]) = 7 + 4 = 11
        D[3][{v2}] = min(W[3][2] + D[2][{}]) = 11 + 3 = 14

D[3][{v2, v4, v5}] = min(W[3][2] + D[2][{v4, v5}],
                          W[3][4] + D[4][{v2, v5}],
                          W[3][5] + D[5][{v2, v4}]) = min(11 + 17, 10 + 20, 7 + 10) = 17

    D[2][{v4, v5}] = min(W[2][4] + D[4][{v5}],
                          W[2][5] + D[5][{v4}]) = min(8 + 21, 10 + 7) = 17
        D[v4][{v5}] = min(W[4][5] + D[5][{}]) = 11 + 10 = 21
        D[v5][{v4}] = min(W[5][4] + D[4][{}]) = 1 + 6 = 7
    
    D[4][{v2, v5}] = min(W[4][2] + D[2][{v5}],
                          W[4][5] + D[5][{v2}]) = min(6 + 20, 11 + 9) = 20
        D[2][{v5}] = min(W[2][5] + D[5][{}]) = 10 + 10 = 20
        D[5][{v2}] = min(W[5][2] + D[2][{}]) = 6 + 3 = 9
    
    D[5][{v2, v4}] = min(W[5][2] + D[2][{v4}],
                          W[5][4] + D[4][{v2}]) = min(6 + 14, 1 + 9) = 10
        D[2][{v4}] = min(W[2][4] + D[4][{}]) = 8 + 6 = 14
        D[4][{v2}] = min(W[4][2] + D[2][{}]) = 6 + 3 = 9

D[4][{v2, v3, v5}] = min(W[4][2] + D[2][{v3, v5}],
                         W[4][3] + D[3][{v2, v5}],
                         W[4][5] + D[5][{v2, v3}]) = min(6 + 16, 7 + 16, 11 + 16) = 22
    
    D[2][{v3, v5}] = min(W[2][3] + D[3][{v5}],
                         W[2][5] + D[5][{v3}]) = min(7 + 17, 10 + 6) = 16
        D[3][{v5}] = min(W[3][5] + D[5][{}]) = 7 + 10 = 17
        D[5][{v3}] = min(W[5][3] + D[3][{}]) = 2 + 4 = 6

    D[3][{v2, v5}] = min(W[3][2] + D[2][{v5}],
                         W[3][5] + D[5][{v2}]) = min(11 + 20, 7 + 9) = 16
        D[2][{v5}] = min(W[2][5] + D[5][{}]) = 10 + 10 = 20
        D[5][{v2}] = min(W[5][2] + D[2][{}]) = 6 + 3 = 9
    
    D[5][{v2, v3}] = min(W[5][2] + D[2][{v3}],
                         W[5][3] + D[3][{v2}]) = min(6 + 11, 2 + 14) = 16
        D[2][{v3}] = min(W[2][3] + D[3][{}]) = 7 + 4 = 11
        D[3][{v2}] = min(W[3][2] + D[2][{}]) = 11 + 3 = 14

D[5][{v2, v3, v4}] = min(W[5][2] + D[2][{v3, v4}],
                         W[5][3] + D[3][{v2, v4}],
                         W[5][4] + D[4][{v2, v3}]) = min(6 + 19, 2 + 19, 1 + 17) = 18

    D[2][{v3, v4}] = min(W[2][3] + D[3][{v4}],
                         W[2][4] + D[4][{v3}]) = min(7 + 16, 8 + 11) = 19
        D[3][{v4}] = min(W[3][4] + D[4][{}]) = 10 + 6 = 16
        D[4][{v3}] = min(W[4][3] + D[3][{}]) = 7 + 4 = 11
    
    D[3][{v2, v4}] = min(W[3][2] + D[2][{v4}],
                         W[3][4] + D[4][{v2}]) = min(11 + 14, 10 + 9) = 19
        D[2][{v4}] = min(W[2][4] + D[4][{}]) = 8 + 6 = 14
        D[4][{v2}] = min(W[4][2] + D[2][{}]) = 6 + 3 = 9
    
    D[4][{v2, v3}] = min(W[4][2] + D[2][{v3}],
                         W[4][3] + D[3][{v2}]) = min(6 + 11, 7 + 14) = 17
        D[2][{v3}] = min(W[2][3] + D[3][{}]) = 7 + 4 = 11
        D[3][{v2}] = min(W[3][2] + D[2][{}]) = 11 + 3 = 14
    
Optimal Circuit = v1 -> v2 -> v3 -> v5 -> v4 -> v1
Shortest Length = 29

Problem 30:
import numpy as np

W = [[0, 8, 13, 18, 20],
    [3, 0, 7, 8, 10],
    [4, 11, 0, 10, 7],
    [6, 6, 7, 0, 11],
    [10, 6, 2, 1, 0]]

W = np.array(W)
D = np.full(W.shape, np.inf, dtype=int)

def shortest_path(W, D, n)
for i in range(n):
    for j in range(n):
        D[i][j] = min()

Problem 38:
Use the dynamic programming approach to write an algorithm to find the
maximum sum in any contiguous sublist of a given list of n real values.
Analyze your algorithm, and show the results using order notation.

"""
import numpy as np
def contigous(n, memo):
    for i in range(len(n)):
        for j in range(len(n)):
            if memo[i][j] != np.inf
                if n 

A = [5, -2, 7, 1, -3, 2, 3, -5, 2]
memo = np.full(len(A), np.inf, dtype=int)
print(contigous(A), memo)


