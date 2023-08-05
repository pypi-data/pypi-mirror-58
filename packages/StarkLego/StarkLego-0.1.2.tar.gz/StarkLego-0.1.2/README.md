# StarkLego

## Introduction
You can use this python library to access different environments to interact with your RL agents.
Written in Python 3.

## Gym.Spaces Environments
These environments cater to the agents available in the `stable_baselines` RL library. These environments were an important part of the pilot of the project. 
### How to run
If you wish to run one of these environments, please feel free using the code below:

```python
from StarkLego.environments.env_low_height import LegoEnv
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
import numpy as np


env = DummyVecEnv([lambda: LegoEnv(6, 14, 6, 12)])

model = PPO2(MlpPolicy, env, verbose=1)
obs = env.reset()
model.set_env(env)
model.learn(total_timesteps=75000)
obs = env.reset()

print("Done training")

for i in range(4):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()

```
### List of Supported Environments
### env_low_height
The goal is to minimize the height of the Lego build. 

| Space | Data Type |
|----|:----|
| action_space | spaces.Box |
| observation_space | spaces.Box |


The only specifications than can be made are the dimensions of the LEGO World, and the number of pieces per build iteration.
#### Constructor:`LegoEnv(maximum_dimension_x, maximum_dimension_y, maximum_dimension_z, number_of_lego_pieces)`

This environment does not allow any customization for which
lego pieces can be used. 
#### Lego Pieces Supported:
- 2X2 Brick

