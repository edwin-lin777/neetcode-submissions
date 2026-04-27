class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        for i in range(amount + 1):
            if i == 0:
                dp[i] = 0
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i - c ] + 1, dp[i])

        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
    