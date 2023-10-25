class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sn = sorted(set(nums));return min(len(nums) - (bisect_right(sn, sn[i] + len(nums) - 1) - i) for i in range(len(sn)))