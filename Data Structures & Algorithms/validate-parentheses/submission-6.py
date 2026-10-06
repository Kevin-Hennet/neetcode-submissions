class Solution:
    def isValid(self, s: str) -> bool:
        """
        Attempt before conceptual 
        valid_pairs = {")": "(", "}": "{", "]": "["}
        stack = [] 
        for i in range(len(s)):
            stack.append(s[i])
        if len(stack) % 2 != 0: 
            return False
        if stack[i] not in valid_pairs:
            return False  
        while len(stack) > 0: 
            if  (stack[len(stack) // 2] not in valid_pairs) or (stack[(len(stack) // 2 - 1)] != valid_pairs[stack[len(stack) // 2]]):
                return False 
            del stack[(len(stack) // 2) - 1], stack[len(stack) // 2]
        return True 
        attempt 2 (fail)
        if len(s) % 2 != 0: 
            return False 
        stack = [] 
        valid_pairs = {")": "(", "}": "{", "]": "["}
        for char in s: 
            stack.insert(0, char)
        length = len(stack) // 2
        while len(stack) > length:
            if stack[0] not in valid_pairs: 
                return False 
            elif stack[len(stack) -1 ] != valid_pairs[stack[0]]:
                return False 
            else: 
                stack.remove(stack[0])
        return True
        """
        stack = []
        valid_pairs = {")": "(", "}": "{", "]": "["}
        for c in s: 
            if c in valid_pairs: 
                if stack and stack[-1] == valid_pairs[c]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)
        return len(stack) == 0







        

        



