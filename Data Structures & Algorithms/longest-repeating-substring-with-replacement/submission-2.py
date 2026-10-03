class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Attempt before the conceptual 
        frequency = {}
        l = 0 
        res = 0 
        for i in range(len(s)): 
            frequency[s[i]] = 1 + frequency.get(s[i], 0)
        for r in range(1, len(s)): 
            if k != 0 and s[r] != s[l] and frequencey[s[l]] > frequency[s[r]]: 
        """
        res = 0 
        frequency = {}
        l = 0 
        window = 1

        for r in range(len(s)):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            if (window - max(frequency.values(), default=0) <= k):
                res = max(window, res)
                window += 1 
            else: 
                while (window - max(frequency.values()) > k): 
                    frequency[s[l]] -= 1 
                    window -= 1 
                    l += 1
                res = max(window, res)
                window += 1
        return res 
                


                
            
        