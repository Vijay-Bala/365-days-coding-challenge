class Solution:
    def maximumNumberOfStringPairs(self, x: List[str]) -> int:
        return len([i for i in x if i[::-1] in x and i!=i[::-1]])//2