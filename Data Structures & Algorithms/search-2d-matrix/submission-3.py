class Solution:
    def binary_search_row(self, l:int, r:int, nums:List[int], target:int) -> bool:
        m = l + (r-l)//2
        if l > r:
            return False
        if nums[m] == target:
            return True
        if nums[m] < target:
            return self.binary_search_row(m+1, r, nums, target)
        return self.binary_search_row(l, r-1, nums, target)
    def binary_search_col(self, l:int, r:int, matrix: List[List[int]], target:int) -> int:
        m = l + (r-l)//2
        if l > r:
            return -1
        if matrix[m][0] <= target <= matrix[m][-1]:
            return m

        if matrix[m][0] < target:
            return self.binary_search_col(m+1, r, matrix, target)
        return self.binary_search_col(l, m-1, matrix, target)
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.binary_search_col(0, len(matrix)-1, matrix, target)
        if row == -1:
            return False
        return self.binary_search_row(0, len(matrix[row])-1, matrix[row], target)