#!/usr/bin/env python

import pygame
import random
import math

# - General settings
background_colour = (0,0,0)
(width, height) = (400, 300)

wind = random.random()*2-1

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
	flake = Flake((x,0), 2)
	my_flakes.append(flake)

running = True

### --- Main function --- ###
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
