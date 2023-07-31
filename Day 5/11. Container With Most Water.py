class Solution:
    def maxArea(self, a: List[int]) -> int:
        m=0
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                tm=min(a[i],a[j])*(j-i)
                if tm>m:
                    m=tm
        return m
