import random
import math

class pixel:
    r = 0
    g = 0
    b = 0

    def __init__(self, r, g, b):
       self.r = r
       self.g = g
       self.b = b

    def setR(self, r):
       self.r = r
    def setG(self, g):
       self.g = g
    def setB(self, b):
       self.val = b
def copyMatrix(matrix, WIDTH, HEIGHT):
    copy = {}
    for x in range(HEIGHT):
        for y in range(WIDTH):
            copy[(x,y)] = copyPixel(matrix[(x,y)])
    return copy

def copyPixel(toCopy):
    copy = pixel(toCopy.r, toCopy.g, toCopy.b)
    return copy

def grayScale(matrix, image, WIDTH, HEIGHT):
    for x in range(HEIGHT):
        for y in range(WIDTH):
        	RGB = (int(matrix[(x,y)].r), int(matrix[(x,y)].g), int(matrix[(x,y)].b))
        	val = (str(int(.2*RGB[0] + .7*RGB[1] + .1*RGB[2])))
        	image[(x,y)] = ( val + " " + val + " " + val + " " )

def createMatrix(nums, image, WIDTH, HEIGHT):
	matrix = {}
	r, c = 0, 0
	for pos in range(0, len(nums), 3):
		matrix[(r,c)] = pixel(int(nums[pos+0]), int(nums[pos+1]), int(nums[pos+2]))
		c += 1
		if c%WIDTH == 0:
			c = 0
			r += 1
	return matrix

def addNine(r, c, copy):
	red, green, blue = 0, 0, 0
	for x in range(r-1, r+2):
		for y in range(c-1, c+2):
			red += copy[(x,y)].r
			green += copy[(x,y)].g
			blue += copy[(x,y)].b
	return [red, green, blue]

def blur(matrix, image, WIDTH, HEIGHT):
	# copy = copyMatrix(matrix, WIDTH, HEIGHT)
	for r in range(HEIGHT):
		for c in range(WIDTH):
			if(r != 0 and r != HEIGHT-1 and c != 0 and c != WIDTH-1):
				RGB = addNine(r, c, matrix)
				red = RGB[0] #sum([copy[(r-1,c-1)].r, copy[(r-1,c)].r, copy[(r-1,c+1)].r, copy[(r,c-1)].r, copy[(r,c)].r, copy[(r,c+1)].r, copy[(r+1,c-1)].r, copy[(r+1,c)].r, copy[(r+1,c+1)].r] ) 
				green = RGB[1] #sum([copy[(r-1,c-1)].g, copy[(r-1,c)].g, copy[(r-1,c+1)].g, copy[(r,c-1)].g, copy[(r,c)].g, copy[(r,c+1)].g, copy[(r+1,c-1)].g, copy[(r+1,c)].g, copy[(r+1,c+1)].g] ) 
				blue = RGB[2] #sum([copy[(r-1,c-1)].b, copy[(r-1,c)].b, copy[(r-1,c+1)].b, copy[(r,c-1)].b, copy[(r,c)].b, copy[(r,c+1)].b, copy[(r+1,c-1)].b, copy[(r+1,c)].b, copy[(r+1,c+1)].b] ) 
				image[(r,c)] = ( str(red/9) + " " + str(green/9) + " " + str(blue/9) + " ")
			else:
				image[(r,c)] = ( str(matrix[r,c].r) + " " + str(matrix[r,c].g) + " " + str(matrix[r,c].b) + " ") 

def gradient(matrix, r , c):
	dx = 0
	dy = 0
	for x in range(r, r+2):
		dx += abs(matrix[(x, c)].r -  matrix[(x-1, c)].r) + abs(matrix[(x, c)].g -  matrix[(x-1, c)].g) + abs(matrix[(x, c)].b -  matrix[(x-1, c)].b)
	for y in range(c, c+2):
		dy += abs(matrix[(r, y)].r -  matrix[(r, y-1)].r) + abs(matrix[(r, y)].g -  matrix[(r, y-1)].g) + abs(matrix[(r, y)].b -  matrix[(r, y-1)].b)
	return dx, dy

