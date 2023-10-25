class Solution:
    def maximizeSum(self, x: List[int], k: int) -> int:
        return max(x)*k+((k-1)*k)//2