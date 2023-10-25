class Solution:
    def findKthLargest(self, x: List[int], k: int) -> int:
        return sorted(x)[::-1][k-1]