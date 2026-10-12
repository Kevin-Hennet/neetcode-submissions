class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        my attempt before conceptual 
        start = (0,0)
        end = (len(matrix) -1, len(matrix[len(matrix)- 1]) - 1)
        while start[0] <= end[0]: 
            mid = (((start[0] + end[0]) // 2), ((start[1] + end[1]) // 2))
            if matrix[mid[0]][mid[1]] == target: 
                return True
            elif matrix[mid[0]][mid[1]] > target: 
                start = (mid[0] + 1, mid[1] + 1)
            else: 
                end = (mid[0] -1, mid[1] - 1)
        return False 
        """
        # after conceptual
        start = 0 
        end = len(matrix) -1
        while start <= end: 
            mid_row = (start + end) // 2

            if target < matrix[mid_row][0]:
                end = mid_row - 1
            elif target > matrix[mid_row][len(matrix[mid_row]) -1]: 
                start = mid_row + 1
            else: 
                break 
        if start > end: 
            return False 
        l = 0 
        r = len(matrix[mid_row]) -1
        while l <= r: 
            mid = (l + r) // 2
            if target == matrix[mid_row][mid]: 
                return True 
            elif target < matrix[mid_row][mid]: 
                r = mid - 1
            else: 
                l = mid + 1
        return False 

                

                
