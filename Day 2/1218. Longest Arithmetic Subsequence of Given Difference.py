class Solution:
    def longestSubsequence(self, x: List[int], y: int) -> int:
        z={}
        c=1
        for i in x:
            if i-y in z: z[i]=z[i-y]+1
            else: z[i]=1
            c=max(c,z[i])
        return c
