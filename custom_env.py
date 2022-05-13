from typing_extensions import Self
import gym
from gym import spaces
import pygame
import numpy as np


pygame.init()

w , h = 400 , 400 

screen = pygame.display.set_mode((w , h))


color = (255 , 0 , 0 )
goal = (0 , 255 , 0)
hole = (0 , 0 , 255)
extra = (220 , 255 , 0)


class gridEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self):
        
        self.x , self.y = 0 , 0
        self.scale = 50

        self.STATES = (w //self.scale)**2 

        self.goal_x , self.goal_y = w - self.scale , h - self.scale 
        # self.hole2_x , self.hole2_y = 200 , 100
        # self.extra_x , self.extra_y = 300 , 0 

        super(gridEnv, self).__init__()
       
        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(1 ,), dtype=np.uint8)

    def step(self, action):

        if action == 0:

            # print("left")  
            self.x -= 1
            if self.x < 0:
                self.x = 0
    
        if action == 1:
            
            # print("right")
            self.x += 1
            if self.x > w//self.scale - 1:
                self.x = 3

        if action == 2:

            # print("up")
            self.y -= 1
            if self.y < 0:
                self.y = 0
        
        if action == 3:

            # print("down")
            self.y += 1
            if self.y > w//self.scale - 1:
                self.y = 3


        if self.x*self.scale == self.goal_x and self.y*self.scale == self.goal_y:
            self.reward = 10
            self.done = True

        # if self.x*self.scale == self.hole2_x and self.y*self.scale == self.hole2_y:
        #     self.reward = -1
        #     self.done = True
            
        # if self.x*self.scale == self.extra_x and self.y*self.scale == self.extra_y:
        #     self.reward += 0.5
        #     self.done = True

        self.observation = [self.x + self.y * 4]
        self.observation = np.array(self.observation, dtype=np.uint8)


        info = {}
        return self.observation, self.reward, self.done, info
    
    def render(self): 
        
        screen.fill((0 , 0 , 0))


        pygame.draw.rect(screen , goal , (self.goal_x , self.goal_y , self.scale , self.scale))    
        # pygame.draw.rect(screen , hole , (self.hole2_x , self.hole2_y , self.scale , self.scale))    
        # pygame.draw.rect(screen , extra , (self.extra_x , self.extra_y , self.scale , self.scale))    
        pygame.draw.rect(screen , color , (self.x*self.scale , self.y*self.scale , self.scale , self.scale))    

        pygame.display.update()

    def reset(self):

        self.x , self.y = 0 , 0
        self.reward = 0
        self.done = False

        
        # screen.fill((0 , 0 , 0))


        # pygame.draw.rect(screen , goal , (self.goal_x , self.goal_y , self.scale , self.scale))    
        # # pygame.draw.rect(screen , hole , (self.hole2_x , self.hole2_y , self.scale , self.scale))    
        # # pygame.draw.rect(screen , extra , (self.extra_x , self.extra_y , self.scale , self.scale))    
        # pygame.draw.rect(screen , color , (self.x*self.scale , self.y*self.scale , self.scale , self.scale))    

        # pygame.display.update()
        self.observation = [self.x + self.y * 4]
        self.observation = np.array(self.observation, dtype=np.uint8)

        return self.observation  