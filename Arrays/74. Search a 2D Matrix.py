class Solution:
    def searchMatrix(self, x: List[List[int]], a: int) -> bool:
        for i in x:
            if a in i: return True
        return False