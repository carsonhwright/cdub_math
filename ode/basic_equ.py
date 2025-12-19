import numpy as np
from math import log10 as ln

from plot_direction_field import plot_vect_field


def radioactive_decay(x, y, **kwargs):
    """Model radioactive decay
    
    Params
    ------
    x, y: np.array - 2D - Numpy arrays of x and y values 
            respectively, based on linspace density

    **kwargs: requires `d_lambda` (something like `ln(2)/5730` in the 
            context of Carbon-14 for radiocarbon dating)
    """
    # TODO how to handle initial conditions
    d_lambda = kwargs.get("d_lambda")
    assert d_lambda, "Lambda was not defined, kwarg missing: `d_lambda` from call to plot_vect_field"
    # in this case y is the quantity of remaining radio-isotopes
    return (-d_lambda) * y

def newton_heating_cooling():
    """Model newton's laws of heating/cooling"""


def malthusian_growth():
    """Model Malthusian growth model"""

if __name__ == "__main__":
    plot_vect_field(
        radioactive_decay,
        (0,100000),
        (0,100000),
        slope_norm=0,
        density=200,
        title="RadioActiveDecay",
        d_lambda=(ln(2)/5730),
        point=(-10000, 80000)
    )