class Solution:
    def numIdenticalPairs(self, x: List[int]) -> int:
        c=0
        for i in range(len(x)-1):
            for j in range(i+1,len(x)):
                if x[i]==x[j]:
                    c+=1
        return c