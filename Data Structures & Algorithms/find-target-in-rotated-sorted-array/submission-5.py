class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        # [3,4,5,6,1,2], target = 1
        # [1,2,3,4,5,6], target = 4
        # do binary search to find pivot
        # pivot is where left number is bigger than right
        # do this by comparing midpoint to right
        # after finding pivot, we can run bs on the values either to left
        # or right of pivot
        
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        def binary_search(l:int, r:int) -> int:
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        res = binary_search(0, pivot-1)
        if res != -1:
            return res
        
        return binary_search(pivot, len(nums)-1)
        
                        

            
        





