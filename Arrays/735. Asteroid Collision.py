class Solution:
    def asteroidCollision(self, x: List[int]) -> List[int]:
        y = []
        for a in x:
            while y and y[-1] > 0 and a < 0:
                if y[-1] + a < 0: y.pop()
                elif y[-1] + a > 0: break    
                else: y.pop(); break
            else: y.append(a)        
        return y