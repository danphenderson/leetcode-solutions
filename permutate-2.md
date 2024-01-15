# [Problem](https://leetcode.com/problems/permutations-ii/description/)

# Approach

The key to solving this problem is to use a backtracking algorithm. Backtracking is a recursive, depth-first search approach for enumerating all possible configurations of a problem space. It's particularly effective for problems like generating permutations.

The primary challenge in this problem is to handle duplicates in the input list to ensure that the generated permutations are unique. This is achieved by:

Sorting the Input Array: Sorting brings duplicates together, making it easier to skip over them in the subsequent steps.

Backtracking with a Set: A set (seen) is used in each recursive call to keep track of elements already considered at that level of recursion. This prevents generating permutations with duplicate elements in the same position.

Swap and Recurse: We swap elements to fix them at the start index and then recurse. Post recursion, we backtrack by swapping the elements back.


# Complexities
- Time Complexity: The time complexity is $O(N×N!)$, where $N$ is the number of elements in the input list. The $N!$ term accounts for the number of permutations, and the additional N factor comes from the fact that for each permutation, a deep copy of the current state (which takes $O(N)$ time) is made when it's added to the result list.

- Space Complexity: The space complexity is $O(N)$, which is needed for the recursion stack. The depth of the recursion tree can go up to N in the worst case. Note that this does not include the space needed to store the output, which is variable depending on the number of unique permutations.

# Code
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            if start == len(nums):
                result.append(nums[:])
                return
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen: continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        nums.sort()  # Sort the array to handle duplicates
        backtrack()
        return result
```
This code uses a classic backtracking approach, optimized for handling duplicates, and efficiently generates all unique permutations of the input list.


