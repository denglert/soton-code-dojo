#!/usr/bin/env python

import pygame
import random
import math

# - General settings
background_colour = (0,0,0)

wind = random.random()*2-1
(width, height) = (600, 400)
def_size = 5

class Flake():
	def __init__(self, (x, y), size):
		self.x = x
		self.y = y
		self.size = size
		self.colour = (255, 255, 255)
		self.thickness = 1
		self.speed = 2+random.random()
		self.wind = wind
		self.stopped = False

	def display(self):
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size/2, self.thickness)
		pygame.draw.line(screen, self.colour, (int(self.x)-self.size, int(self.y)),(int(self.x)+self.size, int(self.y)), self.thickness)
		pygame.draw.line(screen, self.colour, (int(self.x)-self.size, int(self.y)),(int(self.x)+self.size, int(self.y)), self.thickness)
		pygame.draw.line(screen, self.colour,
			(int(self.x-self.size*math.cos(math.pi/3)), int(self.y-self.size*math.sin(math.pi/3))),
			(int(self.x+self.size*math.cos(math.pi/3)), int(self.y+self.size*math.sin(math.pi/3))), self.thickness)
		pygame.draw.line(screen, self.colour,
			(int(self.x-self.size*math.cos(2*math.pi/3)), int(self.y-self.size*math.sin(2*math.pi/3))),
			(int(self.x+self.size*math.cos(2*math.pi/3)), int(self.y+self.size*math.sin(2*math.pi/3))), self.thickness)
		# pygame.draw.rect(screen, self.colour, pygame.Rect(int(self.x)-3,int(self.y)-3,6,6))
		# pygame.draw.polygon(screen, self.colour, [(int(self.x)-3, int(self.y)),(int(self.x), int(self.y)-3),(int(self.x)+3, int(self.y)),(int(self.x), int(self.y)+3)], self.size)

	def move(self):
		self.angle = 3/2*math.pi + self.wind*math.pi/4
		self.x += math.sin(self.angle) * self.speed
		self.y -= math.cos(self.angle) * self.speed

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
pygame.display.set_caption('Snow Flakes')

number_of_particles = 50
my_particles = []

# for n in range(number_of_particles):
#	 size = random.randint(10, 20)
#	 x = random.randint(size, width-size)
#	 y = random.randint(size, height-size)

#	 particle = Particle((x, y), size)
#	 particle.speed = random.random()
#	 particle.angle = random.uniform(0, math.pi*2)

#	 my_particles.append(particle)

# - Generating snowflakes - #
my_flakes = []
for n in range(number_of_particles):
	x = random.randint(0,3*width)-width
	flake = Flake((x,0), def_size)
	my_flakes.append(flake)

running = True

### --- Main function --- ###
def change_wind():
	global wind
	if random.randint(0,100) == 0:
		wind = random.random()*2-1
		for flake in my_flakes:
			flake.wind = wind

def draw_snowman():
	pygame.draw.circle(screen, (255,255,255), (width/4, height-20), 40, 0)
	pygame.draw.circle(screen, (255,255,255), (width/4, height-75), 30, 0)
	pygame.draw.circle(screen, (255,255,255), (width/4, height-115), 20, 0)
	pygame.draw.line(screen, (100,50,0),(width/4-20, height-85),(width/4-50, height-100), 3)
	pygame.draw.line(screen, (100,50,0),(width/4+20, height-85),(width/4+50, height-100), 3)
	pygame.draw.circle(screen, (0,0,0), (width/4-10, height-120), 2, 0)
	pygame.draw.circle(screen, (0,0,0), (width/4+10, height-120), 2, 0)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(background_colour)

	# add new flakes
	if random.randint(0,1) == 0:
		my_flakes += [Flake((random.randint(0,3*width)-width,-10-random.randint(0,20)), 2) for i in range(30)]

	# change wind
	change_wind()

	# change wind
	change_wind()
	# add new flakes
	if random.randint(0,1) == 0:
		my_flakes += [Flake((random.randint(0,3*width)-width,-10-random.randint(0,20)), def_size) for i in range(5)]
	# draw all flakes
	for i,flake in enumerate(my_flakes):
		if flake.y > height:
			del my_flakes[i]

	pygame.display.flip()
			continue
		flake.move()
		flake.display()
	# draw the snowman
	draw_snowman()
	pygame.display.flip()
