from PIL import Image
from tqdm import tqdm
import os
import colorsys
import math
import time

# Generates Mandelbrot set
# Iterates over every coordinates 
# Stop condition is ||z_n|| > 2

HEIGHT, WIDTH = 2500, 2500
MIN_X, MAX_X = -1.7, 0.7
MIN_Y, MAX_Y = -1.25, 1.25
X_RANGE, Y_RANGE = MAX_X - MIN_X, MAX_Y - MIN_Y
MAX_STEPS = 1000

# TODO : Use linspace, actually better ?

rendu = Image.new('RGB', (WIDTH, HEIGHT), color='black')
pixels = rendu.load()

def calc_distance(c, max_iter = MAX_STEPS):
    z = complex(0, 0)

    for iteration in range(max_iter + 1):
        z = (z*z) + c

        if abs(z) > 4:
            break
            pass
        pass
    
    return (iteration + 1) / (max_iter + 1)

def color_scale(distance, exp, const):
    # The one who don't escape are white ? 
    color = distance ** exp
    rgb_color = colorsys.hsv_to_rgb(const + color, 1 - color, 1)
    return tuple(round(i*255) for i in rgb_color)

start = time.time()

for row in tqdm(range(HEIGHT)):
    for col in range(WIDTH):
        x = MIN_X + col * X_RANGE / WIDTH
        y = MAX_Y - row * Y_RANGE / HEIGHT
        c = complex(x, y)
        #prev_x = x
        #prev_y = y
        #prev_c = c

        """
        for i in range(MAX_STEPS + 1):
            re = x**2 - y**2
            im = 2 * x * y
            #current = c*c
            x = re + prev_x
            y = im + prev_y

            if x**2 + y**2 > 4:
                break
        
        if i < MAX_STEPS:
            distance = (i + 1) / (MAX_STEPS + 1)"""

        distance = calc_distance(c)
        pixels[col, row] = color_scale(distance, 0.2, 0.3)

end = time.time()

print("Execution time : {:.2f}sec".format(end - start))

rendu.save('images/mandelbrot.png')
os.system('open images/mandelbrot.png')
