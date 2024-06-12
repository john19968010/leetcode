## Leetcode description
https://leetcode.com/problems/sum-root-to-leaf-numbers/

### Intro
A dp(dynamic programming) question to get the minimum number of coins to make up the amounts.

DP: Avoid repeatedly getting the same value, so it creates an array to record all results.
e.g: find the smallest amount result from 23. so it created an length 24 (plus 1) array to store all result. `[0] * amount + 1`

| Normally, we use `float("inf")` to represent the largest infinite value as the initial value because no value is larger than it, and it consumes the smallest memory size (24 bits). An integer is (28 bits).

## My idea
To optimize the solution, I added a few conditions, such as checking if the amount is equal to 0, to avoid unnecessary calculations. Then, I used dynamic programming (dp) to store all the results. Finally, I iterated through the results that are less than or equal to the target amount using a for loop with the given coins.

Outcome: Correct

ode: [here](1.py)