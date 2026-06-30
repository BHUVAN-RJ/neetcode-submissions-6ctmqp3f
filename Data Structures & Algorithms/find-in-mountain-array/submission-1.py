class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        l,r = 0, length - 1
        m = None
        while l <= r:
            m = (l+r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        l,r = 0, peak
        while l <= r:
            m = (l+r) // 2
            curnum = mountainArr.get(m)
            if  curnum < target:
                l = m + 1
            elif curnum > target:
                r = m - 1
            else:
                return m
        
        l ,r = peak + 1, length - 1
        while l <= r:
            m = (l+r) // 2
            curnum = mountainArr.get(m)
            if curnum < target:
                r = m - 1
            elif curnum > target:
                l = m + 1
            else:
                return m
        
        return -1



        
        