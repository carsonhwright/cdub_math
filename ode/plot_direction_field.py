from math import exp, cos, sin, sqrt, atan

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

from utils import plot_solution_curve as psc

def plot_vect_field(
            f: callable,
            x_domain:tuple=(10,10),
            y_domain:tuple=(10,10), 
            slope_norm:float=0,
            density:int=20,
            title:str="Vector Field",
            coloring: str="brg",
            **kwargs):
    """plot a function's direction field
    TODO currently just shows a fig, doesn't write to file (support for that hasn't been established, i.e. something like an output folder)
    
    Params
    ------
    f: callable
        returns the function value, should take two parameters which 
        are the 2D-arrays of the X,Y values of the domain of the 
        function and gives a 2D array of their results
    
    x_domain : tuple - x domain of field
    y_domain : tuple - y domain of field
    slope_norm : float - slope value for which to normalize the 
            central bgr coloring around
    density : int - sampling density of each domain
    title : str - Title of the figure
    **kwargs : Other options that specific fields might need
            `point` is required if solution curve is desired
    """
    xmin, xmax = x_domain
    ymin, ymax = y_domain
    solution_x, solution_y = [], []
    x = np.linspace(xmin, xmax, density)
    y = np.linspace(ymin, ymax, density)
    X, Y = np.meshgrid(x, y)
    U = np.zeros_like(X)
    V = np.zeros_like(Y)
    U, V, slope, mag = get_unit_uv_slope_mag(f, X, Y, **kwargs) # (*)
    point = kwargs.get("point")
    try:
        # plot solution curve
        assert point
        solution_x, solution_y = psc(point=point, x=X, y=Y, direction_field=slope)
    except AssertionError:
         print("`point` not provided, no solution curve will be plotted")
    
    # configure figure
    plt.figure(figsize=(7, 7))
    # normalize the coloring, centered around slope norm, ideally use 
    # a coloring scheme from matplot lib that has a distinct central 
    # color
    try:
        norm = TwoSlopeNorm(
                vmin=slope.min(),
                vcenter=slope_norm,
                vmax=slope.max())
    except ValueError:
        temp = (slope.max() + slope.min()) / 2
        norm = TwoSlopeNorm(
                vmin=slope.min(),
                vcenter=temp,
                vmax=slope.max())
    
    Q = plt.quiver(
            X, Y, U, V, 
            slope, cmap=coloring, scale=density/2, norm=norm,
            headlength=0, headwidth=0, headaxislength=0, pivot='mid')
    if solution_x and solution_y:
         plt.plot(solution_x, solution_y, color='black', linewidth=2, label=f'Solution curve on ({point})')
    cbar = plt.colorbar(Q)
    cbar.set_label(f"Slope magnitude")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

def example_func(x: np.array, y: np.array):
        """The intended return value is the function's direction field
        array
        
        i.e. y' = y - x
            the above is the desired slope field we wish to represent,
            so the return value is `y - x`

        Params
        ------
        x, y: np.array - 2D - Numpy arrays of x and y values 
                respectively, based on linspace density
        
        Returns
        -------
        2D-array of function result
        """
        return ((2*x) - 4) / ((3*(y**2)) - 4)


def dumb_funck(x: np.array, y: np.array):
        """The intended return value is the function's direction field
        array
        
        i.e. y' = y - x
            the above is the desired slope field we wish to represent,
            so the return value is `y - x`

        Params
        ------
        x, y: np.array - 2D - Numpy arrays of x and y values 
                respectively, based on linspace density
        
        Returns
        -------
        2D-array of function result
        """
        return y**2

def get_unit_uv_slope_mag(func: callable, x: np.array, y: np.array, **kwargs):
    """Apply desired function to arrays to get vector objects for 
    plotting

    Params
    ------
    func : callable - function to be applied to the desired coordinate
            arrays: `x` and `y`
    x : numpy.array - 2D-array containing x-coordinate values
    y : numpy.array - 2D-array containing y-coordinate values

    Returns
    -------
    u : np.array - 2D-array of first index of unit vector

    v : np.array - 2D-array of second index of unit vector

    slope: np.array - 2D-array of function result

    mag: np.array - 2D-array of abs value of function result, used as 
            magnitude for unit vectors
    """
    if kwargs:
        slope = func(x, y, **kwargs)
    else:
        slope = func(x, y)
    mag = abs(slope)
    theta = np.atan(slope)
    
    unit_u, unit_v = np.cos(theta), np.sin(theta)
    
    return unit_u, unit_v, slope, mag

if __name__ == "__main__":
    # example plot
    plot_vect_field(
            dumb_funck,
            (-4,4),
            (-4,4),
            density=50,
            title="wunk",
            slope_norm=1)