class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:      
        """
        cars = [] 
        for i in range(len(position)): 
            cars.append((position[i], speed[i]))
        cars.sort()
        stack = [cars[-1]]
        time = (target - stack[-1][0]) / stack[-1][1]
        for j in range(len(cars) -2 , -1,  -1):
            stack.append(cars[j])
            if ((target - stack[-1][0]) / stack[-1][1]) <= time: 
                stack.pop()
            else: 
                time = ((target -stack[-1][0])/ stack[-1][1])
        return len(stack)
        """ #alt approach: 
        cars = [] 
        for i in range(len(position)): 
            cars.append((position[i], speed[i]))
        cars.sort()
        stack = []
        for p,s in cars[::-1]:
            stack.append((target - p) /s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)



