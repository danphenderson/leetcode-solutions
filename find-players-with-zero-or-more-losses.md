# [Problem](https://leetcode.com/problems/find-players-with-zero-or-one-losses/)

# Intuition
In this problem, we are given a list of matches where each match is represented by a pair of integers [winner, loser]. Our task is to find all the players who have never lost a match (zero losses) and those who have lost exactly one match. The key intuition here is to efficiently track each player's losses.

# Approach
The strategy involves using a dictionary to count the losses for each player. We iterate over the list of matches, updating the loss count for each loser while ensuring winners are also tracked in the dictionary with zero losses if they haven't lost yet. After processing all matches, we categorize the players into two lists based on their loss counts: one for players with zero losses and another for those with one loss. Finally, we sort these lists to meet the problem's output requirements.

# Complexities
- Time Complexity: $O(N log N)$, where N is the total number of players. The main time complexity comes from sorting the list of players. While iterating over the matches only takes $O(M)$ time, where M is the number of matches, sorting the players, especially when their count is large, becomes the dominant factor.
- Space Complexity: $O(N)$, as we use additional space for the dictionary and the lists to store players with zero and one loss. The space used is proportional to the number of players.

# Code

```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}

        # Count losses for each player
        for winner, loser in matches:
            loss_count[winner] = loss_count.get(winner, 0)
            loss_count[loser] = loss_count.get(loser, 0) + 1

        no_loss = []
        one_loss = []

        # Categorize players based on their loss count
        for player, losses in loss_count.items():
            if losses == 0:
                no_loss.append(player)
            elif losses == 1:
                one_loss.append(player)

        # Sort the lists
        return [sorted(no_loss), sorted(one_loss)]
```