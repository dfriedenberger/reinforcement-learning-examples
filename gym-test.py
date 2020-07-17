import gym
import logging

logging.basicConfig(level=logging.INFO)

env = gym.make("SpaceInvaders-v0"); #CartPole-v1
observation = env.reset()
for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)
  
  logging.info(' action to step ', action , observation, reward, done, info) 


  if done:
    observation = env.reset()
env.close()