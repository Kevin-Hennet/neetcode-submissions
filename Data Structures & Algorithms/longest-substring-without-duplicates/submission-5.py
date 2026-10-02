class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Attempt without conceptual
        l = 0 
        r = 1 
        res = 0
        length = 1   
        while (r < len(s)):
            if s[l] != s[r]:
                length += 1
                r+= 1
            else:
                res = max(length, res)
                length = 1
                l = r 
                r = l + 1 
        return res
        """
        if len(s) == 0: 
            return 0 
        duplicates = {s[0]}
        res = 1
        current_substring = s[0]
        
        for i in range(1, len(s)): 
            if s[i] not in duplicates:
                duplicates.add(s[i])
                current_substring = current_substring + s[i]
            else:
                
                while s[i] in duplicates:
                    res = max(len(current_substring), res)
                    duplicates.remove(current_substring[0]) 
                    current_substring = current_substring[1:]
                duplicates.add(s[i])
                current_substring = current_substring + s[i]
        
                
                
                
        return max(len(current_substring), res)
                
                
            
        
        


                 
                
            
            