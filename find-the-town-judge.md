# [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

## Intuition
When first approaching the problem, it struck me as a classic case of graph theory application, specifically in a directed graph. The key insight was realizing that the town judge, if exists, would be the only person not trusting anyone else while being trusted by everyone else. This unique combination of trust relationships made me think of representing each person as a node in a graph and each trust relationship as a directed edge.

## Approach
To solve the problem, I decided to create two arrays: `trusts` and `trusted_by`, each of length $n$, where $n$ is the number of people in the town. For each person, `trusts[i]` keeps track of how many people they trust, and `trusted_by[i]` keeps track of how many people trust them. I then iterated through the trust relationships, updating these arrays accordingly. After processing all relationships, I checked for a person with $0$ `trusts` and $n-1$ `trusted_by`, which would indicate the town judge. This method effectively maps out the trust network, allowing us to pinpoint the judge based on the problem's criteria.

## Complexity
- Time complexity: The time complexity of this solution is $O(n)$, as it involves a single pass through the trust array of length $n$ and then another pass through the arrays `trusts` and `trusted_by`.

- Space complexity: The space complexity is also $O(n)$, due to the additional arrays `trusts` and `trusted_by` used for storing trust counts.

## Code
```python
class Solution:
    
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts, trusted_by = [0] * n, [0] * n
        for rel in trust:
            ai, bi = rel[0] - 1, rel[1] - 1
            trusts[ai] += 1
            trusted_by[bi] += 1
        for i in range(n):
            if trusts[i] == 0 and trusted_by[i] == n-1:
                return i+1
        return -1

```