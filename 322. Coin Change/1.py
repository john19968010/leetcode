class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        if amount == 0:
            return 0

        if coins[0] > amount:
            return -1

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        fir_num = coins[0]
        dp[fir_num] = 1

        for i in range(fir_num, amount + 1):
            min_val = dp[i]
            for coin in coins:
                if (i - coin) >= 0 and dp[i - coin] != float("inf"):
                    min_val = min(min_val, dp[i - coin] + 1)
            dp[i] = min_val

        return dp[amount] if dp[amount] != float("inf") else -1


# print(coin_change([474, 83, 404, 3], 264))
