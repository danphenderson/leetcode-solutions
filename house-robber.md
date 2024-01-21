# [Problem](https://leetcode.com/problems/house-robber)

# Approach
1. Initialization: Create an array `dp` of the same length as nums. This array will store the maximum amount of money that can be robbed up to the current house.

2. Base Cases:
- `dp[0] = nums[0]` since there's only one house to rob.
- `dp[1] = max(nums[0], nums[1])` as you can only rob one of the first two houses.

3. Iterative Approach:
- For each house from the 2nd index onward, calculate `dp[i]`.
- The formula is `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.
- This means, at each house i, you decide whether to rob it or not. If you rob it, you add its value to the maximum amount robbed from all houses up to `i-2`. If you don't, you just take the maximum amount robbed up to `i-1`.

4. Result:
- The last element in the dp array represents the maximum amount that can be robbed.

# Complexities
- Time Complexity: $O(n)$, where $n$ is the number of houses. Each house is processed once.
- Space Complexity: $O(n)$ for the dp array. This can be reduced to $O(1)$ by using two variables instead of an array, as we only need values from the two previous states.

# Code
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
```