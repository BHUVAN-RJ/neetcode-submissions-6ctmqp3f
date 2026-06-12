class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        num1 = -1
        num2 = -1
        for i in nums:
            if num1 == i:
                cnt1 += 1
            elif num2 == i:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = i
                cnt1 = 1
            elif cnt2 == 0:
                num2 = i
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        res = []
        cnt1 = cnt2 = 0
        for i in nums:
            if i == num1:
                cnt1 += 1
            elif i == num2:
                cnt2 += 1
        if cnt1 > len(nums) // 3:
            res.append(num1)
        if cnt2 > len(nums) // 3:
            res.append(num2)
        return res