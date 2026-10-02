class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Attempt before conceptual 
        res = [] 
        current = 0 
        while current < len(nums):
            total = 1  
            for num in nums: 
                if num == nums[current]: 
                    continue 
                else:
                    total *= num

            res.append(total)
            current += 1 
        return res
        """
        res = [] 
        pre = 1 
        post = 1
        for i in range(len(nums)): 
            res.append(pre)
            pre *= nums[i]
        for j in range(len(nums) -1, -1, -1):
            res[j] *= post
            post *= nums[j]
        return res 
        


        