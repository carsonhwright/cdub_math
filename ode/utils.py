import operator
from collections import deque

import numpy as np



def plot_solution_curve(point: tuple, x:np.array, y:np.array, direction_field:np.array):
    """Given a cartesian coordinate, plot a solution curve on a vector 
    field
    
    It needs mentioning that this plots the solution based on the 
    direction field and has nothing to do with the function that 
    defines the direction field

    TODO this is only solving forward of the point, needs to solve backwards too
    """
    global SUCCESS_THRESHOLD

    delta_x = abs(x[0][0] - x[0][1])
    SUCCESS_THRESHOLD = delta_x
    delta_y = abs(y[0][0] - y[1][0])
    ret_x, ret_y = [], []
    convergence_limit = len(x)
    convergence_counter = 0
    is_decreasing = True
    # here needs a solve backwards situation
    while convergence_counter < convergence_limit:
        convergence_counter += 1

        closest_x, closest_y = get_index_closest_to_point(point, x, y, is_decreasing)
        if not closest_x and not closest_y:
            continue
        ret_x.append(point[0])
        ret_y.append(point[1])
        start_slope = direction_field[closest_y][closest_x]
        is_decreasing = start_slope < 0
        point = get_next_point(point, delta_x, delta_y, start_slope)
    return ret_x, ret_y

def get_index_closest_to_point(point, x, y, is_decreasing):
    """Returns the INDEXES of the given arrays who's values should be closest to the values in the `point` (requires well-ordered)
    This method is necessary because the given is not a function, but rather a direction field

    Params
    ------
    point: tuple - the point who's closest neighbor's index we are 
            seeking
    x, y: np.array - the 2-D arrays containing the x and y indices 
            that defined the direction field
    is_decreasing: bool - if the slope at a given position is less 
            than `0`, this is set to `True`, is used to define 
            `__lt__` and `__le__` ordering for better selection of 
            y-values
    
    Returns
    -------
    tuple - (ret_x_idx, ret_y_idx) : this is the x,y indices of the 
            direction field that correlate to the `point` param
    """
    ret_x_idx, ret_y_idx = 0, 0
    op, sis_op = comparison(is_decreasing)
    for x_idx in range(len(x[0])):
        try:
            # throw on out-of-bounds of point
            if point[0] < x[0][0] or x[0][-1] < point[0]:
                raise RuntimeError(f"Point {point} exists outside of the direction field")
            if x[0][x_idx] < point[0] and x[0][x_idx + 1] >= point[0]:
                # find x-value of point/index for slope
                left_close = abs(x[0][x_idx] - point[0])
                right_close = abs(x[0][x_idx + 1] - point[0])
                if left_close > right_close:
                    ret_x_idx = x_idx + 1
                    break
                else:
                    ret_x_idx = x_idx
                    break
        except IndexError:
            if abs(point[0] - x[0][-1]) <= SUCCESS_THRESHOLD:
                # end of plot reached
                return None, None
            breakpoint()
            raise RuntimeError(f"x-value of Point {point} could not be found on the direction field")
    
    for y_idx in range(len(y)):
        try:

            # TODO need to throw on out of bounds condition

            # operators are affected by decreasing vs. increasing function
            if sis_op(y[y_idx][0], point[1]) and op(point[1], y[y_idx + 1][0]):
                # find y-value of point/index for slope
                lower_close = abs(y[y_idx][0] - point[1])
                upper_close = abs(y[y_idx + 1][0] - point[1])
                if lower_close > upper_close:
                    ret_y_idx = y_idx + 1
                    break
                else:
                    ret_y_idx = y_idx
                    break
        except IndexError:
            if abs(point[1] - y[-1][0]) <= SUCCESS_THRESHOLD:
                # end of plot reached
                return None, None
            breakpoint()
            raise RuntimeError(f"y-value of Point {point} could not be found on the direction field")
    return ret_x_idx, ret_y_idx

def get_next_point(point, delta_x, delta_y, slope):
    """Get the next point relative to the `point` param using the given slope and delta scalars
    
    Params
    ------
    point: tuple - (x, y) cartesian coordinate
    delta_x: float - scalar by which to increment the x-coordinate
    delta_y: float - scalar by which to increment the y-coordinate
    slope: float - scalar by which to increment both the 
            x,y-coordinates
    
    Returns
    -------
    (ret_x_point, ret_y_point): tuple - new point relative to param `
            point` via slope and delta values
    """
    ret_x_point = point[0] + delta_x
    ret_y_point = point[1] + (delta_y * slope)
    return ret_x_point, ret_y_point

def comparison(is_decreasing):
    """Get operators for less than and less than or equal to, whose order is based on the bool `is_decreasing`
    
    Params
    ------
    is_decreasing: bool - function being considered elsewhere has a negative slope

    Returns
    -------
    operators: tuple - the ordering of which is not important here, 
            only that it is different and based on the value of a 
            boolean
    """
    if is_decreasing:
        return operator.__le__, operator.__lt__
    return operator.__lt__, operator.__le__