class Solution:
    def containsDuplicate(self, x: List[int]) -> bool:
        return not(len(set(x))==len(x))