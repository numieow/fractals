import colorsys

def calc_distance(c, max_iter):
    z = complex(0, 0)

    for iteration in range(max_iter + 1):
        z = (z*z) + c

        if abs(z) > 2:
            break
            pass
        pass
    
    return (iteration + 1) / (max_iter + 1)

def color_scale(distance, exp, const):
    # The one who don't escape are white ? 
    color = distance ** exp
    rgb_color = colorsys.hsv_to_rgb(const + color, 1 - color, 1)
    return tuple(round(i*255) for i in rgb_color)