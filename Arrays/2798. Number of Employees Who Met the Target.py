class Solution:
    def numberOfEmployeesWhoMetTarget(self, x: List[int], y: int) -> int:
        x=sorted(x)[::-1]
        i=0
        while i<len(x) and x[i]>=y: i+=1
        return i