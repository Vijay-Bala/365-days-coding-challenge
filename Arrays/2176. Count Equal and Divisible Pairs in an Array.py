class Solution:
    def countPairs(self, x: List[int], k: int) -> int:
        c=0
        for i in range(len(x)-1):
            for j in range(i+1,len(x)):
                if x[i]==x[j] and (i*j)%k==0:
                    c+=1
        return c