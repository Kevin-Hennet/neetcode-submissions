class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        my attempt before conceptual
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]: 
            return nums[l]
        res = nums[l]
        while l <= r: 
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]: 
                l = mid + 1
                res = nums[r] 
            elif nums[mid] < nums[r]: 
                r = mid - 1
                res = nums[mid]
            elif nums[mid] > nums[l]: 
                r = mid - 1
                res = nums[l]
            else: 
                l = mid + 1
        return res
        attempt 2 
        l = 0 
        r = len(nums) - 1
        res = nums[(l+r) // 2]
        while l <= r: 
            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[l] < nums[r]: 
                res = nums[l]
                break 
            if nums[mid] >= nums[l]: 
                l = mid + 1
            else: 
                r = mid - 1
        return res 
        """
        # had to watch the vid solution 
        res = nums[0]
        l, r = 0, len(nums) -1 
        
        while l <= r: 
            if  nums[l] < nums[r]: 
                res = min(res, nums[l])
                break 
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: 
                l = m + 1
            else: 
                r = m - 1
        return res 
                

        
