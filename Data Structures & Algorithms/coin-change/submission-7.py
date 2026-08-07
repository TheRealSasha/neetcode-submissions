class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for amt in range(1, amount + 1):
            try:
                dp[amt] = min(1 + dp[amt - c] for c in coins if amt - c >= 0)
            except ValueError:
                dp[amt] = amount + 1
                pass
        
        print(dp)

        return dp[amount] if dp[amount] < amount + 1 else -1

        