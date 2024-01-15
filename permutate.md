# [Problem](https://leetcode.com/problems/permutations)


# Approach
In solving this problem, we utilize a backtracking approach. Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, and removing those solutions that fail to satisfy the constraints of the problem at any point of time.

Here's how the approach works:

We iterate through the array and swap each element with the first element, and then call the function recursively to handle the rest of the array.
The base case of the recursion is when the start index is equal to the array length, at which point we append the current permutation of nums to result.
After the recursive call, we backtrack, i.e., we swap the elements back to their original positions. This step is crucial as it ensures that the array is restored to its original state for the next iteration.
This method effectively generates all possible permutations of the array.

Complexities
Time Complexity: O(N!), where N is the number of elements in the array. This is because generating all permutations of an array requires us to explore N options for the first element, N-1 options for the second, and so on, down to 1 option for the last element.
Space Complexity: O(N), which is used by the recursion stack. The depth of the recursion tree can go up to N in the worst case (where N is the number of elements in the array). Note that while we are also storing permutations, this space is not counted towards the complexity as it is required for the output.

# Code

My solution beats $99.24%$ of users with Python3. 

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recursively generate permutations with the next element
                backtrack(start + 1, end)
                # Backtrack to swap the elements back to their original position
                nums[start], nums[i] = nums[i], nums[start]
        result = []
        backtrack(0, len(nums))
        return result
```