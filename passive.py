import numpy as np

# Grid environment
ROWS = 4
COLS = 4

START = (0, 0)
GOAL = (3, 3)

# Parameters
GAMMA = 0.9
EPISODES = 100

# Rewards
MOVE_REWARD = -1
GOAL_REWARD = 10


# Step 1: Represent the fixed policy
def policy(state):
    row, col = state

    if col < COLS - 1:
        return "RIGHT"
    elif row < ROWS - 1:
        return "DOWN"
    else:
        return "GOAL"


# Step 2: Define the environment transition
def move(state, action):
    row, col = state

    if action == "RIGHT":
        next_state = (row, col + 1)
    elif action == "DOWN":
        next_state = (row + 1, col)
    else:
        next_state = state

    return next_state


# Step 3: Simulate one episode
def simulate_episode():
    state = START
    episode = []

    while state != GOAL:
        action = policy(state)
        next_state = move(state, action)

        # Reward for reaching the goal
        if next_state == GOAL:
            reward = GOAL_REWARD
        else:
            reward = MOVE_REWARD

        episode.append((state, reward))
        state = next_state

    return episode


# Step 4: Estimate utilities using discounted returns
utility_sum = {}
visit_count = {}

for _ in range(EPISODES):
    episode = simulate_episode()

    G = 0

    # Calculate return backward from the end
    for state, reward in reversed(episode):
        G = reward + GAMMA * G

        utility_sum[state] = utility_sum.get(state, 0) + G
        visit_count[state] = visit_count.get(state, 0) + 1

# Step 5: Calculate average utility of each state
print("Estimated State Utilities:")

for row in range(ROWS):
    for col in range(COLS):
        state = (row, col)

        if state == GOAL:
            utility = 0.0
        elif state in visit_count:
            utility = utility_sum[state] / visit_count[state]
        else:
            utility = 0.0

        print(f"State {state}: Utility = {utility:.2f}")