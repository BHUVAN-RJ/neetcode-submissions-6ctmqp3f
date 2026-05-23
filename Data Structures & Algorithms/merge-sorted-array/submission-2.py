class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1 = m - 1
        arr2 = n - 1
        ptr = m + n - 1

        while arr1 >= 0 and arr2 >= 0:
            if nums1[arr1] < nums2[arr2]:
                nums1[ptr] = nums2[arr2]
                arr2 -= 1
            else:
                nums1[ptr] = nums1[arr1]
                arr1 -= 1
            ptr -= 1
        while arr2 >= 0:
            nums1[ptr] = nums2[arr2]
            ptr -= 1
            arr2 -= 1



