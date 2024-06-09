from matplotlib import pyplot as plt

from .constants import DIRECTIONS

def plot_polar_sky(
    
):
    """
    Plot a polar sky map of the celestial sphere.
    """
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_xticks([i for i in range(0, 360, 45)], DIRECTIONS)
    ax.set_ylim(0, 90)
    ax.set_yticks([i for i in range(0, 100, 10)])
    