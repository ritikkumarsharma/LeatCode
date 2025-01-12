class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev2 = 0
        for i in range(1,n+1):
            ritik = prev + prev2
            prev2 = prev
            prev = ritik

        return prev