from PIL import Image
import numpy as np
import cv2

# How much padding
free_space = 200

# Size of the whole image
size_1 = 1200
size_2 = 1000

# Number of squares in each axis
n_squares_1 = 10
n_squares_2 = 8

array = [True, False, True, False, True, False, True, False, True, False]

img = Image.new("RGB", (size_2,size_1), "white") # create a new (size_2,size_1) image
pixels = img.load() # create the pixel map

# First the program creates the whole matrix with one color, for example pink for the padding
for j in range(size_1):
	for i in range(size_2):
		pixels[i,j] = (255,0,255)

# Then it creates a square between the free_space of the padding / 2 and size_1 - free_space of the padding / 2 in axis = 0
# Then it creates a square between the free_space of the padding / 2 and size_2 - free_space of the padding / 2 in axis = 1
for j in range(free_space/2, (size_1-free_space/2)):
	for i in range(free_space/2, (size_2-free_space/2)):
        # Then it switches between 2 colors, right now black and white 
		if(array[int(i/((size_2-free_space)/n_squares_2))]):
			if(array[int(j/((size_1-free_space)/n_squares_1))-1]):
				pixels[i,j] = (255,255,255)
			else:
				pixels[i,j] = (0,0,0)
		else:
			if(array[int(j/((size_1-free_space)/n_squares_1))-1]):
				pixels[i,j] = (0,0,0)
			else:
				pixels[i,j] = (255,255,255)

cv2.imwrite('bw_chessboard.png', pix)
cv2.waitKey()
