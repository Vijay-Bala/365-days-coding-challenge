class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        subseq = []
        for i in range(n):
            if not subseq or groups[subseq[-1]] != groups[i]:
                subseq.append(i)
        return [words[i] for i in subseq]