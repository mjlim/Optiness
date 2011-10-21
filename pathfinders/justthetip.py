#!/usr/bin/env python2

"""
An Optiness "pathfinder" that uses iterative deepening
Darren Alton
"""

import pygame

from skeleton_solver import Brain

class JustTheTip(Brain):
	name = 'just the tip'

	def __init__(self, game, depthfactor = 10):
		self.supported_games = [ 'maze', 'snes' ]
		Brain.__init__(self, game)

	def Step(self):
		pass  # derp

LoadedBrain = JustTheTip
