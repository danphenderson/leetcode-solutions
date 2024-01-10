# [Problem](https://leetcode.com/problems/two-sum/description/)

# Intuition
Work it out with pen and paper, and you will find the pattern.

# Complexities
- Time Complexity: $$O(n)$$, where $$n$$ is the length of the input array.
- Space Complexity: $$O(n)$$, where $$n$$ is the length of the input array.

# Code
This solution beat 96% of other submissions' runtime.

```python
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [ind, seen[compliment]]
            seen[num] = ind
```