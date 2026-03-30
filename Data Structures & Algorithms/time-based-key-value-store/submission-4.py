class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        curVal = self.store.get(key, [])
        l = 0
        r = len(curVal) - 1
        while l <= r:
            m = (l + r) // 2
            if curVal[m][1] <= timestamp:
                res = curVal[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
