class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        my attempt 
        l = 0 
        r = len(nums) - 1
        while l <= r: 
            mid = (l+r) // 2
            if nums[mid] == target: 
                return mid 
            elif nums[mid] > target and target >= nums[l]: 
                r = mid -1 
            elif nums[mid] > target and nums[mid] >= nums[l]:
                l = mid + 1 
            elif nums[mid] < target and target <= nums[r]: 
                l = mid + 1 
            else: 
                r = mid - 1
        return - 1
        """
        l = 0 
        r = len(nums) - 1
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid 
            
            elif nums[mid] >= nums[l]:
                if nums[mid] > target and target >= nums[l]: 
                    r = mid - 1

                else: 
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]: 
                    l = mid + 1
                else: 
                    r = mid - 1
        return -1 




        