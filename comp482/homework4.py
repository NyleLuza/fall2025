"""
1. Show that the greedy approach always finds an optimal solution for the
Change problem when the coins are in the denominations D0, D1, D2, … , Di
for some integers i > 0 and D > 0.

The greedy approach finds the most optimal problem because the denominator
makes sure that the ratio is still consistent because if a coin were to be
an outlier with a random value, it would make the alg not optimal

4. *Seperate file*

5. Implement Prim's algorithm (Algorithm 4.1) on your system, and study its
performance using different graphs.

"""
def prim(G, start):
    F = set()
    Y = {start}
    V = set(G.keys())
    min_set = set()
    while(Y!=V):
        for vertex in Y:
            for neighbor, weight in G[vertex].items():
                if neighbor not in Y:
                    min_set.add((vertex, neighbor, weight))
            local_min_edge = min(min_set, key = lambda x:x[2])
            F.add(local_min_edge)
            Y.add(local_min_edge[1])
        min_set = set()
            



graph = {
    'v1':{'v2':1, 'v3':3},
    'v2':{'v1':1, 'v3':3, 'v4':6},
    'v3':{'v1':3, 'v2':3, 'v4':4, 'v5':2},
    'v4':{'v2':6, 'v3':4, 'v5':5},
    'v5':{'v3':2, 'v4':5}
}
prim(graph, 'v1')