class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=""
        for i in range(len(s)):
            x+=s[indices.index(i)]
            print(indices.index(i),s[indices.index(i)])
        return x