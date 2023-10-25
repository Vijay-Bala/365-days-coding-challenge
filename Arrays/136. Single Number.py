class Solution:
    def singleNumber(self, a: List[int]) -> int:
        return 2*sum(set(a))-sum(a)