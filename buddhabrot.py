from PIL import Image
from tqdm import tqdm
import os
import colorsys
import math
import time
import numpy as np

def non_mandel_points(base_num_points, max_iter):

    non_mandel = np.zeros(base_num_points, dtype=np.complex128)
    points_found = 0

    random_numbers = (np.random.random(base_num_points)* 4 - 2 + (np.random.random(base_num_points)* 4 - 2) * 1j)

    print("Total number of points found : {0}".format(len(random_numbers)))
    
    p = (((random_numbers.real-0.25)**2) + (random_numbers.imag**2))**.5
    random_numbers = random_numbers[random_numbers.real > p- (2*p**2) + 0.25]

    print("After deleting points in the main cardioid : {0}".format(len(random_numbers)))

    random_numbers = random_numbers[((random_numbers.real+1)**2) + (random_numbers.imag**2) > 0.0625]

    print("After deleting points of the period-2 bulb : {0}".format(len(random_numbers)))

    z = np.copy(random_numbers)

    for i in range(max_iter):

        z = z ** 2 + random_numbers

        mask = abs(z) < 2
        # Get the points that are for sure not part of the Mandelbrot set
        new_non_mandel = random_numbers[mask == False]
        found_in_iter = len(new_non_mandel)
        non_mandel[points_found:points_found+found_in_iter] = new_non_mandel
        points_found += found_in_iter


        #Delete these points from the data
        random_numbers = random_numbers[mask]
        z = z[mask]

        #print("Deleted {0} numbers in iteration {1}".format(found_in_iter, i))
        
    print(points_found)
    return(non_mandel[:points_found])




if __name__ == "__main__":

    non_mandel_points(500000, 10000)