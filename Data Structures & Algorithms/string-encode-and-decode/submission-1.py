class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += (str(len(s)) + "#" + s)
        return res 

    def decode(self, s: str) -> List[str]:
        """ attempt before watching solution
        res = [] 
        for i in range(len(s)): 
            if s[i] == "#":
                before = s.split(s[i])[0]
                length = int("".join([char for char in before if char.isdigit()]))
                sub = ""
                for j in range(1, length + 1):
                    sub += s[i + j]
                res.append(sub)
            
        return res 
        """
        res = [] 
        i = 0 
        while (i < len(s)):
            j = i 
            while s[j] != "#": 
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j + 1 + length])
            i = j + 1 + length 
        return res 

            
