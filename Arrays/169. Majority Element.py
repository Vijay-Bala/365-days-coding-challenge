class Solution:
    def majorityElement(self, x: List[int]) -> int:
        for i in set(x):
            if x.count(i)>len(x)/2:
                return i