class Solution:
    def missingNumber(self, x: List[int]) -> int:
        x.sort()
        for i in range(len(x)+1):
            if i not in x:
                return i