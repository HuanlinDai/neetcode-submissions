class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left, star = [], []
        for i in range(len(s)):
            if s[i] == ")":
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif s[i] == "(":
                left.append(i)
            else:
                star.append(i)
        
    
        while left and star:
            if left.pop() > star.pop():
                return False
            
        return not left