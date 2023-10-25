class Solution:
    def longestStrChain(self, x):
        y = {}
        for w in sorted(x, key=len):
            y[w] = max(y.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(y.values())