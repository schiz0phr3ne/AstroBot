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
    
    Args:
        eph (Ephemeris): The Ephemeris object.
        sky_object (str): The sky object.
        date (datetime): The date.
    
    Returns:
        BytesIO: The BytesIO image.
    """
    alt, az = eph.compute_daily_path(date, sky_object)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('N', offset=0)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.linspace(0, 360, 9), DIRECTIONS)
    ax.set_rgrids(np.linspace(0, 90, 10), [f'{int(i)}°' for i in np.linspace(90, 0, 10)])
    ax.set_rlabel_position(0)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_ylim([0, 90])
    ax.plot(np.radians(az), [90 - a for a in alt], color='k', linewidth=0.8)
    ax.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer
