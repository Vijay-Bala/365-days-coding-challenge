class Solution:
    def singleNonDuplicate(self, x: List[int]) -> int:
        t=list(set(x))
        t=t[::-1]
        for i in t:
            if x.count(i)==1:
                return i