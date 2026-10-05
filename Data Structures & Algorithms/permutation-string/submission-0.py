class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_frequency = {}
        for i in range(len(s1)): 
            s1_frequency[s1[i]] = 1 + s1_frequency.get(s1[i], 0)

        l = 0 
        r = l + (len(s1) - 1)
        substring = {}
        while r < len(s2): 
            for j in range(l, r+1): 
                substring[s2[j]] = 1 + substring.get(s2[j], 0)
            if substring == s1_frequency: 
                return True 
            else:
                substring = {}
                l += 1 
                r += 1
        return False 
            
            
            