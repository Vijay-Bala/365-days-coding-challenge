class Solution:
    def alternatingSubarray(self, x: List[int]) -> int:
        m = -1
        for i in range(len(x) - 1):
            if x[i + 1] - x[i] == 1:
                t = 2
                for j in range(i + 2, len(x)):
                    if j < len(x) and x[j] == x[j - 2]:
                        t += 1
                    else:
                        break
                m = max(m, t)
        return m if m != 0 else -1