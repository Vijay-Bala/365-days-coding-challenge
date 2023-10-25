class Solution:
    def twoSum(self, y: List[int], a: int) -> List[int]:
        x=sorted(y)
        i=0
        j=len(x)-1
        while i<j:
            s=x[i]+x[j]
            if s>a: j-=1
            if s<a: i+=1
            if s==a: return [y.index(x[i]),len(y)-y[::-1].index(x[j])-1]