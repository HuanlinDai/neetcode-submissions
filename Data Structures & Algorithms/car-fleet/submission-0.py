class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted([(position[i],speed[i]) for i in range(len(position))], reverse = True)

        stack = [(target-cars[0][0])/cars[0][1]]
        for p, s in cars[1:]:
            timer = (target-p)/s
            if timer > stack[-1]:
                stack.append(timer)
            
        return len(stack)