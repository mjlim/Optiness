#!/usr/bin/env python2

"""
A Simple Maze Game written in Python
Chris Merck

Object: To reach the right-hand side of the screen.
"""

import pygame
import random

xmax = 100
ymax = 80

wall_color = (180,85,20)
floor_color = (0,0,0)
player_color = (200,200,200)

# tile types:
floor = 0
wall = 1


class Maze:
	def __init__(self,seed):
		# God does not play dice
		random.seed(seed)

		# all wall tiles at first
		self.world = [[wall for i in xrange(ymax)] for j in xrange(xmax)]

		# generating the surface as we go along too
		self.surf = pygame.Surface((xmax,ymax))
		self.surf.fill(wall_color)

		# start on left side in the middle
		x = 1
		y = ymax/2

		# create our Player
		self.player = Player(self,x,y)

		# place the floor tile, thereby demolishing the walls
		# do the same thing in the visual map
		self.world[x][y]=floor
		self.surf.set_at((x,y), floor_color)

		# wander around until we hit the right side,
        #  but leaving a border of wall around the outside
		tick = 0
		while True:
			step = random.randint(0,1)*2 - 1

			if random.randint(0,1) == 1:
				x+=step
			else:
				y+=step

			# avoid crossing boundaries, except...
			if x == 0: x=1
			# we don't check for x out of the right side yet...
			if y == 0: y=1
			elif y == ymax-1: y=ymax-2

			self.world[x][y] = floor
			self.surf.set_at((x,y), floor_color)

			tick += 1

			# if we hit the right edge, we're done!
			if x==xmax-1: return

	def Draw(self):
		ret = self.surf.copy()
		self.player.Draw(ret)
		return ret


class Player:
	def __init__(self,maze,xpos,ypos):
		self.maze = maze
		self.xstart = xpos
		self.ystart = ypos
		self.ResetHistory()

	def Draw(self,surf):
		for pos in self.hist:
			surf.set_at(pos, player_color)
		surf.set_at((self.xpos, self.ypos), (255,255,255))

	def Move(self,xvel,yvel):
		nx = self.xpos + xvel
		ny = self.ypos + yvel

		if self.maze.world[nx][ny] == wall: return False

		# if we didn't run into a wall, that's our new position
		self.xpos = nx
		self.ypos = ny
		self.hist.append((self.xpos,self.ypos))
		return True

	def ResetHistory(self):
		self.xpos = self.xstart
		self.ypos = self.ystart
		self.hist = []

