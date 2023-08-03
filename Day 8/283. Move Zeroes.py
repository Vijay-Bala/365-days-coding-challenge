class Solution:
    def moveZeroes(self, x: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(x.count(0)): x.remove(0);x.append(0)
