class Solution:
    def minOperations(self, x: List[int], k: int) -> int:
        return max([x[::-1].index(i) for i in range(1,k+1)])+1
        