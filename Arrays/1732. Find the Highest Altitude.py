class Solution:
    def largestAltitude(self, x: List[int]) -> int:
        x=[0]+x
        # print([x[i-1]+x[i] for i in range(1,len(x))])
        for i in range(1,len(x)): x[i]+=x[i-1]
        return max(x)