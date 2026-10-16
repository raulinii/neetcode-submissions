class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r:
            k = (l+r) // 2

            if nums[k] < nums[r]:
                
                r = k
            else:
        
                l = k + 1
            
        return nums[l]
