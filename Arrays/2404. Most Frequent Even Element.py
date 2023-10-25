class Solution:
    def mostFrequentEven(self, x: List[int]) -> int:
        c=1
        a=-1
        for i in sorted(set(x))[::-1]:
            if x.count(i)>=c and i%2==0:
                c=x.count(i)
                a=i
        return a