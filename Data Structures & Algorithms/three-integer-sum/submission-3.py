class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        attempt before conceptual 
        result = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] >= nums[j]:
                    nums[i] , nums[j] = nums[j], nums[i]
        
        i = 0 
        j = len(nums) -1
        k = len(nums) // 2
        while (i < j):
            if nums[i] + nums[j] + nums[k] == 0: 
                result.append([nums[i], nums[j], nums[k]])
            elif nums[i] + nums[j] + nums[k] < 0: 
                i += 1 
                k += 1 
            else: 
                j -= 1 
                k -= 1
        return result 
        """
        #attempt after conceptual part 
        result = []  
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        a = 0 
        while (a < len(nums)-1):
            b = a + 1 
            c = len(nums) - 1  
            while (b < c):
                if nums[a] + nums[b]+ nums[c] == 0: 
                    result.append([nums[a], nums[b], nums[c]])
                    b += 1 
                    c -= 1 
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                elif nums[a] + nums[b]+ nums[c] < 0: 
                    b += 1 
                else: 
                    c -= 1
            a += 1 
            while a < len(nums) - 2 and nums[a] == nums[a - 1]:
                a += 1

        return result 


            
        
        