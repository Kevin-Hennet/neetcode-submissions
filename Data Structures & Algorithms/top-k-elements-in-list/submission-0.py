class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for i in range(k):
            result.append(max(hashmap, key=hashmap.get))
            del hashmap[result[i]]
        return result
                

        