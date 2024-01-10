# [Problem](https://leetcode.com/problems/climbing-stairs/description/)

# Complexity
- Time Complexity: $$O(n)$$, where $$n$$ is the number of steps to reach the top.
- Space Complexity: $$O(1)$$, constant space is used.

# Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Initialize the first two steps
        first, second = 1, 2

        # Bottom-up calculation
        for i in range(3, n + 1):
            third = first + second
            first, second = second, third

        return second
```