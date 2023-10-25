class Solution:
    def plusOne(self, x: List[int]) -> List[int]:
        s=0
        for i in x:
            s*=10
            s+=i
        s+=1
        y=[]
        while s!=0:
            y.append(s%10)
            s//=10
        return y[::-1]