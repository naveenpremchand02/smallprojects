import pygame , random , sys

vr=20
hr=20
size = 400,400
rows = size[1]/hr
columns = size[0]/vr
red = 255,0,0
white = 255, 255,255

array = [[0 for i in range(columns)] for j in range(rows)]
neighbour_array = [[0 for i in range(columns)] for j in range(rows)]

class Initial_Window(object):
	
	def __init__(self, size, color ):
		self.size = size  	
		self.color = color	
		self.s = 0		
		
	def rand(self, i, j):
		return j*random.choice(range(i))
 

	def initial_surface(self):
		self.s = pygame.display.set_mode(self.size)
		pygame.display.update()
		return self.s
# create a random pattern first
		
	def initial_pattern(self):
		self.s = self.initial_surface()	
		pygame.display.set_caption("Conway's Game of Life")
		self.s.fill(white)
		pygame.display.update()
		for i in range(60):
			pygame.draw.rect(self.s, self.color,
 			(self.rand(rows, hr), self.rand(columns, vr), vr, hr))
			pygame.display.update()
			pygame.time.delay(2)
		return self.s	
	

class Changing_Window(Initial_Window):
	def __init__(self, rows, columns):
		self.size = size
		self.color = red
		self.rows = rows	
		self.columns = columns	
		self.array = array	
		self.neighbour_array = neighbour_array  
		self.s = super(Changing_Window, self).initial_pattern()
		
 	def get_rect(self, vr, hr):
		self.s.unlock()	
		for i in range(self.rows):	
			for j in range(self.columns):
				if self.s.get_at((j*vr, i*hr)) == (255, 0, 0, 255):
					self.array[i][j] = 1 
		return self.array
	
	def try_it(self, r, c, k, l, num):
		try:
			if self.array[r+k][c+l] == 1:
			    	num += 1
     	   		if self.array[r-k][l-c] == 1:
           			num +=1
     		except IndexError:
      			pass
		return num


  	def num_neighbours(self, r, c):
		num = 0
     		for k in range(2):	
     			for l in range(2):
      				if (r, c) != (k+r, l+c) or (r, c) != (r-k, l-c):	
					num = self.try_it(r, c, k, l, num)
		return num

 	def neighbour_array_make(self):
		for i in range(self.rows):
       			for j in range(self.columns):
           			self.neighbour_array[i][j] = self.num_neighbours(i,j)
    		return  self.neighbour_array 
#the condition of conway's game

	def check_live_or_dead(self, i, j):
		if self.array[i][j] == 1:
      			if self.neighbour_array[i][j] < 2 or self.neighbour_array[i][j] >3 :
              			self.array[i][j]=0
          		else:
              			self.array[i][j]=1
   		elif self.array[i][j] == 0 and self.neighbour_array[i][j]==3:
           		self.array[i][j]=1
       		else:
        		return
		return 0

  	def compute_nextgen(self):
		for i in range(self.rows):
        		for j in range(self.columns):
            			self.check_live_or_dead(i, j)
      		return self.array

 	def changing_pattern_make(self):
		self.s.fill(white)
		pygame.display.update()
		for i in range(self.rows):
       			for j in range(self.columns):
                		if self.array[i][j] == 1:
             				w=pygame.draw.rect(self.s, red, (j*vr, i*hr, vr, hr))
					pygame.display.flip()
		pygame.display.flip()
		pygame.time.delay(50)
       		return 0	
	

	def quit_or_not(self):
		for event in pygame.event.get():
        		if event.type == pygame.QUIT: sys.exit()
      		return 0

w = Initial_Window(size, red)		
c = Changing_Window(rows, columns)

while 1:	
	c.quit_or_not()					
	c.get_rect(vr, hr)		
	c.neighbour_array_make()	
	c.compute_nextgen()		   
	c.changing_pattern_make()	
	pygame.display.update()		
	pass

