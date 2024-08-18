from PIL import Image
from tqdm import tqdm
import os
import colorsys
import math

# Generates Mandelbrot set
# Iterates over every coordinates 
# Stop condition is ||z_n|| > 2

WIDTH = 1000
HEIGHT = round(WIDTH * 16/9)
X_RANGE = 4
Y_RANGE = X_RANGE * 16/9
MIN_X, MAX_X = (-X_RANGE/2, X_RANGE/2)
MIN_Y, MAX_Y = (-Y_RANGE/2, Y_RANGE/2)
MAX_STEPS = 250

rendu = Image.new('RGB', (WIDTH, HEIGHT), color='black')
pixels = rendu.load()

def color_scale(distance, exp, const):
    color = distance ** exp
    rgb_color = colorsys.hsv_to_rgb(const + color, 1 - color, 1)
    return tuple(round(i*255) for i in rgb_color)

for row in tqdm(range(HEIGHT)):
    for col in range(WIDTH):
        x = MIN_X + col * X_RANGE / WIDTH
        y = MAX_Y - row * Y_RANGE / HEIGHT
        prev_x = x
        prev_y = y

        for i in range(MAX_STEPS + 1):
            re = x**2 - y**2
            im = 2 * x * y
            x = re + prev_x
            y = im + prev_y
            if x**2 + y**2 > 4:
                break
        
        if i < MAX_STEPS:
            distance = (i + 1) / (MAX_STEPS + 1)
            pixels[col, row] = color_scale(distance, 0.2, 0.3)

rendu.save('images/mandelbrot.png')
os.system('open images/mandelbrot.png')
