class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        hashmap = {}
        result = []
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for i in range(k):
            result.append(max(hashmap, key=hashmap.get))
            del hashmap[result[i]]
        return result
        """
        # Alt solution: 
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: 
                res.append(n)
                if len(res) == k: 
                    return res

                

        