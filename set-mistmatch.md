# [Problem](https://leetcode.com/problems/set-mismatch/description)

# Intuition
The "Set Mismatch" problem asks us to find two integers in an array: one that appears twice and one that is missing from the set ${1, 2, ..., n}$, where $n$ is the array's length.

# Approach
1. Identifying the Duplicate: We iterate through the `nums` array, using a seen set to track the numbers we've encountered. When a number is seen for the first time, it's added to the sum `s1`. If a number is repeated, it does not contribute to `s1` again. By the end of the loop, `s1` contains the sum of unique numbers from the array.

2. Finding the Missing Number: The missing number is found by calculating the sum of the first $n$ natural numbers (using the formula $n⋅(n+1)÷2) and subtracting `s1` from it. The difference gives the missing number.

Combining these two steps allows us to find both the duplicate number and the missing number.

The duplicate is found by subtracting `s1` (sum of unique numbers) from `s2` (sum of all numbers in the array). The missing number is the difference between the sum of the first `n` natural numbers and `s1`.


# Complexities
- Time Complexity: $O(n)$, where $n$ is the length of `nums` array.
- Space Complexity: $O(n)$, space is constant except for the `seen` array.

# Code
My solution beats 100.00% of users with Python3.

```python
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s1, s2 = 0, 0
        seen = set()
        for num in nums:
            if num not in seen:
                s1 += num
            seen.add(num)
            s2 += num
        return [s2 - s1, n*(n+1)//2 - s1]
```