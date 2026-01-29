# 2976. Minimum Cost to Convert String I

# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for src, dst, cur_cost in zip(original, changed, cost):
            adj[src].append((dst, cur_cost))

        def djikstra(src):
            heap = [(0, src)]
            min_cost_map = {}

            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost_map:
                    continue
                min_cost_map[node] = cost
                for nei, nei_cost in adj[node]:
                    heapq.heappush(heap, (cost + nei_cost, nei))
            return min_cost_map
        
        min_cost_maps = {c: djikstra(c) for c in set(source)}
        res = 0
        for src, dst in zip(source, target):
            if dst not in min_cost_maps[src]:
                return -1
            res += min_cost_maps[src][dst]
        return res 