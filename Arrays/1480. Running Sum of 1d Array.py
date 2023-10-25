class Solution:
    def runningSum(self, x: List[int]) -> List[int]:
        for i in range(1,len(x)):
            x[i]+=x[i-1]
        return x