"""
Eulerian path is a trail in a finite graph that visits every edge exactly once. Vertices can be revisited.

There are two algorithms used to construct eulerain paths in graphs:
1. Fleury's algorithm
2. Hierholzer's algorithm
"""

from copy import copy


# BFS
def isConnected(G):
    start_node = list(G)[0]
    color = {v: "white" for v in G}
    color[start_node] = "gray"
    S = [start_node]
    while len(S) != 0:
        u = S.pop()
        for v in G[u]:
            if color[v] == "white":
                color[v] = "gray"
                S.append(v)
            color[u] = "black"

    return list(color.values()).count("black") == len(G)


def from_dict(G):
    return [(u, v) for u in G for v in G[u]]


def fleury(G):
    oddDegreeNodes = [u for u in G if len(G[u]) % 2 != 0]

    if len(oddDegreeNodes) > 2 or len(oddDegreeNodes) == 1:
        return False

    g = copy(G)
    trail = []
    u = oddDegreeNodes[0] if len(oddDegreeNodes) == 2 else list(g)[0]

    while len(from_dict(g)) > 0:
        current_vertex = u
        for u in g[current_vertex]:
            g[current_vertex].remove(u)
            g[u].remove(current_vertex)
            bridge = not isConnected(g)

            if bridge:
                g[current_vertex].append(u)
                g[u].append(current_vertex)

            else:
                break

        if bridge:
            g[current_vertex].remove(u)
            g[u].remove(current_vertex)
            g.pop(current_vertex)

        trail.append((current_vertex, u))

    return trail
