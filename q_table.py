from stable_baselines3.common.env_checker import check_env
from custom_env import gridEnv
import time
import numpy as np

# check_env(env)
env = gridEnv()

STATES = env.STATES
# STATES = 64
ACTIONS = env.action_space.n

print(STATES , ACTIONS)

Q = np.zeros((STATES, ACTIONS))

EPISODES = 20000 
MAX_STEPS = 400  

LEARNING_RATE = 0.81 

GAMMA = 0.50

epsilon = 0.9

rewards = []

for episode in range(EPISODES):

    print(f' EPISODE NO : {episode}')
    state = env.reset()

    for _ in range(MAX_STEPS):
        # env.render()

        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  

        else:
            action = np.argmax(Q[state, :])

        next_state, reward, done, _ = env.step(action)

        Q[state, action] = Q[state, action] + LEARNING_RATE * (reward + GAMMA * np.max(Q[next_state, :]) - Q[state, action])

        state = next_state

        if done: 
            rewards.append(reward)
            epsilon -= 0.0001
            break  # reached goal


print(f"Average reward: {sum(rewards)/len(rewards)}:")

print(Q)

# ◀️ LEFT = 0
# 🔽 DOWN = 1
# ▶️ RIGHT = 2
# 🔼 UP = 3

# # Saving the 2D array in a text file
# np.savetxt("custom_env\\file2.txt", Q)

# # Displaying the contents of the text file
# content = np.loadtxt('file2.txt')
# print("\nContent in file2.txt:\n", content)


time.sleep(2)
episodes = 5
for episode in range(episodes):
    done = False 
    obs = env.reset()
    time.sleep(0.5)


    while not done:
        env.render()
        action =  np.argmax(Q[obs])
        obs , reward , done , info = env.step(action)
        time.sleep(0.5)

        # print(f"REWARD : {reward}")


