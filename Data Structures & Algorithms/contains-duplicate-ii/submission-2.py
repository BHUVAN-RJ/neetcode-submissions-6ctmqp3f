class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                for item in visited[nums[i]]:
                    if i - item <= k:
                        return True
            
            visited[nums[i]] = visited.get(nums[i], []) + [i]
        return False
        