class Solution:
    def minOperations(self, x: List[int]) -> int:
        y={}
        for i in x: y[i]=1 if i not in y else y[i]+1
        if 1 in y.values(): return -1
        c=0
        for i in y:
            c+=y[i]//3
            if y[i]%3!=0:c+=1
        return c