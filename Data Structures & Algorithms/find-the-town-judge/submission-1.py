class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # incoming = defaultdict(int)
        # outgoing = defaultdict(int)
        delta = defaultdict(int) # out - in

        for src, dst in trust:
            delta[src] -= 1
            delta[dst] += 1
        
        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i
        return -1
        