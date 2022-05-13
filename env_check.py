from stable_baselines3.common.env_checker import check_env
from custom_env import gridEnv
import time

env = gridEnv()
# check_env(env)
episodes = 1

for episode in range(episodes):
    done = False 
    obs = env.reset()
    print(obs)
    while not done:

        action = env.action_space.sample()
        obs , reward , done , info = env.step(action)
        
        print(f"REWARD : {reward}")