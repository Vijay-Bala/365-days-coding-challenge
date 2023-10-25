class Solution:
    def removeDuplicates(self, x: List[int]) -> int:
        x[:]=sorted(list(set(x)))
        return len(x)