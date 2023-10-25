class Solution:
    def rotate(self, x: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x.reverse()
        for i in range(k%len(x)):
            x.append(x[0])
            x.remove(x[0])
        x.reverse()