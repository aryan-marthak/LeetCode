# 451. Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# bucket sort solution

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        buckets = defaultdict(list)

        for char, cnt in count.items():
            buckets[cnt].append(char)

        res = ""
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res += c * i

        return res
    
# heaps
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        temp = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(temp)
        result = ''
        while temp:
            freq, char = heapq.heappop(temp)
            result += char * -freq
        return result