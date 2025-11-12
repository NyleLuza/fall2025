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


def prim(G, start):
    F = set()          # Edges in the minimum spanning tree
    Y = {start}        # Set of vertices already in the tree
    V = set(G.keys())  # All vertices

    while Y != V:
        min_edge = None
        min_weight = float('inf')

        # Look at all edges from Y to V-Y
        for u in Y:
            for v, w in G[u].items():
                if v not in Y and w < min_weight:
                    min_edge = (u, v, w)
                    min_weight = w

        if min_edge is None:
            break  # Graph may not be connected

        F.add(min_edge)
        Y.add(min_edge[1])

    return F

graph = {
    'v1':{'v2':1, 'v3':3},
    'v2':{'v1':1, 'v3':3, 'v4':6},
    'v3':{'v1':3, 'v2':3, 'v4':4, 'v5':2},
    'v4':{'v2':6, 'v3':4, 'v5':5},
    'v5':{'v3':2, 'v4':5}
}
print(prim(graph, 'v1'))

9. Do you think it is possible for a minimum spanning tree to have a cycle?
Justify your answer.

No because a tree is a a connected acyclic graph so an mst cant have a cycle
because then it wouldn't be a tree

10. Assume that in a network of computers any two computers can be linked.
Given a cost estimate for each possible link, should Algorithm 4.1 (Prim’s
algorithm) or Algorithm 4.2 (Kruskal’s algorithm) be used? Justify your
answer

Prims alg would be the more optimal alg to use because kruskal's alg would need
to sort all edges which would take logn time. Prim's avoids this by using a simple array
to track the min edge for each vertex

17. Can Dijkstra’s algorithm (Algorithm 4.3) be used to find the shortest paths in
a graph with some negative weights? Justify 

No it can't be used on graphs with negative edge weights because the algorithm assumes
that once the shortest distance to a vertex is found it will never change. So if a graph
contains a negative weight, a path that seemed longer at first might become shorter by passing through the
negative edge, but the alg will already finalized the earlier distance.

19. Consider the following jobs and service times. Use the algorithm in Section
4.3.1 to minimize the total amount of time spent in the system.
Job Service Time
1   7
2   3
3   10
4   5
"""
