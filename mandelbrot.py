from PIL import Image
from tqdm import tqdm
import os
import colorsys
import math
import time
import utils as utils

# Generates Mandelbrot set
# Iterates over every coordinates 
# Stop condition is ||z_n|| > 2

HEIGHT, WIDTH = 7500, 7500
MIN_X, MAX_X = -1.7, 0.7
MIN_Y, MAX_Y = -1.25, 1.25
X_RANGE, Y_RANGE = MAX_X - MIN_X, MAX_Y - MIN_Y
MAX_STEPS = 1200

# TODO : Use linspace, actually better ?

rendu = Image.new('RGB', (WIDTH, HEIGHT), color='black')
pixels = rendu.load()

start = time.time()

for row in tqdm(range(HEIGHT)):
    for col in range(WIDTH):
        x = MIN_X + col * X_RANGE / WIDTH
        y = MAX_Y - row * Y_RANGE / HEIGHT
        c = complex(x, y)

        distance = utils.calc_distance(c, MAX_STEPS)
        pixels[col, row] = utils.color_scale(distance, 0.2, 0.3)

end = time.time()

print("Execution time : {:.2f}sec".format(end - start))

rendu.save('images/mandelbrot.png')
os.system('open images/mandelbrot.png')
