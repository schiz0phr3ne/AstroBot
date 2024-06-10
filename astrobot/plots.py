from io import BytesIO

import numpy as np
import matplotlib.pyplot as plt

from constants import DIRECTIONS

def plot_polar_sky(
    eph,
    sky_object,
    date
):
    """
    Plot a polar sky map of the celestial sphere.
    
    WIP : This function is not yet well implemented nor tested.
    """
    alt, az, path = eph.compute_daily_path(date, sky_object)
    print(alt)
    print(az)
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location("S")
    ax.set_theta_direction(-1)
    ax.set_xticks(np.pi/180 * np.linspace(0, 360, 8, endpoint=False), DIRECTIONS)
    ax.set_rmax(90)
    ax.set_rticks(list(range(90, -10, -10)), [f"{i}°" for i in range(90, -10, -10)])
    ax.tick_params(axis='y', labelsize=8)
    ax.plot(*path)
    ax.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer
