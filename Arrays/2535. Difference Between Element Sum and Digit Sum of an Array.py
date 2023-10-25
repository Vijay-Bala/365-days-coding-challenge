class Solution:
    def differenceOfSum(self, a: List[int]) -> int:
        x=sum(a)
        y=[]
        for i in a:
            s=0
            while i!=0:
                s+=i%10
                i//=10
            y.append(s)
        z=sum(y)
        return x-z if x>z else z-x