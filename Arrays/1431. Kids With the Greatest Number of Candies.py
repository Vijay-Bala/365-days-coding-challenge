class Solution:
    def kidsWithCandies(self, a: List[int], x: int) -> List[bool]:
        return [True if i+x>=max(a) else False for i in a]