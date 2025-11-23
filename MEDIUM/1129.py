#   

# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

#     redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
#     blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        red, blue = defaultdict(list), defaultdict(list)

        for i, j in redEdges:
            red[i].append(j)

        for i, j in blueEdges:
            blue[i].append(j)

        answer = [-1 for i in range(n)]
        q = deque()
        q.append((0, 0, None))
        visit = set()
        visit.add((0, None))

        while q:
            node, length, edgeColor = q.popleft()
            if answer[node] == -1:
                answer[node] = length

            if edgeColor != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append((nei, length + 1, "RED"))

            if edgeColor != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append((nei, length + 1, "BLUE"))

        return answer