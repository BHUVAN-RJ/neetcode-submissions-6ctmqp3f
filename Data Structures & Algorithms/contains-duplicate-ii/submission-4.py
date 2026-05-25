class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for l in range(len(nums)):
            r = l + k + 1
            visited = set()
            for i in range(l, min(r, len(nums))):
                if nums[i] in visited:
                    return True
                else:
                    visited.add(nums[i])
        return False


        