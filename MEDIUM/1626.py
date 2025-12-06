# 1626. Best Team With No Conflicts

# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

# RECURSION WITH MEMOIZATION (TOP-DOWN DP) -> MEMORY limit exceeded on LEETCODE
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))

        cache = {}
        def dfs(i, sc):
            if (i, sc) in cache:
                return cache[(i, sc)]
            if i == len(scores):
                return 0
            skip = dfs(i + 1, sc)
            take = 0
            if players[i][1] >= sc:
                take = players[i][1] + dfs(i + 1, players[i][1])
            cache[(i, sc)] = max(skip, take)
            return cache[(i, sc)]
        return dfs(0, 0)