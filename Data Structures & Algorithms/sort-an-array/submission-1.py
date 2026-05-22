class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            leftarr = arr[L:M+1]
            rightarr = arr[M+1:R+1]
            left = 0
            right = 0
            mid = L
            while left < len(leftarr) and right < len(rightarr):
                if leftarr[left] <= rightarr[right]:
                    arr[mid] = leftarr[left]
                    left += 1
                else:
                    arr[mid] = rightarr[right]
                    right += 1
                mid += 1
            
            while left < len(leftarr):
                arr[mid] = leftarr[left]
                left += 1
                mid += 1
            
            while right < len(rightarr):
                arr[mid] = rightarr[right]
                right += 1
                mid += 1
                

        
        def mergesort(arr, l, r):
            if l >= r:
                return arr
            m = (l + r) // 2
            mergesort(arr, l, m)
            mergesort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        return mergesort(nums, 0, len(nums))

            
        