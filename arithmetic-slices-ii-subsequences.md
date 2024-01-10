# [Problem](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/)

# Intuition
The key challenge here is to handle the concept of subsequences efficiently and to keep track of arithmetic sequences.
The construction of a subsequence is a natural fit for dynamic programming.

# Approach
1. Understanding the Problem: A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. In this problem, we are interested in subsequences that are at least three elements long and have a constant difference between consecutive elements.

2. Dynamic Programming Approach: We can use a 2D array dp where dp[i][d] represents the number of arithmetic subsequences ending at index i with a common difference d. However, the difference d can be quite large, so we use a hash map for the second dimension.

3. Iterating Over the Array: For each pair of elements nums[i] and nums[j] where i < j, we calculate the difference d = nums[j] - nums[i]. This d represents the potential common difference for a subsequence ending at j.

4. Updating the DP Array: If there already are some subsequences ending at i with difference d, it means we can extend those subsequences by adding nums[j]. Therefore, we add dp[i][d] to dp[j][d].

5. Counting Valid Subsequences: Since we are interested in subsequences of length at least 3, we start counting valid subsequences from the second element in our iteration.

6. Handling Edge Cases: We need to handle arrays with fewer than three elements as special cases.

The psuedocode for this approach is as follows:
```
function countArithmeticSubsequences(nums):
    if length of nums is less than 3:
        return 0

    Initialize count as 0
    Initialize dp as an array of empty hash maps

    for j from 1 to length of nums:
        for i from 0 to j-1:
            Calculate d = nums[j] - nums[i]
            Add dp[i][d] to dp[j][d]
            If dp[i][d] exists, add its value to count

    return count
```

Note, in practice we can use a single hash map for the second dimension of the dp array. We can use a hash map where the key is the common difference and the value is the number of subsequences ending at i with that difference. This is because we only need to know the number of subsequences ending at i with a particular difference, not the subsequences themselves.

# Complexities
- Time Complexity: $O(n^2k)$, where $n$ is the length of the input array and $k$ is the number of unique differences between elements in the array.
- Space Complexity: $O(n^2)$, where $n$ is the length of the input array.

# Code
This solution beat 91% of other submissions' runtime.

```python
class Solution:


    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        # Exit early check
        if n < 3:
            return count
        
        # dp[i] is a hash map where the key is the common difference
        # and the value is the number of subsequences ending at i with that difference
        dp = [{} for _ in range(n)]

        for j in range(1, n):
            for i in range(j):
                d = nums[j] - nums[i]

                # The number of subsequences ending at i with difference d
                subsequences_i = dp[i].get(d, 0)

                # The number of subsequences ending at j with difference d
                subsequences_j = dp[j].get(d, 0)

                # Update the count. We count subsequences of length >= 3, so add the subsequences ending at i
                count += subsequences_i

                # Update the number of subsequences ending at j with difference d
                dp[j][d] = subsequences_j + subsequences_i + 1

        return count
```