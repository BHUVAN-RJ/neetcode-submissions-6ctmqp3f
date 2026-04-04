class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        freq = [[-cnt, char] for char,cnt in count.items()]
        res = ''
        prev = None
        while len(res) < len(s):
            heapq.heapify(freq)
            cur = 0
            if prev and freq[cur][1] == prev:
                if len(freq) >=2:
                    cur = 1
                else:
                    return ""
            res += freq[cur][1]
            freq[cur][0] += 1
            prev = freq[cur][1]
            if freq[cur][0] == 0:
                del freq[cur]
        return res



        