class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 2 person per boat - and the combined weight should be less than limit
        l, r = 0, len(people) - 1
        res = 0
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                r -= 1
                l += 1
            else:
                r -= 1
                res += 1
        return res
        
            
            
                



        