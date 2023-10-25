class Solution:
    def sumOddLengthSubarrays(self, x: List[int]) -> int:
        s=0 if len(x)%2==0 else sum(x)
        for i in range(1,len(x),2):
            for j in range(0,len(x)):
                if i+j<=len(x): s+=sum(x[j:j+i])
        return s