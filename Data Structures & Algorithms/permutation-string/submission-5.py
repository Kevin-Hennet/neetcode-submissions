class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_frequency = {}
        for i in range(len(s1)): 
            s1_frequency[s1[i]] = 1 + s1_frequency.get(s1[i], 0)

        l = 0 
        r = l + (len(s1) - 1)
        substring = {}
        
        for j in range(l, r + 1): 
            substring[s2[j]] = 1 + substring.get(s2[j], 0)
        
        while r < len(s2):
            if substring == s1_frequency: 
                return True 
            else:
                substring[s2[l]] -= 1
                if substring[s2[l]] == 0: 
                    del substring[s2[l]]
                l += 1 
                r += 1
                if r < len(s2):
                    substring[s2[r]] = 1 + substring.get(s2[r], 0)
        return False 
            
            
            