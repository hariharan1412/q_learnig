# from turtle import clear
import numpy as np 
import time


class play:

    def __init__(self):
        
        self.w , self.h = 500 , 500
        self.scale = 25

        self.row = self.w//self.scale
        self.col = self.h//self.scale

        self.board = [[' * ' for i in range(self.col)] for i in range(self.row)]

        self.x , self.y = 0 , 0 
        self.goal_x , self.goal_y = self.row - 1 , self.col - 1

        # self.start = self.board[0][0]

        self.action_space = 4
        self.states = self.row * self.row

        self.reward = 0
        self.done = False

    def step(self , action):

        if action == 0: #LEFT 
            self.y -= 1
            if self.y < 0:
                self.y = 0

        if action == 1: #RIGHT
            self.y += 1
            if not self.y < self.col:
                self.y = self.col -1 

        if action == 2: #UP
            self.x -= 1
            if self.x < 0:
                self.x = 0 

        if action == 3: #DOWN 
            self.x += 1 
            if not self.x < self.row:
                # self.x = self.row
                self.x = self.row - 1

        #GOAL
        if self.x == self.goal_x and self.y == self.goal_y:
            self.done = True
            self.reward += 10
            print(' [ REACHED ]')

        self.observation = [self.y + self.x * self.row]
        self.observation = np.array(self.observation, dtype=np.uint8)

        # print(self.observation)

        info = {}

        return self.observation, self.reward, self.done, info

    def render(self):

        for i in range(self.row):
            for j in range(self.col):

                if self.x == i and self.y == j:
                    self.board[i][j] = ' # '
                if self.goal_x == i and self.goal_y == j:
                    self.board[i][j] = ' $ '

                print(self.board[i][j] , end=' ')
            print()
        
        print()


        # for i in range(self.row):
        #     for j in range(self.col):

        #         if self.x == i and self.y == j:
        #             self.board[i][j] = ' # '
        #         if self.goal_x == i and self.goal_y == j:
        #             self.board[i][j] = ' $ '

        #         print(j + i * self.row , end=' ')
        #     print()

        self.board = [[' * ' for i in range(self.col)] for i in range(self.row)]

    def reset(self):

        # self.board = [[' * ' for i in range(self.col)] for i in range(self.row)]

        self.x , self.y = 0 , 0 
        self.reward = 0
        self.done = False    
        # self.goal_x , self.goal_y = self.row - 1 , self.col - 1

        # self.start = self.board[0][0]


        self.observation = [self.y + self.x * self.row]
        self.observation = np.array(self.observation, dtype=np.uint8)

        # print(self.observation)
        return self.observation

env = play()

STATES = env.states
ACTION = env.action_space

print(STATES , ACTION)

Q = np.zeros((STATES , ACTION))
print(Q)



def main():

    EPISODE = 10000
    MAX_STEP = 1000

    LEARNING_RATE = 0.81

    GAMMA = 0.91

    epsilon = 0.9

    for episodes in range(EPISODE):
        
        state = env.reset()
        print(f' Episode Number : {episodes} ')

        for _ in range(MAX_STEP):
            # env.render()

            if np.random.uniform(0 , 1) < epsilon:
                action = round(np.random.uniform(0 , 3))
            else:
                action = np.argmax(Q[state , :])

            # action = int(input(" ACTION : "))
            next_state , reward , done , _ = env.step(action)

            Q[state,action] = Q[state , action] + LEARNING_RATE * (reward + GAMMA * np.max(Q[next_state, : ]) - Q[state , action])

            state = next_state

            if done:
                epsilon -= 0.001
                break
            # time.sleep(0.4)

def run():

    time.sleep(1)
    episodes = 3

    for episode in range(episodes):
        done = False 
        obs = env.reset()
        time.sleep(0.5)


        while not done:
            env.render()
            action =  np.argmax(Q[obs])
            print(action)
            obs , reward , done , info = env.step(action)
            time.sleep(0.3)



main()
run()