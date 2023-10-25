class Solution:
    def arrayStringsAreEqual(self, x: List[str], y: List[str]) -> bool:
        a=""
        b=""
        for i in x: a+=i
        for i in y: b+=i
        return a==b