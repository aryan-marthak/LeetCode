# 1466. Reorder Routes to Make All Paths Lead to the City Zero

# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        connection = set()
        for start, end in connections:
            neighbors[start].append(end)
            neighbors[end].append(start)
            connection.add((start, end))
        
        curr = [0]
        reverse = 0
        visited = set()
        visited.add(0)
        
        while curr:
            new_curr = []
            for city in curr:
                for n in neighbors[city]:
                    if n not in visited:
                        visited.add(n)
                        if (n, city) not in connection:
                            reverse += 1
                        new_curr.append(n)
            curr = new_curr
        return reverse