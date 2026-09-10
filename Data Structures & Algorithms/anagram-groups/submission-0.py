class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_test = "".join(sorted(s))
            res[sorted_test].append(s)
        return list(res.values())