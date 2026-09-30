class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        attempt before conceptual 
        sequence = defaultdict(list)
        current = 0
        sequence[current].append(current)
        res = 0 
        while current != len(nums): 
            if nums[current] + 1 in nums: 
                sequence[current].append(nums[current] + 1)
            else: 
                res = max(len(sequence[current]), res)
                current += 1 
        return res
        """
        set_nums = set(nums)
        res = 0 
        for n in nums:
             
            if n - 1 not in set_nums: 
                length = 0
                while (n + length) in set_nums:
                    length += 1 
                res = max(length, res)
        return res
            







        
        
            