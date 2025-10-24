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

Problem 29:
def travel(W):
    n = len(W) - 1  # assume W is 1-indexed: W[1..n][1..n]

    # init D and P
    D = {}  # D[(i, A)] = min distance to start at 1, visit A, and end at i
    P = {}  # P[(i, A)] = index of the vertex j that gave the minimum

    # base case
    for i in range(2, n + 1):
        D[(i, frozenset())] = W[i][1]

    # for subsets A of {2,...,n} of increasing size
    for k in range(1, n - 1):
        for A in combinations(range(2, n + 1), k):
            A = frozenset(A)
            for i in range(2, n + 1):
                if i in A:
                    continue
                # D[i][A] = min over j in A of (W[i][j] + D[j][A - {j}])
                best_cost = inf
                best_j = None
                for j in A:
                    cost = W[i][j] + D[(j, A - {j})]
                    if cost < best_cost:
                        best_cost = cost
                        best_j = j
                D[(i, A)] = best_cost
                P[(i, A)] = best_j

    # compute the minimum tour cost ending back at 1
    full_set = frozenset(range(2, n + 1))
    best_cost = inf
    best_j = None
    for j in range(2, n + 1):
        cost = W[1][j] + D[(j, full_set - {j})]
        if cost < best_cost:
            best_cost = cost
            best_j = j

    minlength = best_cost
    P[(1, full_set)] = best_j

    return minlength, P

Problem 30:
def generate_random_tsp(n, max_dist=50):
    # Generate a random symmetric distance matrix for n cities
    W = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                W[i][j] = 0
            else:
                W[i][j] = W[j][i] = random.randint(1, max_dist)
    return W


# check performance
for n in range(4, 11):  # test for 4 to 10 cities
    W = generate_random_tsp(n)
    start = time.time()
    cost = travel(W)
    end = time.time()
    print(f"{n} cities: cost = {cost:5}, time = {end - start:.4f} seconds")

Problem 38:
Use the dynamic programming approach to write an algorithm to find the
maximum sum in any contiguous sublist of a given list of n real values.
Analyze your algorithm, and show the results using order notation.

def contigous(n):
    current_sum = 0
    best_sum = 0
    for i in range(len(n)):
        current_sum = max(n[i], n[i] + current_sum)
        best_sum = max(best_sum, current_sum)
    return best_sum

A = [5, -2, 7, 1, -3]
print(contigous(A))
"""






