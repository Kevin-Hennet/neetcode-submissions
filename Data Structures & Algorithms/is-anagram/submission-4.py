class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s = sorted(s)
        #t = sorted(t)
        #return s == t
        # too simple of a solution we are running this back
        if len(s) != len(t):
            return False 
        count_s = {}
        count_t = {}
        for char in s: 
            if char not in count_s: 
                count_s[char] = 1
            else: 
                count_s[char] += 1
        for char in t: 
            if char not in count_t: 
                count_t[char] = 1
            else:
                count_t[char] += 1 
        for char in count_s:
            if char not in count_t or count_s[char] != count_t[char]: 
                return False 
        return True 
        
        