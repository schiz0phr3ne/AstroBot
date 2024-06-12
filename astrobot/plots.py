from datetime import datetime
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from constants import BODIES, DIRECTIONS


def plot_polar_sky(
    eph,
    obj,
    date
):
    """
    Plot a polar sky map of the celestial sphere.
    
    Args:
        eph (Ephemeris): The Ephemeris object.
        obj (str): The sky object.
        date (datetime): The date.
    
    Returns:
        BytesIO: The BytesIO image.
    """
    # Compute the daily path and the actual position of the object
    alt, az = eph.compute_daily_path(date, obj)
    actual_alt, actual_az = eph.compute_actual_position(date, obj)

    # Get the color and size of the object
    color, size = BODIES[obj]

    # Plot the polar sky map
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('N', offset=0)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.linspace(0, 360, 9), DIRECTIONS)
    ax.set_rgrids(np.linspace(0, 90, 10), [f'{int(i)}°' for i in np.linspace(90, 0, 10)])
    ax.set_rlabel_position(0)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_ylim([0, 90])
    ax.plot(np.radians(az), [90 - a for a in alt], color='k', linewidth=0.8) # Plot the daily path
    ax.plot(np.radians(actual_az), 90 - actual_alt, 'o', color=color, markersize=size) # Plot the actual position
    if obj == 'sun': # Plot the solstices paths if the object is the sun
        summer_solstice, winter_solstice = eph.get_solstices(date.year)
        summer_solstice_alt, summer_solstice_az = eph.compute_daily_path(summer_solstice, obj)
        winter_solstice_alt, winter_solstice_az = eph.compute_daily_path(winter_solstice, obj)

        ax.plot(np.radians(summer_solstice_az), [90 - a for a in summer_solstice_alt], color='gold', linestyle='--', linewidth=0.8)
        ax.plot(np.radians(winter_solstice_az), [90 - a for a in winter_solstice_alt], color='blue', linestyle='--', linewidth=0.8)
    ax.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return buffer
