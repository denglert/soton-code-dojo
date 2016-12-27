# - Snowflake class
class Flake():

    # - Constructor
	def __init__(self, (x, y), size):
		self.x = x
		self.y = y
		self.size = size
		self.colour = (255, 255, 255)
		self.thickness = 1
		self.speed = 2+random.random()
		self.wind = wind

    # - Display
	def display(self):
		pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
#		pygame.draw.rect (screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    # - Translation
	def move(self):
		self.angle = 3/2*math.pi + self.wind*math.pi/4
		self.x += math.sin(self.angle) * self.speed
		self.y -= math.cos(self.angle) * self.speed
    


# - Change wind speed
def change_wind():
	if random.randint(0,100) == 0:
		wind = random.random()*2-1
		for flake in my_flakes:
			flake.wind = wind
