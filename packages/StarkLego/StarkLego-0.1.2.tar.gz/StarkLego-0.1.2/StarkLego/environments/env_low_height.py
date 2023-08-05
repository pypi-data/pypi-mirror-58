import gym
from gym import spaces as _spaces
import numpy as _np
from ..lego_builders.builder import TwoXTwoBlock as _TwoXTwoBlock
from ..lego_builders.builder import LegoWorld as _LegoWorld

from ldraw.pieces import Group, Piece

class LegoEnv(gym.Env):
	def __init__(self, x, y, z, noLegoPieces):
		super(LegoEnv, self).__init__()

		self.action_space = _spaces.Box(low=_np.array([0, 0]), high=_np.array([x,z], dtype=_np.int8))
		self.observation_space = _spaces.Box(
            low=0, high=1, shape=(x, y, z), dtype=_np.int8)
		
		self.current_step = 0
		self.reward = noLegoPieces
		self.world = _LegoWorld(x, y, z)
		self.noLegoPieces = noLegoPieces
		self.consecutiveWrongChoices = 0
		self.steps_taken = 0

	def _take_action(self, action):
		
		action_x = action[0]
		action_z = action[1]
		print("Taking action: " + action_x.__repr__() + action_z.__repr__())
		
		legoBlock = _TwoXTwoBlock()
	
		self.world.addPartToWorld(legoBlock, action_x, action_z)
		return self.world.yGlobalMax
		

	def _next_observation(self):
		self.current_step += 1
		return self.world.content

	def step(self, action):
		done=False
		reward = 0
		try:
			reward = self.world.maxLegoDimensions.y - self._take_action(action)
		except:
			reward = -10000

		self.steps_taken += 1
		
		if self.steps_taken >= self.noLegoPieces:
			done = True
		obs = self._next_observation()
		return obs, reward, done, {}

	def reset(self):
		self.reward = 0
		self.world.reset()
		self.current_step = 0
		self.steps_taken = 0
		#print(self.world.ldrContent)

		return self.world.content

	def render(self, mode='human', close=False):
		# Render the environment to the screen
		print(self.world.ldrContent)
		
