

## 1. Aim

To implement Passive Reinforcement Learning using Python to represent a fixed policy, simulate multiple episodes, and estimate the utility of each state by averaging discounted returns.

## 2. Theory

Passive Reinforcement Learning (Passive RL) is a type of reinforcement learning in which an agent follows a predefined policy and learns the utility of each state by observing rewards received during its interactions with the environment.

In this problem, a robot moves through a 4 × 4 grid to reach a goal. It follows a fixed policy: move right until reaching the last column, then move down until reaching the goal.

The environment is deterministic, meaning that an action always produces the same next state.

The robot receives a reward of -1 for every normal move and +10 for reaching the goal. It simulates multiple episodes and estimates state utilities by averaging discounted returns.

### Important Concepts

- **State:** The current position of the robot.
- **Action:** A movement, such as right or down.
- **Policy:** A predefined rule that selects an action in each state.
- **Reward:** Immediate feedback received after an action.
- **Episode:** A complete journey from the start to the goal.
- **Utility:** The expected discounted return from a state.
- **Discount Factor:** A value between 0 and 1 that determines the importance of future rewards.

## 3. Environment Description

- Grid size: 4 × 4
- Starting state: (0, 0)
- Goal state: (3, 3)
- Fixed policy: Right, then Down
- Normal move reward: -1
- Goal reward: +10
- Discount factor: 0.9
- Number of episodes: 100
- Environment: Deterministic

## 4. Fixed Policy

The robot follows these rules:

1. If the robot is not in the last column, move right.
2. If the robot reaches the last column but has not reached the goal, move down.
3. Stop when the goal is reached.

---

## 5. Algorithm

1. Start the program.
2. Initialize the grid, starting state, and goal state.
3. Set the discount factor and number of episodes.
4. Define the fixed policy.
5. Initialize utility sums and visit counts.
6. For each episode:
   - Place the robot at the starting state.
   - Follow the fixed policy until reaching the goal.
   - Record the visited states and rewards.
   - Calculate discounted returns in reverse order.
   - Add returns to the corresponding utility sums.
   - Update the visit counts.
7. Calculate average utility for every visited state.
8. Display the estimated state utilities.
9. Stop the program.
---

## 6. Expected Output

```text
Estimated State Utilities:
State (0, 0): Utility = 3.10
State (0, 1): Utility = 4.56
State (0, 2): Utility = 6.18
State (0, 3): Utility = 7.98
State (1, 0): Not Visited
State (1, 1): Not Visited
State (1, 2): Not Visited
State (1, 3): Utility = 9.98
State (2, 0): Not Visited
State (2, 1): Not Visited
State (2, 2): Not Visited
State (2, 3): Utility = 10.90
State (3, 0): Not Visited
State (3, 1): Not Visited
State (3, 2): Not Visited
State (3, 3): Terminal State
```

## 7. Conclusion

Passive Reinforcement Learning was implemented using Python. A robot followed a fixed policy in a deterministic grid environment, completed multiple episodes, and estimated state utilities using average discounted returns. This experiment demonstrates how an agent evaluates a predefined policy without changing its actions.
