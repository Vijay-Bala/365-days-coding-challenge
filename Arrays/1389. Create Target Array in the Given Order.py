class Solution:
    def createTargetArray(self, x: List[int], p: List[int]) -> List[int]:
        y=[]
        for i in range(len(x)):
            y.insert(p[i],x[i])
        return y