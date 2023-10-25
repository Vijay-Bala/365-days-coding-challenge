class Solution:
    def removeDuplicates(self, x: List[int]) -> int:
        for i in set(x):
            while x.count(i)>2: x.remove(i)
        return len(x)