def edgeDetection(matrix, image, WIDTH, HEIGHT):
	gradVals = {}
	for r in range(HEIGHT):
		for c in range(WIDTH):
			if(r != 0 and r != HEIGHT-1 and c != 0 and c != WIDTH-1):
				dx, dy = gradient(matrix, r, c)
				gradVals[(r,c)] = [dx, dy]
				grad = dx + dy
				limit = 250
				if grad > limit:
					image[(r,c)] = ( str(255) + " " + str(255) + " " + str(255) + " ")
					continue
				image[(r,c)] = ( str(0) + " " + str(0) + " " + str(0) + " ")

			else:
				image[(r,c)] = ( str(matrix[r,c].r) + " " + str(matrix[r,c].g) + " " + str(matrix[r,c].b) + " ") 
	return gradVals

def edgeThinning(matirx, image, WIDTH, HEIGHT, grad):
	for r in range(HEIGHT):
		for c in range(WIDTH):
			if(r > 1 and r < HEIGHT-2 and c > 1 and c < WIDTH-2):
				dx = grad[(r,c)][0]
				dy = grad[(r,c)][1]
				theta = math.degrees(math.atan2(dy, dx))
				if 0 < theta < 90 or -180 < theta < -90:  ## line in quad 1 and 3
					quad2 = grad[(r-1,c-1)][0] + grad[(r-1,c-1)][1]
					center = dx + dy
					quad4 = grad[(r+1,c+1)][0] + grad[(r+1,c+1)][1]
					maxp = max([quad2, center, quad4])
					if maxp != center:
						image[(r,c)] = ( str(0) + " " + str(0) + " " + str(0) + " ")
						continue

				if -90 < theta < 0 or 90 < theta < 180: ## line in quad 2 and 4
					quad1 = grad[(r-1,c+1)][0] + grad[(r-1,c+1)][1]
					center = dx + dy
					quad3 = grad[(r+1,c-1)][0] + grad[(r+1,c-1)][1]
					maxp = max([quad1, center, quad3])
					if maxp != center:
						image[(r,c)] = ( str(0) + " " + str(0) + " " + str(0) + " ")
						continue
			else:
				image[(r,c)] = ( str(matrix[r,c].r) + " " + str(matrix[r,c].g) + " " + str(matrix[r,c].b) + " ") 

def blankimage(image, WIDTH, HEIGHT):
	for r in range(HEIGHT):
		for c in range(WIDTH):
			image[(r,c)] = ( str(0) + " " + str(0) + " " + str(0) + " ")

def imageNoise(image, WIDTH, HEIGHT):
	for n in range(500):
		r = random.randint(0, HEIGHT-1)
		c = random.randint(0, WIDTH-1)
		image[(r,c)] = ( str(255) + " " + str(255) + " " + str(255) + " ")

def drawLine(m, b, image, WIDTH, HEIGHT):
	for x in range(WIDTH): #used to c
		y = m*(x) + b
		# print HEIGHT-y
		image[((HEIGHT-y), x)] = ( str(255) + " " + str(255) + " " + str(255) + " ")
def drawLinePolar(r, theta, image, WIDTH, HEIGHT):
	pass



file1 = open('stubs.ppm', 'r')
stng = file1.readline()
#print(stng)
nums = file1.read().split()
file1.close()
#print(nums)

WIDTH = int(nums[0])
HEIGHT = int(nums[1])
nums = nums[3:]
#print (len(nums))
#print (WIDTH)
#print (HEIGHT)

data = []
data.append(stng) # 0
data.append(str(WIDTH) + " ") #1
data.append(str(HEIGHT) + "\n") #2
data.append("255\n") #3

###################################################   This is where we edit the pixels
image = {}
matrix = createMatrix(nums, image, WIDTH, HEIGHT)
gradVals = edgeDetection(matrix, image, WIDTH, HEIGHT)
edgeThinning(matrix, image, WIDTH, HEIGHT, gradVals)
grayScale(matrix, image, WIDTH, HEIGHT)
# blur(matrix, image, WIDTH, HEIGHT)
# blankimage(image, WIDTH, HEIGHT)
# drawLine(0, 50, image, WIDTH, HEIGHT)
# imageNoise(image, WIDTH, HEIGHT)

gray = open('grayScale.ppm', 'w')

###################################################

gray.write(str(data[0]))
gray.write(str(data[1]))
gray.write(str(data[2]))
gray.write(str(data[3]))

for r in range(HEIGHT):
	for c in range(WIDTH):
		gray.write(image[(r,c)])

gray.close()