# [Problem](https://leetcode.com/problems/search-insert-position/description/)

# Intuition
Binary search all day long.

# Complexity
- Time Complexity: $O(\log{n})$, where $n$ is the length of the input array.
- Space Complexity: $O(1)$, constant space is used. (The variables `lp`, `rp`, and `mid` are the only additional storage used)

# Code
```python
class Solution:
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Perform a binary search
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                lp = mid + 1
            else:
                rp = mid - 1

        # target is not found, but it should be inserted at lp
        return lp
```