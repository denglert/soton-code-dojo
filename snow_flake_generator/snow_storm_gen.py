#!/usr/bin/env python

import pygame
import random
import math

background_colour = (0,0,0)
(width, height) = (400, 300)
wind = random.random()*2-1

class Flake():
	def __init__(self, (x, y), size):
		self.x = x
		self.y = y
		self.size = size
		self.colour = (255, 255, 255)
		self.thickness = 1
		self.speed = 2+random.random()
		self.wind = wind

	def display(self):
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

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

my_flakes = []
for n in range(number_of_particles):
	x = random.randint(0,3*width)-width
	flake = Flake((x,0), 2)
	my_flakes.append(flake)

running = True

def change_wind():
	if random.randint(0,100) == 0:
		wind = random.random()*2-1
		for flake in my_flakes:
			flake.wind = wind

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
	# draw all flakes
	for i,flake in enumerate(my_flakes):
		if flake.y > height:
			del my_flakes[i]
		flake.move()
		flake.display()
	pygame.display.flip()